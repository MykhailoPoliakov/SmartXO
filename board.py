from enum import Enum

class Square(Enum):
    _ = 0
    O = 1
    X = 2 


class Result(Enum):
    WinO = 1
    WinX = 2
    Draw = 3


class Board(list[Square]):

    @classmethod
    def init(cls) -> Board:
        return cls([Square._] * 9)


    def print(self):
        count = 1

        first_stat = ["exit - 'q'", "reset - 'r'", ""]
        second_stat = ["undo - 'z'", "autoplay - 'b'", ""]


        print("-------------")
        for i in range(3):
            for j in range(3):
                element: str
                match self[i*3+j]:
                    case Square._: 
                        element = " "
                    case Square.O:  
                        element = "O" 
                    case Square.X:  
                        element = "X" 
                print(f"| {element} ", end='')
            print(f"|     {first_stat[i]}\n--{count}---{count+1}---{count+2}--     {second_stat[i]}")
            count += 3


    def check(self) -> None | Result:
        lines: list = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (2,4,6), (0,4,8)]

        # win check
        for line in lines:
            if self[line[0]] == self[line[1]] == self[line[2]] != Square._:
                return (Result.WinO if self[line[0]] == Square.O else Result.WinX)

        # draw check
        for line in lines:
            if not (Square.O in [self[line[0]], self[line[1]], self[line[2]]] and 
                    Square.X in [self[line[0]], self[line[1]], self[line[2]]]):
                return          
        return Result.Draw


    def validate(self, num: int, square: Square) -> bool: 
        if not num in range(9):
            return False

        # if square is taken
        if self[num] != Square._:
            return False
        
        return True


    def play(self, num: int, square: Square):
        self[num] = square

