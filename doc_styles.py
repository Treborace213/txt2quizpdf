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
        spaceBefore=25,
        spaceAfter=40
    ),
    "Subtitle": ParagraphStyle(
        name="Subtitle",
        parent=base["Normal"],
        fontSize=20,
        leading=25,
        spaceBefore=18,
        spaceAfter=18
    ),
    "Normal": ParagraphStyle(
        name="Normal",
        parent=base["Normal"],
        fontSize=14,
        leading=16,
        spaceBefore=10,
        spaceAfter=10
    )
}

HorizonalLine = HRFlowable(width="100%", thickness=1, color="black", spaceBefore=16, spaceAfter=16)