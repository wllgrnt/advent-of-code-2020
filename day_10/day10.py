"""
Given a list of volatages (plus a 0, and one 3+ higher than the max), return a count of the 
differences.
"""
from collections import Counter
from typing import List


def get_diffs(adapters: List[int]) -> List[int]:
    """Sort a list and return the differences between consecutive elements."""
    adapters = sorted(adapters)
    diffs = []
    for i, level in enumerate(adapters[1:], start=1):
        diffs.append(level-adapters[i-1])
    return diffs


if __name__ == "__main__":
    with open("input.txt") as flines:
        adapters = [int(line.strip()) for line in flines]

    # Add the floor and ceiling.
    adapters.append(0)
    adapters.append(max(adapters)+3)
    # sort and get the diffs
    diffs = get_diffs(adapters)
    counter = Counter(diffs)
    print(counter[1]*counter[3])
