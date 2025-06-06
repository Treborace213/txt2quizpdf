from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class DocBuilder:
    def __init__(self, name: str):
        self._name = name
        self._doc = SimpleDocTemplate(self._name + ".pdf")
        self._flow = []

        self._styles = getSampleStyleSheet()

        self._flow.append(Paragraph(self._name, self._styles["Title"]))
        self._flow.append(Spacer(1,12))

    def build(self):
        self._doc.build(self._flow);

    def addLine(self, line):
        self._flow.append(Paragraph(line.strip(), self._styles["Normal"]))