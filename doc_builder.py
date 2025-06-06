from reportlab.platypus import SimpleDocTemplate, Paragraph
from doc_styles import styles

class DocBuilder:
    def __init__(self, name: str):
        self._name = name
        self._styles = styles()
        self._doc = SimpleDocTemplate(name + ".pdf")
        self._flow = []
        self._questions = []

    def build(self):
        self._flow.append(Paragraph(self._name, self._styles["Title"]))
        self._flow.extend(self._questions)
        self._doc.build(self._flow)

    def add_question(self, question):
        text = f"{len(self._questions) + 1}: {question}"
        self._questions.append(Paragraph(text, self._styles["Normal"]))