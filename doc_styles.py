from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import HRFlowable
from reportlab.lib.enums import TA_CENTER

def styles():
    base = getSampleStyleSheet()

    return {
    "Title": ParagraphStyle(
        name="Title",
        parent=base["Title"],
        fontSize=32,
        alignment=TA_CENTER,
        leading=40,
        spaceBefore=16,
        spaceAfter=16
    ),
    "Subtitle": ParagraphStyle(
        name="Subtitle",
        parent=base["Normal"],
        fontSize=20,
        leading=25,
        spaceBefore=12,
        spaceAfter=12
    ),
    "Normal": ParagraphStyle(
        name="Normal",
        parent=base["Normal"],
        fontSize=14,
        leading=16,
        spaceBefore=10,
        spaceAfter=10
    ),
}

AnswerLine = HRFlowable(width="100%", thickness=1, color="black", spaceBefore=16, spaceAfter=16, dash=(1,2))