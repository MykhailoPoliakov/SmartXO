from enum import Enum

class Player(Enum):
    O = 1
    X = 2


    def switch(self) -> Player:
        return Player.X if self is Player.O else Player.O