"""
Binary space partitioning.
7 chars e.g. FBFBBFF to specify 0-127 rows.

3 chars e.g. RLR to specify 0-7 seats

Seat id is row*8 + column.

What is the highest seat ID on a boarding pass?
"""

def cast_to_number(binary_string: str, zero:str, one: str) -> int:
    binary_string = binary_string.replace(zero, "0").replace(one, "1")
    binary_number = int(binary_string, 2)
    return binary_number

def get_seat_id(boarding_pass:str) -> int:
    row = boarding_pass[:7]
    column = boarding_pass[7:]
    row_number = cast_to_number(row, zero="F", one="B")
    column_number = cast_to_number(column, zero="L", one="R")
    return row_number*8 + column_number

# test input
boarding_pass = "FBFBBFFRLR"
row = boarding_pass[:7]
col = boarding_pass[7:]
assert cast_to_number(row, zero="F", one="B") == 44
assert cast_to_number(col,  zero="L", one="R") == 5
assert get_seat_id(boarding_pass) == 357


if __name__ == "__main__":

    with open("input.txt") as flines:
        boarding_passes = [line.strip() for line in flines]

    # Part 1 - find the max
    print(max([get_seat_id(x) for x in boarding_passes]))
    # Part 2 - find a missing seat with id +=1 existing
    seat_ids = sorted([get_seat_id(x) for x in boarding_passes])
    for i, seat_id in enumerate(seat_ids[1:], start=1):
        if seat_id - seat_ids[i-1] != 1:
            print(seat_id, seat_ids[i-1])