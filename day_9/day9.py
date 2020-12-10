"""
XMAS starts by transmitting a preamble of 25 numbers. After that, each number
you receive should be the sum of any two of the 25 immediately previous numbers.
The two numbers will have different values, and there might be more than one such pair.
## Part one
The first step of attacking the weakness in the XMAS data is to find the first number
in the list (after the preamble) which is not the sum of two of the 25 numbers
before it. What is the first number that does not have this property?
## Part two
Find a contiguous set of at least two numbers in your list which sum to the invalid number
from step 1.
Add together the smallest and largest number in this contiguous range
In this example, these are 15 and 47, producing 62.
"""

from typing import List

PREAMBLE_LENGTH = 25


def is_valid(number: int, prev: List[int]) -> bool:
    """Check if the number is the sum of two of the previous numbers."""
    for i, prev_one in enumerate(prev):
        for prev_two in prev[i+1:]:
            if prev_one + prev_two == number:
                return True
    return False


if __name__ == "__main__":
    with open("input.txt") as flines:
        sequence = [int(x.strip()) for x in flines]

    for i, _ in enumerate(sequence[PREAMBLE_LENGTH:], start=PREAMBLE_LENGTH):
        number = sequence[i]
        prev = sequence[i-PREAMBLE_LENGTH: i]
        if not is_valid(number, prev):
            invalid_number = number

    print(invalid_number)

    # Be dumb: look for threes, then fours, etc.
    found = False
    length = 3
    while not found:
        for i in range(len(sequence) - length):
            subsequence = sequence[i:i+length]
            if sum(subsequence) == invalid_number:
                print(min(subsequence) + max(subsequence))
                found = True
        length += 1