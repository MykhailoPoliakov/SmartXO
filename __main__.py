from dataclasses import dataclass
from copy import deepcopy

# Local imports
from player import Player
from board import Board, Result, Square
from autoplay import autoplay


@dataclass
class Game:
    board: Board
    player: Player

    @classmethod
    def init(cls) -> Game:
        return cls(Board.init(), Player.X)


def main():

    history: list[Game] = []
    game: Game = Game.init()
    comment: str = "Game started!"    

    # main loop
    while True:

        # check board for wins and draws
        result = game.board.check()
        match result:
            case Result.WinO: 
                comment = "Game Over! O wins"
            case Result.WinX:
                comment = "Game Over! X wins"
            case Result.Draw:
                comment = "Game Over! it's a Draw"


        # print the UI
        print("\033c")
        game.board.print()
        print(comment)

        
        # get input
        inp = input(f"{" " if result != None else "O" if game.player == Player.O else "X"} > ").strip()

        
        # validate input
        if inp == '':
            comment = "Input was empty! Try again"
            continue

        if inp.lower()[0] in ['q']:
            return

        if inp.lower()[0] in ['r']:
            comment = "Game started!"
            # add old version to the history
            history.append(deepcopy(game))
            # reset the game
            game = Game.init()
            continue

        if inp.lower()[0] in ['z']:
            if history:
                game = history.pop()
                comment = "Undone!"
            else:
                comment = ""
            continue
        
        if result != None:
            continue

        if inp.lower()[0] in ['b']:
            inp = str(autoplay(game.board, game.player) + 1)

        try:
            num = int(inp) - 1 
        except:
            comment = "Invalid input! Try again"
            continue

        if not num in range(9):
            comment = "Invalid input! Enter number 1-9"
            continue

        # if square is taken
        square = Square.O if game.player == Player.O else Square.X
        if not game.board.validate(num, square):
            comment = "Square is taken. Try again"
            continue


        comment = ""
        # add old version to the history
        history.append(deepcopy(game))

        # play the move
        game.board.play(num, square)
        game.player = game.player.switch()
            


if __name__ == "__main__":
    main()