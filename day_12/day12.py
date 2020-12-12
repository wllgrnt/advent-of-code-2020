"""
The navigation instructions (your puzzle input) consists of a sequence of single-character actions
paired with integer input values. After staring at them for a few minutes, you work out what they
probably mean:

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

Part 2:

    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number
        of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the given number
        of degrees.
    Action F means to move forward to the waypoint a number of times equal to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative
to the ship; that is, if the ship moves, the waypoint moves with it.
"""

import math

from typing import List
from dataclasses import dataclass


@dataclass
class Instruction:
    action: str
    value: int

    def __post_init__(self):
        assert self.action in "NSEWLRF"


class Ferry:
    def __init__(self, instructions: List[str]):
        self.instructions = self._parse_instructions(instructions)
        self.position = [0, 0]
        self.degrees = 0
        self.waypoint_position = [1, 10]

    @property
    def distance(self):
        return abs(self.position[0]) + abs(self.position[1])

    def _parse_instructions(self,
                            instructions: List[str]) -> List[Instruction]:
        instruction_list = []
        for instruction in instructions.split("\n"):
            instruction = instruction.strip()
            if instruction:
                instruction_list.append(
                    Instruction(action=instruction[0],
                                value=int(instruction[1:])))
        return instruction_list

    def __repr__(self):
        return "\n".join(map(repr, self.instructions))

    def follow_instructions_part_one(self) -> int:
        for instruction in self.instructions:
            action = instruction.action
            value = instruction.value
            if action == "N":
                self.position[0] += value
            elif action == "S":
                self.position[0] -= value
            elif action == "E":
                self.position[1] += value
            elif action == "W":
                self.position[1] -= value
            elif action == "L":
                self.degrees += value
            elif action == "R":
                self.degrees -= value
            elif action == "F":
                self.position[1] += round(value *
                                          math.cos(math.radians(self.degrees)))
                self.position[0] += round(value *
                                          math.sin(math.radians(self.degrees)))
        return self.distance

    def follow_instructions_part_two(self) -> int:
        for instruction in self.instructions:
            action = instruction.action
            value = instruction.value
            if action == "N":
                self.waypoint_position[0] += value
            elif action == "S":
                self.waypoint_position[0] -= value
            elif action == "E":
                self.waypoint_position[1] += value
            elif action == "W":
                self.waypoint_position[1] -= value
            elif action == "L":
                # rotate the waypoint around the ship counter-clockwise
                self.waypoint_position[1], self.waypoint_position[0] = _rotate(self.waypoint_position, value)
            elif action == "R":
                # rotate the waypoint around the ship clockwise
                self.waypoint_position[1], self.waypoint_position[0] = _rotate(self.waypoint_position, -value)

            elif action == "F":
                self.position[0] += self.waypoint_position[0] * value
                self.position[1] += self.waypoint_position[1] * value

        return self.distance


def _rotate(position, degrees):
    """I stored my position the wrong way around :/"""
    x = position[1]
    y = position[0]
    x_prime = round(x*math.cos(math.radians(degrees)) - y*math.sin(math.radians(degrees)))
    y_prime = round(x*math.sin(math.radians(degrees)) + y*math.cos(math.radians(degrees)))
    return x_prime, y_prime


test_instructions = """
F10
N3
F7
R90
F11
"""

ferry = Ferry(test_instructions)
assert ferry.follow_instructions_part_one() == 25
ferry = Ferry(test_instructions)
assert ferry.follow_instructions_part_two() == 286

if __name__ == "__main__":
    with open("input.txt") as flines:
        input_data = flines.read()

    ferry = Ferry(input_data)
    print(ferry.follow_instructions_part_one())
    ferry = Ferry(input_data)
    print(ferry.follow_instructions_part_two())
