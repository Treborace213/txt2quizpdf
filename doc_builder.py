from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from doc_styles import styles, HorizonalLine

class DocBuilder:
    def __init__(self, name: str):
        self._name = name
        self._styles = styles()
        self._doc = SimpleDocTemplate(name + ".pdf")
        self._flow = []
        self._questions = []

    def build(self):
        self._flow.append(Paragraph(self._name, self._styles["Title"]))
        for question in self._questions:
            self._flow.append(question)
            self._flow.append(Spacer(1, 10))
            self._flow.append(HorizonalLine)
        self._doc.build(self._flow)

    def add_question(self, question):
        text = f"{len(self._questions) + 1}: {question}"
        self._questions.append(Paragraph(text, self._styles["Normal"]))