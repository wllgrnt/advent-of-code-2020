"""
The ID number for the bus is also the time the bus takes to perform its loop.
The bus with ID 5 departs from the sea port at timestamps 0, 5, 10, 15, and so on.
The bus with ID 11 departs at 0, 11, 22, 33, and so on. If you are there when the bus
departs, you can ride that bus to the airport!

The input gives the earliest timestamp you could depart, and a list of bus IDs.

"""
from typing import List, Tuple

test_input = """939
7,13,x,x,59,x,31,19
"""


def parse_input(input_data: str) -> Tuple[int, List[int]]:
    timestamp, buses, _ = input_data.split("\n")
    timestamp = int(timestamp)
    buses = [int(x) for x in buses.split(",") if x != "x"]
    return timestamp, buses

def get_wait_time(departure_time, bus):
    bus_arrival_time = bus * (departure_time // bus + 1)
    wait_time = bus_arrival_time - departure_time
    return wait_time


def get_quickest_bus(departure_time: int, buses: List[int]) -> int:
    """
    Return the wait time multiplied by the quickest bus ID.
    """
    quickest_bus = sorted(buses,
                          key=lambda x: get_wait_time(departure_time, x),
                          reverse=False)[0]

    return get_wait_time(departure_time, quickest_bus) * quickest_bus


departure_time, buses = parse_input(test_input)
assert get_quickest_bus(departure_time, buses) == 295

if __name__ == "__main__":

    with open("input.txt") as flines:
        data = flines.read()
    departure_time, buses = parse_input(data)

    print(get_quickest_bus(departure_time, buses))
