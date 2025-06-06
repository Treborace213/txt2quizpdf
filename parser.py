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
                l = line.strip()

                # If the length of the line is 0 or 1 skip it.
                if len(l) <= 1:
                    print(f"Line {line_number} skipped: must be at least 2 characters long.")
                elif l == "---":
                    self._doc_builder.add_horizontal_line()
                else:
                    match l[0]:
                        case '!': # Paragraph
                            self._doc_builder.add_parragraph(l[1:])
                        case '$': # Multi char command
                            l = l[1::]
                            try: # Space command
                                if len(l) > 2 and l[0] == '[' and l[-1] == ']':
                                    self._doc_builder.add_spacer(int(l[1:-1]))
                                else:
                                    print(f"Line {line_number} skipped: invalid command.")
                            except (ValueError) as e:
                                print(f"Line {line_number} skipped: space command size is not an integer.")

                        case _: # Question
                            self._doc_builder.add_question(l)