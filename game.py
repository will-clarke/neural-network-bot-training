from grid import Grid
from consts import GRID_SIZE, APPLE_COUNT, APPLE_STR, NUMBER_OF_MOVES
from object import Object
import random
from bot import Bot


class Game:
    def __init__(self):
        # new square grid
        self.grid = Grid(GRID_SIZE, GRID_SIZE)

        # randomize apple positions
        self.apples: set[Object] = set()
        while len(self.apples) < APPLE_COUNT:
            random_x = random.randint(0, GRID_SIZE - 1)
            random_y = random.randint(0, GRID_SIZE - 1)
            self.apples.add(Object(random_x, random_y, APPLE_STR))
        for apple in self.apples:
            self.grid.add_object(apple)

        # randomize bot position
        random_x = random.randint(0, GRID_SIZE - 1)
        random_y = random.randint(0, GRID_SIZE - 1)
        self.bot = Bot(random_x, random_y, self.grid)

    def play(self):
        for move in range(NUMBER_OF_MOVES):
            self.bot.make_best_move(self.grid)
