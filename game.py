from grid import Grid
from consts import GRID_SIZE, APPLE_COUNT, APPLE_STR
from object import Object
import random
from bot import Bot


def play_game():
    grid = Grid(GRID_SIZE, GRID_SIZE)

    apples: set[Object] = set()
    while len(apples) < APPLE_COUNT:
        random_x = random.randint(0, GRID_SIZE - 1)
        random_y = random.randint(0, GRID_SIZE - 1)
        apples.add(Object(random_x, random_y, APPLE_STR))

    for apple in apples:
        grid.add_object(apple)

    bot = Bot(1, 1)
    grid.add_object(bot.object())

    print(grid)
    bot.move(1, 0, grid)
    print(grid)
    bot.move(1, 0, grid)
    print(grid)
