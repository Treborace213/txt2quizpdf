import sys
import os
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_input_txt>")
        sys.exit(1)

    input_path_str = sys.argv[1]
    target_path_str = os.path.normpath(os.path.expandvars(os.path.expanduser(input_path_str)))

    if not os.path.isfile(target_path_str):
        print(f"Error: File does not exist -> {target_path_str}")
        sys.exit(1)

    target_path = Path(target_path_str)

    doc_name = target_path.stem

    doc = SimpleDocTemplate(doc_name + ".pdf")
    styles = getSampleStyleSheet()

    flow = []

    flow.append(Paragraph(doc_name, styles["Title"]))
    flow.append(Spacer(1,12))

    with open(target_path, 'r') as text_file:
        for line in text_file:
            flow.append(Paragraph(line.strip(), styles["Normal"]))
    
    doc.build(flow)
    print("Generated pdf.")



if __name__ == "__main__":
    main()