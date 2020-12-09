"""
The boot code is represented as a text file with one instruction per line of text. 
Each instruction consists of an operation (acc, jmp, or nop) and an argument 
(a signed number like +4 or -20).

    acc increases or decreases a single global value called the accumulator by the value 
        given in the argument. For example, acc +7 would increase the accumulator by 7. 
        The accumulator starts at 0. After an acc instruction, the instruction immediately
        below it is executed next.
    jmp jumps to a new instruction relative to itself. The next instruction to execute is found
        using the argument as an offset from the jmp instruction; for example, jmp +2 would skip
        the next instruction, jmp +1 would continue to the instruction immediately below it, and
        jmp -20 would cause the instruction 20 lines above to be executed next.
    nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.



Run your copy of the boot code. 
Immediately before any instruction is executed a second time, what value is in the accumulator?
"""
from typing import List
from collections import namedtuple
from dataclasses import dataclass
@dataclass
class Instruction:
    arg: str
    op: int
    exec_count: int = 0

class Instructions:
    def __init__(self, input_text=None, path="input.txt"):
        """Create the instruction set from an input file or raw text."""
        if input_text:
            self.instruction_set = _parse_input_data(input_text)
        else:
            with open(path) as flines:
                input_text = [line.strip() for line in flines]
            self.instruction_set = _parse_input_data(input_text)
        self.accumulator = 0
        self.pointer = 0
        self.exec_count = [0]*len(self.instruction_set)

    def run(self):
        """Move along the tape, executing the instructions."""
        while True:
            code = self.execute_instruction()
            if code != 0:
                break
    def execute_instruction(self):
        """Run the instruction at the pointer position."""
        if self.pointer == len(self.instruction_set):
            print(f"Terminating normally with acc {self.accumulator}")
            return 1
        instruction = self.instruction_set[self.pointer]
        instruction.exec_count += 1
        if self.instruction_set[self.pointer].exec_count == 2:
            # Then we're in an infinite loop.
            # print(f"Infinite loop detected: acc {self.accumulator}")
            return 1
        if instruction.op == "acc":
            self.accumulator += instruction.arg
            self.pointer += 1
        elif instruction.op == "jmp":
            self.pointer += instruction.arg
        elif instruction.op == "nop":
            if self.pointer + instruction.arg == len(self.instruction_set):
                print(f"This should be a jmp. Acc {self.accumulator}.")
            self.pointer += 1
        else:
            print(f"Instruction op is {instruction.op}. Should be 'acc', 'jmp', or 'nop'.")
            return 1
        return 0

def _parse_input_data(input_data: List[str]) -> Instructions:
    """Parse each newline-stripped line of the input into a set of Instructions."""
    instruction_set = []
    for line in input_data:
        op, arg = line.split()
        arg = int(arg)
        instruction_set.append(Instruction(arg=arg, op=op))
    return instruction_set

if __name__ == "__main__":

    instructions = Instructions(path="input.txt")
    instructions.run()

    # Look for a rogue jmp or nop
    with open("input.txt") as flines:
        input_text = [line.strip() for line in flines]
    
    jump_positions = []
    for i, line in enumerate(input_text):
        if line.startswith("jmp"):
            jump_positions.append(i)

    for jump_position in jump_positions:
        input_text_altered = input_text.copy()
        input_text_altered[jump_position] = input_text_altered[jump_position].replace("jmp", "nop")
        instructions = Instructions(input_text=input_text_altered)
        instructions.run()
    
    nop_positions = []
    for i, line in enumerate(input_text):
        if line.startswith("nop"):
            nop_positions.append(i)
 
    for nop_position in nop_positions:
        input_text_altered = input_text.copy()
        input_text_altered[nop_position] = input_text_altered[nop_position].replace("nop", "jmp")
        instructions = Instructions(input_text=input_text_altered)
        instructions.run()
   
