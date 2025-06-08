from enum import Enum
from pathlib import Path

from doc_builder import DocBuilder

class CommandChar(Enum):
    UNKNOWN = None
    SUBTITLE = '!'      # Start of line
    PARAGRAPH = '>'     # Start of line
    QUESTION = '?'      # Start of line
    PAGE_BREAK = '~'    # Start of line
    COMMENT = '#'       # Start of line & inline

    # Functions the same name as 'CommandChar(value)'
    # but if no command exists it returns CommandChar.UNKNOWN
    @classmethod
    def from_value(cls, value: str) -> "CommandChar":
        return next((member for member in cls if member.value == value), cls.UNKNOWN)

class Parser():
    def __init__(self, file_path: Path):
        self._path = file_path
        self._doc_builder = DocBuilder(file_path.stem)

    def build(self):
        self._doc_builder.build()

    def parse(self):
        with open(self._path, 'r', encoding='utf-8') as text_file:
            for line_num, line in enumerate(text_file, start=1):
                line = line.strip()

                # If line is whitespace just ignore it.
                if not line:
                    continue

                # When adding commands with this implimentation,
                # it is key that they are only one char long

                command_char, text = Parser._handle_line_text(line)

                match command_char:
                    case CommandChar.SUBTITLE:
                        self._doc_builder.add_subtitle(text)
                    case CommandChar.PARAGRAPH:
                        self._doc_builder.add_paragraph(text)
                    case CommandChar.QUESTION:
                        self._doc_builder.add_question(text)
                    case CommandChar.PAGE_BREAK:
                        self._doc_builder.add_page_break()
                    case CommandChar.COMMENT:
                        continue
                    case CommandChar.UNKNOWN:
                        print(f"Skipped line: {line_num}. Invalid line start.")

    @staticmethod
    def _handle_line_text(line: str):
        command_char = CommandChar.from_value(line[0])
        text = line[1:]
        read = ""
        for char in text:
            if char == CommandChar.COMMENT.value:
                break
            read += char
        return command_char, read.strip()