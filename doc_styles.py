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
            spaceAfter=32
        ),
        "Normal": ParagraphStyle(
            name="Normal",
            parent=base["Normal"],
            fontSize=14,
            leading=14,
            spaceAfter=8
        )
    }

HorizonalLine = HRFlowable(width="100%", thickness=1, color="black", spaceBefore=16, spaceAfter=16)