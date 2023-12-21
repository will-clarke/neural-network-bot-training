from object import Object
from grid import Grid
from consts import BOT_STR, EMPTY_STR, APPLE_STR
from typing import Iterator, Callable
import random
import copy


class Bot:
    def __init__(self, x: int, y: int, grid: Grid):
        self.x = x
        self.y = y
        self.apple_count = 0
        self.grid_history: list[Grid] = [copy.deepcopy(grid)]
        grid.add_object(self.object())

    def object(self) -> Object:
        return Object(self.x, self.y, BOT_STR)

    def move(self, x: int, y: int, grid: Grid):
        grid[self.y][self.x] = EMPTY_STR  # clear previous position
        self.x += x
        self.y += y

        # wrap around bot location
        if self.x >= grid.width:
            self.x = 0
        if self.y >= grid.height:
            self.y = 0

        if grid[self.y][self.x] == APPLE_STR:
            self.apple_count += 1
            grid[self.y][self.x] = EMPTY_STR
        grid[self.y][self.x] = BOT_STR
        self.grid_history.append(copy.deepcopy(grid))

    def get_position(self) -> tuple[int, int]:
        return (self.x, self.y)

    def __str__(self):
        return f"Bot({self.x}, {self.y} [{self.apple_count}])"

    def score(self):
        return self.apple_count

    def make_best_move(self, grid: Grid):
        m = random.choice([move for move in self.possible_moves(grid)])
        m()

    def possible_moves(self, grid: Grid) -> Iterator[Callable]:
        for (x, y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            yield lambda x=x, y=y: self.move(x, y, grid)

    def print_history(self):
        for grid in self.grid_history:
            print(grid)
