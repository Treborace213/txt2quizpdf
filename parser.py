from instruction import Instruction, InstructionHandler, midLine_chars
from utils import tell_skipped

class Parser():
    def parse(path: str) -> InstructionHandler:
        symbolToInstruction = \
                {instr.value: instr for instr in Instruction}
        
        with open(path, 'r', encoding='utf-8') as file:
            line_number = 0
            line = file.readline()
            
            handler = InstructionHandler()

            while line:
                line_number += 1
                line = line.strip()

                currentRead = ""
                ignoreNextInstructChar = False
                
                # Read each line untill the end is reached.
                for i, char in enumerate(line):
                    if char in midLine_chars and not ignoreNextInstructChar:
                        if char == '\\':
                              ignoreNextInstructChar = True
                        # Break out of the loop as the rest of the chars are comments
                        elif char == '#':
                            break
                        elif char == '|':
                            handler.add_read(currentRead)
                            currentRead = ""
                            handler.add_instruction(symbolToInstruction[char], line_number)
                    else:
                        try:
                            # If first char
                            if i == 0:
                                    handler.add_instruction(symbolToInstruction[line[0]], line_number)
                            else:
                                currentRead += char
                        except KeyError:
                            tell_skipped(line_number, "Unexpected line start")

                # After reading each line - if the line was not empty
                if currentRead.strip():
                    handler.add_read(currentRead)
                    currentRead = ""
                line = file.readline()

        return handler