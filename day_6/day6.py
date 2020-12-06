"""
Count the number of questions to which anyone answered yes in each group.
Each group is separated by a blank line.

```
abc

a
b
c

ab
ac

a
a
a
a

b
```
"""
import collections
from typing import List


def count_unique_letters(group: List[str]) -> int:
    counter = collections.Counter("".join(group))
    return len(counter)

def count_common_letters(group: List[str]) -> int:
    counter = collections.Counter("".join(group))
    return sum(1 for key, value in counter.items() if value == len(group))

def sum_unique_letters(groups: List[List[str]]) -> int:
    return sum([count_unique_letters(x) for x in groups])

def sum_common_letters(groups: List[List[str]]) -> int:
    return sum([count_common_letters(x) for x in groups])


test_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""
test_groups = [group.strip().split() for group in test_input.split("\n\n")]
assert [count_unique_letters(x) for x in test_groups] == [3,3,3,1,1]
assert [count_common_letters(x) for x in test_groups] == [3,0,1,1,1]
assert sum_unique_letters(test_groups) == 11
assert sum_common_letters(test_groups) == 6



if __name__ == "__main__":

    with open("input.txt") as flines:
        groups = [group.strip().split() for group in flines.read().split("\n\n")]
    
    print("Sum of unique yes answers:", sum_unique_letters(groups))
    print("Sum of common yes answers:", sum_common_letters(groups))