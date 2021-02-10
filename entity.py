from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc
    """

    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.god_mode = 0

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def toggle_god_mode(self, switch: int):
        self.god_mode ^= switch
        print(self.is_god())

    def is_god(self):
        return self.god_mode == 1
