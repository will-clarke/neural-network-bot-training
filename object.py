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

    def __hash__(self):
        return hash((self.x, self.y, self.value))
