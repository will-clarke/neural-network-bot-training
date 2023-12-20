from bot import Bot
from object import Object
from consts import apple_str, empty_str, bot_str


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[empty_str for _ in range(width)] for _ in range(height)]

    def add_object(self, object: Object):
        self.grid[object.y][object.x] = object.value

    def with_bot(self, bot: Bot) -> str:
        return self.draw([bot.object()])

    def move_bot(self, bot: Bot, x: int, y: int):
        (previous_x, previous_y) = bot.get_position()
        bot.move(x, y)
        self[previous_y][previous_x] = empty_str
        # wrap around bot location
        if bot.x >= self.width:
            bot.x = 0
        if bot.y >= self.height:
            bot.y = 0

        if self[bot.y][bot.x] == apple_str:
            bot.apple_count += 1
            self[bot.y][bot.x] = empty_str

    def draw(self, objects: list[Object]) -> str:
        for object in objects:
            self.add_object(object)
        return self.__str__()

    def __str__(self):
        string = ""
        for row in self.grid:
            for item in row:
                string += item + " "
            string += "\n"
        return string

    def __getitem__(self, index):
        return self.grid[index]
