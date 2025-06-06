import sys
import os
from pathlib import Path

from doc_builder import DocBuilder

def handle_argv():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_input_txt>")
        sys.exit(1)

    input_path = sys.argv[1]
    target_path = os.path.normpath(os.path.expandvars(os.path.expanduser(input_path)))

    if not os.path.isfile(target_path):
        print(f"Error: File does not exist -> {target_path}")
        sys.exit(1)
    return Path(target_path)


def main():
    target_path = handle_argv()
    doc_builder = DocBuilder(target_path.stem)

    with open(target_path, 'r') as text_file:
        for line in text_file:
            doc_builder.add_question(line.strip())

    doc_builder.build();
    print("Generated pdf.")



if __name__ == "__main__":
    main()