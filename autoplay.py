from player import Player
from board import Board, Square



def autoplay(board: Board, player: Player) -> int:
    lines: list = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (2,4,6), (0,4,8)]
    clock: list = [0, 1, 2, 5, 8, 7, 6, 3,   0, 1, 2, 5, 8, 7, 6, 3]

    pl_sq = Square.O if player == Player.O else Square.X
    op_sq = Square.O if player != Player.O else Square.X


    # critical positions: if 2 player squares in line
    for line in lines:
        board_line = [board[line[0]], board[line[1]], board[line[2]]]
        if board_line.count(pl_sq) == 2 and Square._ in board_line:
            for l in line:
                if board[l] == Square._:
                    return l


    # critical positions: if 2 opponent squares in line
    for line in lines:
        board_line = [board[line[0]], board[line[1]], board[line[2]]]
        if board_line.count(op_sq) == 2 and Square._ in board_line:
            for l in line:
                if board[l] == Square._:
                    return l
                

    # if center is empty / first move
    if board[4] == Square._:
        return 4


    # second move (center taken)
    if board.count(op_sq) == 1 and board.count(pl_sq) == 0:
        return 0
            

    # third move
    if board.count(op_sq) == 1 and board.count(pl_sq) == 1:
        if board[4] == pl_sq:
            if op_sq in [board[0], board[2], board[8], board[6]]:
                return clock[clock.index(board.index(op_sq)) + 4]
            else:
                return clock[clock.index(board.index(op_sq)) + 3]
        else:
            if op_sq in [board[0], board[2], board[8], board[6]]:
                return clock[clock.index(board.index(pl_sq)) + 3]
            else:
                return clock[clock.index(board.index(pl_sq)) + 3]


    # forth move (faced position)
    if board.count(op_sq) == 2 and board.count(pl_sq) == 1:
        if op_sq in [board[0], board[2], board[8], board[6]]:
            return clock[clock.index(board.index(pl_sq)) + 2]
        else:
            return clock[clock.index(board.index(pl_sq)) + 3]



    # any move 
    weights: list = [0] * 9
    for sq in range(9):
        # if square is taken
        if board[sq] != Square._:
            continue

        # for free squares
        weight = 1
        for line in lines:
            # for lines with the square
            if sq in line:
                board_line = [board[line[0]], board[line[1]], board[line[2]]]
                # add weight if place is sussy
                if board_line.count(pl_sq) > 0 and board_line.count(op_sq) == 0:
                    weight += 3
                if board_line.count(pl_sq) == 0 and board_line.count(op_sq) > 0:
                    weight += 2
        weights[sq] = weight

    return weights.index(max(weights))