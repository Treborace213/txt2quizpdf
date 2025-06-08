from pathlib import Path

from doc_builder import DocBuilder


class Parser():
    def __init__(self, file_path: Path):
        self._path = file_path
        self._doc_builder = DocBuilder(file_path.stem)

    def build(self):
        self._doc_builder.build()

    def parse(self):
        with open(self._path, 'r', encoding='utf-8') as text_file:
            for line in text_file:
                line.strip()
                match line[0]:
                    # Subtitle
                    case '!':
                        self._doc_builder.add_subtitle(line[1:])
                    # Paragraph
                    case '>':
                        self._doc_builder.add_paragraph(line[1:])
                    # Question
                    case '?': 
                        self._doc_builder.add_question(line[1:])
                    # Page Break
                    case '~':
                        self._doc_builder.add_page_break()