from typing import Final

# game

empty_str: Final[str] = "."
bot_str: Final[str] = "X"
apple_str: Final[str] = "@"


class Object:
    def __init__(self, x: int, y: int, value: str):
        self.x = x
        self.y = y
        self.value = value

    def move(self, x: int, y: int):
        self.x += x
        self.y += y

    def get_position(self):
        return [self.x, self.y]


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[empty_str for _ in range(width)] for _ in range(height)]

    def add_object(self, object: Object):
        self.grid[object.y][object.x] = object.value

    def draw(self, objects: list[Object]) -> str:
        g = Grid(self.width, self.height)
        for object in objects:
            g.add_object(object)
        return g.__str__()

    def __str__(self):
        string = ""
        for row in self.grid:
            for item in row:
                string += item + " "
            string += "\n"
        return string

    def __getitem__(self, index):
        return self.grid[index]


grid = Grid(4, 4)


apples = [
    Object(2, 2, apple_str),
    Object(3, 3, apple_str),
    Object(0, 3, apple_str),
]


class Bot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.apple_count = 0

    def object(self) -> Object:
        return Object(self.x, self.y, bot_str)

    def move(self, x: int, y: int, grid: Grid):
        self.x += x
        self.y += y
        if self.x >= grid.width:
            self.x = 0
        if self.y >= grid.height:
            self.y = 0
        if grid[self.y][self.x] == apple_str:
            self.apple_count += 1
            grid[self.y][self.x] = empty_str

    def get_position(self):
        return [self.x, self.y]

    def __str__(self):
        return f"Bot({self.x}, {self.y} [{self.apple_count}])"


bot = Bot(1, 1)

print(grid.draw([*apples, bot.object()]))
print(bot)
bot.move(1, 0, grid)
print(grid.draw([*apples, bot.object()]))
print(bot)
