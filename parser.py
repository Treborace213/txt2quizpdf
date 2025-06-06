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
            for line in text_file:
                line.strip()

                # Paragraph
                if line[0] == '!':
                    self._doc_builder.add_parragraph(line[1::])
                # Question
                else: 
                    self._doc_builder.add_question(line)