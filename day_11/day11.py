"""
All decisions are based on the number of occupied seats adjacent to a given seat
(one of the eight positions immediately up, down, left, right, or diagonal from
the seat). The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the
    seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied,
    the seat becomes empty. Otherwise, the seat's state does not change.
"""


class Grid:
    def __init__(self, input_string: str):
        self.grid = input_string.split("\n")

    def step_two(self):
        """Go through one step of the seating process."""
        new_grid = []
        for i, row in enumerate(self.grid):
            new_row = ""
            for j, item in enumerate(row):
                # rule one
                if item == "L" and self._visible_neighbours(i, j) == 0:
                # if item == "L" and self._num_neighbours(i, j) == 0:
                    new_row += "#"
                elif item == "#" and self._visible_neighbours(i, j) >= 5:
                # elif item == "#" and self._num_neighbours(i, j) >= 4:
                    new_row += "L"
                else:
                    new_row += item
            assert len(new_row) == len(row)
            new_grid.append(new_row)
        self.grid = new_grid

    def step(self):
        """Go through one step of the seating process."""
        new_grid = []
        for i, row in enumerate(self.grid):
            new_row = ""
            for j, item in enumerate(row):
                # rule one
                if item == "L" and self._num_neighbours(i, j) == 0:
                    new_row += "#"
                elif item == "#" and self._num_neighbours(i, j) >= 4:
                    new_row += "L"
                else:
                    new_row += item
            assert len(new_row) == len(row)
            new_grid.append(new_row)
        self.grid = new_grid

    def __repr__(self):
        return "\n".join(self.grid)

    def _num_neighbours(self, i: int, j: int) -> int:
        """Return the num of neighbours of position [i,j]."""
        num_neighbours = 0
        for row_index in [i-1, i, i+1]:
            for col_index in [j-1, j, j+1]:
                try:
                    if col_index < 0 or row_index < 0 or (row_index == i and col_index == j):
                        continue
                    if self.grid[row_index][col_index] == "#":
                        num_neighbours += 1
                except IndexError:
                    continue
        return num_neighbours

    def _visible_neighbours(self, i: int, j: int) -> int:
        """Return the number of neighbours visible in a straight line.
        (you can see through '.' but not 'L' """
        num_neighbours = 0
        for row_direction in [-1, 0, +1]:
            for col_direction in [-1, 0, +1]:
                if row_direction == col_direction == 0:
                    continue
                row_index = i + row_direction
                col_index = j + col_direction
                while 0 <= row_index < len(self.grid) and 0 <= col_index < len(self.grid[0]):
                    try:
                        seat = self.grid[row_index][col_index]
                    except IndexError:
                        print(row_index, len(self.grid), col_index,  len(self.grid[0]))
                        break
                    if seat == "L":
                        break
                    elif seat == "#":
                        num_neighbours += 1
                        break
                    else:
                        row_index += row_direction
                        col_index += col_direction
        return num_neighbours

    @property
    def occupancy(self):
        return sum([row.count("#") for row in self.grid])

    def run(self, logging=False) -> int:
        """Step until stable."""
        prev_occupancy = -1
        while True:
            self.step()
            if logging:
                print(self.occupancy)
            if self.occupancy == prev_occupancy:
                return self.occupancy
            prev_occupancy = self.occupancy

    def run_two(self, logging=False) -> int:
        """Step_two until stable."""
        prev_occupancy = -1
        while True:
            self.step_two()
            if logging:
                print(self.occupancy)
            if self.occupancy == prev_occupancy:
                return self.occupancy
            prev_occupancy = self.occupancy

test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

test_grid = Grid(test_input)
assert test_grid.run() == 37


test_grid = Grid(test_input)
assert test_grid.run_two() == 26

if __name__ == "__main__":

    with open("input.txt") as flines:
        data = flines.read()

    grid = Grid(data)
    print(grid.run())

    grid = Grid(data)
    print(grid.run_two())