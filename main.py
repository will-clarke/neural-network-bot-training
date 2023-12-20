# game

from grid import Grid, apple_str
from object import Object
from bot import Bot


grid = Grid(4, 4)
apples = [
    Object(2, 2, apple_str),
    Object(3, 3, apple_str),
    Object(3, 0, apple_str),
]

print(grid.draw(apples))
for apple in apples:
    grid.add_object(apple)

print(grid)


bot = Bot(1, 1)

print(grid.with_bot(bot))
print(bot)
grid.move_bot(bot, 1, 0)

print(grid.with_bot(bot))
print(bot)

grid.move_bot(bot, 0, 1)
print(grid.with_bot(bot))
print(bot)
grid.move_bot(bot, 0, 1)
print(grid.with_bot(bot))
print(bot)
