from collections import deque
from enum import Enum
from reportlab.platypus import SimpleDocTemplate, KeepTogether, Paragraph, Spacer, PageBreak

from doc_styles import styles, HorizonalLine
from instruction import Instruction, InstructionHandler
from utils import tell_skipped

class _BuildStates(Enum):
    NORMAL = "NORMAL"
    QUESTIONLIST = "QUESTIONLIST"
    NUMQUESTIONLIST = "NUMQUESTIONLIST"
    WAITINGFORAWNSER = "WAITINGFORAWNSER"

def _tell_skipped_ext(line_number: int, wrong_instruciton: Instruction):
    tell_skipped(line_number, f"Unexpected '{wrong_instruciton.value}'")


class DocBuilder:
    def __init__(self, name: str):
        self._styles = styles()
        self._question_doc = SimpleDocTemplate(name + ".pdf")
        self._answer_doc = SimpleDocTemplate(name + "-answers.pdf")

        self._question_sheet_flow = []
        self._answer_sheet_flow = []

    def build(self, instructions: InstructionHandler):
        state = deque()
        state.append(_BuildStates.NORMAL)
        while instructions.has_instructions():
            instruction, line_number = instructions.pop_instruction()
            skip = False

            match instruction:
                case Instruction.STARTQUESTIONLIST:
                    if state[-1] != _BuildStates.NORMAL:
                        skip = True
                    else:
                        state.append(_BuildStates.QUESTIONLIST)

                case Instruction.ENDQUESTIONLIST:
                    if state[-1] != _BuildStates.QUESTIONLIST:
                        skip = True
                    else:
                        state.pop()

                case Instruction.STARTNUMQUESTIONLIST:
                    if state[-1] != _BuildStates.NORMAL:
                        skip = True
                    else:
                        state.append(_BuildStates.NUMQUESTIONLIST)
                        self._question_count = 0

                case Instruction.ENDNUMQUESTIONLIST:
                    if state[-1] != _BuildStates.NUMQUESTIONLIST:
                        skip = True
                    else:
                        state.pop()

                case Instruction.QUESTION:
                    if state[-1] not in (_BuildStates.QUESTIONLIST, _BuildStates.NUMQUESTIONLIST):
                        skip = True
                    else:
                        self._add_question(instructions.pop_read(), state[-1])
                        state.append(_BuildStates.WAITINGFORAWNSER)

                case Instruction.QUESTIONWITHSPACE:
                    if state[-1] not in (_BuildStates.QUESTIONLIST, _BuildStates.NUMQUESTIONLIST):
                        skip = True
                    else:
                        self._add_question(instructions.pop_read(), state[-1], answer_space=True)
                        state.append(_BuildStates.WAITINGFORAWNSER)

                case Instruction.ANSWER:
                    if state[-1] != _BuildStates.WAITINGFORAWNSER:
                        skip = True
                    else:
                        self._add_awnser(instructions.pop_read())
                        state.pop()
                
                case Instruction.TITLE:
                    if state[-1] not in \
                        (_BuildStates.NORMAL, _BuildStates.QUESTIONLIST, _BuildStates.NUMQUESTIONLIST):
                        skip = True
                    else:
                        self._add_title(instructions.pop_read())
                    
                case Instruction.PARA:
                    if state[-1] not in \
                        (_BuildStates.NORMAL, _BuildStates.QUESTIONLIST, _BuildStates.NUMQUESTIONLIST):
                        skip = True
                    else:
                        self._add_paragraph(instructions.pop_read())

                case Instruction.HORIZONTALLINE:
                    if state[-1] not in \
                        (_BuildStates.NORMAL, _BuildStates.QUESTIONLIST, _BuildStates.NUMQUESTIONLIST):
                        skip = True
                    else:
                        self._add_horizontal_line()

                case Instruction.VERTICALSPACE:
                    if state[-1] not in \
                        (_BuildStates.NORMAL, _BuildStates.QUESTIONLIST, _BuildStates.NUMQUESTIONLIST):
                        skip = True
                    else:
                        try:
                            height = int(instructions.pop_read())
                            self._add_spacer(height)
                        except ValueError as e:
                            tell_skipped(line_number, f"Expected numeric spacer height, got invalid value: {e}")

                case Instruction.PAGEBREAK:
                    if state[-1] not in \
                        (_BuildStates.NORMAL, _BuildStates.QUESTIONLIST, _BuildStates.NUMQUESTIONLIST):
                        skip = True
                    else:
                        self._add_page_break()

            if skip:
                _tell_skipped_ext(line_number, instruction)

        self._question_doc.build(self._question_sheet_flow)
        self._answer_doc.build(self._answer_sheet_flow)

    def _add_question(self, question: str, state: _BuildStates, answer_space: bool = False):
        if (state == _BuildStates.NUMQUESTIONLIST):
            self._question_count += 1
            question = f"{self._question_count}. {question}"

        para = Paragraph(question, self._styles["Normal"])

        # Question Sheet
        if answer_space:
            self._question_sheet_flow.append(KeepTogether([
                    para,
                    Spacer(1, 30),
                    HorizonalLine(),
                ]))
        else:
            self._question_sheet_flow.append(para)

        #Answer Sheet
        self._answer_sheet_flow.append(Paragraph(f"Q: {question}", self._styles["Normal"]))

    def _add_awnser(self, answer: str):
        self._answer_sheet_flow.append(Paragraph(f"A: {answer}",  self._styles["Normal"]))

    def _add_title(self, text: str):
        self._question_sheet_flow.append(Paragraph(text, self._styles["Title"]))
        self._answer_sheet_flow.append(Paragraph(text, self._styles["Title"]))

    def _add_paragraph(self, text: str):
         para = KeepTogether([
                Paragraph(text, self._styles["Normal"]),
                Spacer(1, 10)
            ])
         self._question_sheet_flow.append(para)
         self._answer_sheet_flow.append(para)

    def _add_horizontal_line(self):
        self._question_sheet_flow.append(HorizonalLine())
        self._answer_sheet_flow.append(HorizonalLine())

    def _add_spacer(self, height: int):
        self._question_sheet_flow.append(Spacer(1,height))
        self._answer_sheet_flow.append(Spacer(1,height))

    def _add_page_break(self):
        self._question_sheet_flow.append(PageBreak())
        self._answer_sheet_flow.append(PageBreak())