from object import Object
from grid import Grid
from consts import BOT_STR, EMPTY_STR, APPLE_STR


class Bot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.apple_count = 0

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

    def get_position(self) -> tuple[int, int]:
        return (self.x, self.y)

    def __str__(self):
        return f"Bot({self.x}, {self.y} [{self.apple_count}])"

    # def move_bot(self, x: int, y: int):
    #     self[previous_y][previous_x] = empty_str
    #     # wrap around bot location
    #     if bot.x >= self.width:
    #         bot.x = 0
    #     if bot.y >= self.height:
    #         bot.y = 0
    #
    #     if self[bot.y][bot.x] == apple_str:
    #         bot.apple_count += 1
    #         self[bot.y][bot.x] = empty_str

    def score(self):
        return self.apple_count

    # The following are the only options for the bot to use:
    # Up / Down / Left / Right
