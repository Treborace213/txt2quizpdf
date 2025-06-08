from reportlab.platypus import SimpleDocTemplate, KeepTogether, Paragraph, Spacer, PageBreak
from doc_styles import styles, AnswerLine

class DocBuilder:
    def __init__(self, name: str):
        self._name = name
        self._styles = styles()
        self._doc = SimpleDocTemplate(name + ".pdf")
        self._flow = []
        self._question_count = 0

        self._flow.append(Paragraph(self._name, self._styles["Title"]))

    def build(self):
        self._doc.build(self._flow)

    def add_question(self, question: str):
        self._question_count += 1
        text = f"{self._question_count}. {question}"
        self._flow.append(KeepTogether([
                Paragraph(text, self._styles["Normal"]),
                Spacer(1, 10),
                AnswerLine,
            ]))

    def add_paragraph(self, text: str):
        self._flow.append(Paragraph(text, self._styles["Normal"]))
        self._flow.append(Spacer(1, 10))

    def add_subtitle(self, text: str):
        self._flow.append(Paragraph(text, self._styles["Subtitle"]))

    def add_page_break(self):
        self._flow.append(PageBreak())