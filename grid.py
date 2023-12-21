from object import Object
from consts import EMPTY_STR


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[EMPTY_STR for _ in range(width)] for _ in range(height)]

    def add_object(self, object: Object):
        self.grid[object.y][object.x] = object.value

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
        return string + "\n\n"

    def __getitem__(self, index):
        return self.grid[index]
