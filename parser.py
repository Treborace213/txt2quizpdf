from pathlib import Path

from doc_builder import DocBuilder


class Parser():
    def __init__(self, file_path: Path):
        self._path = file_path
        self._doc_builder = DocBuilder(file_path.stem)

    def build(self):
        self._doc_builder.build()

    def parse(self):
        with open(self._path, 'r') as text_file:
            for line_number, line in enumerate(text_file, start=1):
                line = line.strip()

                # If the length of the line is 0 or 1 skip it.
                if len(line) <= 1:
                    print(f"Line {line_number} skipped: must be at least 2 characters long.")
                elif line == "---":
                    self._doc_builder.add_horizontal_line()
                else:
                    match line[0]:
                        case '!': # Paragraph
                            self._doc_builder.add_parragraph(line[1::])
                        case _: # Question
                            self._doc_builder.add_question(line)