import sys
import os
from pathlib import Path

from doc_builder import DocBuilder

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
    doc_builder = DocBuilder(doc_name)

    with open(target_path, 'r') as text_file:
        for line in text_file:
            doc_builder.addLine(line.strip())

    doc_builder.build();
    
    print("Generated pdf.")



if __name__ == "__main__":
    main()