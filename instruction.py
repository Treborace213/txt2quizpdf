from enum import Enum
from queue import Queue
from typing import Tuple

class Instruction(Enum):
    STARTQUESTIONLIST = '('
    ENDQUESTIONLIST = ')'
    STARTNUMQUESTIONLIST = '['
    ENDNUMQUESTIONLIST = ']'
    QUESTION = '?'
    QUESTIONWITHSPACE = '_'
    ANSWER = '|'
    TITLE = '!'
    PARA = '@'
    HORIZONTALLINE = '-'
    VERTICALSPACE = '~'
    PAGEBREAK = '+'

midLine_chars = [
    '\\', # If encountered check the next char to see if it is any of the following
    '#', # If encountered ignore all remaining chars on the line
    '|' # If encountered add current read to the buffer, add this instruction to the instruction buffer, read untill EOL.
]

class InstructionHandler():
    def __init__(self):
        self._instruction_buffer = Queue()
        self._instruction_line_numbers = Queue()
        self._read_buffer = Queue()

    def add_instruction(self, instruction: Instruction, line_number: int):
        self._instruction_buffer.put(instruction)
        self._instruction_line_numbers.put(line_number)

    def add_read(self, read: str):
        self._read_buffer.put(read.strip())

    def pop_instruction(self) -> Tuple[Instruction, int]:
        return self._instruction_buffer.get(), self._instruction_line_numbers.get()
    
    def pop_read(self) -> str:
        return self._read_buffer.get()
    
    def has_instructions(self) -> bool:
        return not self._instruction_buffer.empty()