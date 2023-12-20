from object import Object
from consts import apple_str, empty_str, bot_str


class Bot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.apple_count = 0

    def object(self) -> Object:
        return Object(self.x, self.y, bot_str)

    def move(self, x: int, y: int):
        self.x += x
        self.y += y

    def get_position(self) -> tuple[int, int]:
        return (self.x, self.y)

    def __str__(self):
        return f"Bot({self.x}, {self.y} [{self.apple_count}])"
