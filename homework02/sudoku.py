import pathlib
import typing as tp
from random import randint

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    return [values[i:i + n] for i in range(0, len(values), n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    (row, col) = pos
    arr = []
    for i in range(len(grid(row))):
        arr += [grid[row][i]]
    return arr


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    (row, col) = pos
    arr = []
    for i in range(len(grid)):
        arr += [grid[i][col]]
    return arr


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    (row, col) = pos
    line = (row // 3) * 3
    cl = (col // 3) * 3
    arr = []
    for i in range(line, line + 3):
        for j in range(cl, cl + 3):
            arr += [grid[i][j]]
    return arr


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                return i, j
    return None



def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:

    lot = set(str(i) for i in range(1, 10))
    row = get_row(grid, pos)
    col = get_col(grid, pos)
    block = get_block(grid, pos)
    for i in row:
        lot.discard(i)
    for i in col:
        lot.discard(i)
    for i in block:
        lot.discard(i)
    return lot


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    pos = find_empty_positions(grid)
    if not pos:
        return grid
    else:
        lot = find_possible_values(grid, pos)
        (row, col) = pos
        for i in lot:
            grid[row][col] = lot
            if solve(grid):
                return grid
            grid[row][col] = "."
        return None

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    # TODO: Add doctests with bad puzzles
    lot = set("123456789")
    for row in solution:
        if set(row) != lot:
            return False
    for col in range(9):
        pos = (0, col)
        if set(get_col(solution, pos)) != lot:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            pos = (i, j)
            bl = get_block(solution, pos)
            if set(bl) != lot:
                return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:

    empt = [["." for i in range(9)] for j in range(9)]
    grid = solve(empt)
    if grid is None:
        return empt
    if N > 81:
        N = 81
    place = 81 - N
    for i in range(place):
        row = randint(0, 8)
        col = randint(0, 8)
        while grid[row][col] == ".":
            row = randint(0, 8)
            col = randint(0, 8)
        grid[row][col] = "."
    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
