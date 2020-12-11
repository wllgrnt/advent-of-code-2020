"""
Given a list of volatages (plus a 0, and one 3+ higher than the max), return a count of the 
differences.

Part 2:
What is the total number of distinct ways you can arrange
the adapters to connect the charging outlet to your device?
"""
from collections import Counter
from typing import List
import math


def get_diffs(adapters: List[int]) -> List[int]:
    """Sort a list and return the differences between consecutive elements."""
    adapters = sorted(adapters)
    diffs = []
    for i, level in enumerate(adapters[1:], start=1):
        diffs.append(level-adapters[i-1])
    return diffs


def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r)*f(n-r))

if __name__ == "__main__":
    with open("input.txt") as flines:
        adapters = [int(line.strip()) for line in flines]

    # Add the floor and ceiling.
    adapters.append(0)
    adapters.append(max(adapters)+3)
    # sort and get the diffs
    diffs = get_diffs(adapters)
    counter = Counter(diffs)
    
    # Try to be clever with int.
    adapters = sorted(adapters[:-2] + [max(adapters)+3])

    ways = {0 : 1}
    for level in adapters:
        ways[level] = ways.get(level - 1, 0) + ways.get(level - 2, 0) + ways.get(level - 3, 0)
    print(f'Answer: {ways[adapters[-2]]}')
