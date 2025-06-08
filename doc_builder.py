from reportlab.platypus import SimpleDocTemplate, KeepTogether, Paragraph, Spacer, PageBreak
from doc_styles import styles, AnswerLine
from document_flow import DocumentFlow, SectionType

class DocBuilder:
    def __init__(self, name: str):
        self._name = name
        self._styles = styles()
        self._doc = SimpleDocTemplate(name + ".pdf")
        self._flow = DocumentFlow()
        self._question_count = 0

        self._flow.add(Paragraph(self._name, self._styles["Title"]), SectionType.TITLE)

    def build(self):
        self._doc.build(self._flow.get_flow())

    def add_question(self, question: str):
        # Reset question count if the question does not follow another question
        if self._flow.get_last_added_type() != SectionType.QUESTION:
            self._question_count = 0

        self._question_count += 1
        text = f"{self._question_count}. {question}"
        self._flow.add(KeepTogether([
                Paragraph(text, self._styles["Normal"]),
                Spacer(1, 10),
                AnswerLine,
            ]), SectionType.QUESTION)

    def add_paragraph(self, text: str):
        self._flow.add(Paragraph(text, self._styles["Normal"]), SectionType.PARAGRAPH)

    def add_subtitle(self, text: str):
        self._flow.add(Paragraph(text, self._styles["Subtitle"]), SectionType.SUBTITLE)

    def add_page_break(self):
        self._flow.add(PageBreak(), SectionType.PAGEBREAK)