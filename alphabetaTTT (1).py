from tictactoe import TicTacToe
from math import inf as infinity


def evaluate(board):
    if board.wins(TicTacToe.cpu):
        score = +1
    elif board.wins(TicTacToe.human):
        score = -1
    else:
        score = 0
    return score


def game_over(board):
    return board.wins(TicTacToe.human) or board.wins(TicTacToe.cpu)


def minimaxAB(state, depth, alpha, beta, player):
    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [score, None]

    if player == TicTacToe.cpu:
        best = [-infinity, None]
        for cell in state.getnextmoves(TicTacToe.cpu):
            score = [minimaxAB(cell, depth - 1, alpha, beta, TicTacToe.human)[0], cell]
            if score[0] > best[0]:
                best = score  # max value
            alpha = max(alpha, best[0])
            if alpha >= beta:
                break
    else:
        best = [+infinity, None]
        for cell in state.getnextmoves(TicTacToe.human):
            score = [minimaxAB(cell, depth - 1, alpha, beta, TicTacToe.cpu)[0], cell]
            if score[0] < best[0]:
                best = score  # min value
            beta = min(beta, best[0])
            if alpha >= beta:
                break
    return best


if __name__ == '__main__':
    currentBoard = TicTacToe()
    currentBoard.print2d()
    while not game_over(currentBoard):
        move = int(input('Enter Move(1-9): ')) - 1
        if move in currentBoard.emptyindices():
            currentBoard.move(move, TicTacToe.human)
        currentBoard.print2d()
        print(len(currentBoard.emptyindices()))
        if currentBoard.wins(TicTacToe.human):
            break
        currentBoard = minimaxAB(currentBoard, len(currentBoard.emptyindices()), -infinity, +infinity, TicTacToe.cpu)[1]
        currentBoard.print2d()
        if currentBoard.wins(TicTacToe.cpu):
            break
    if currentBoard.wins(TicTacToe.human):
        print('Human Wins!')
    else:
        print('CPU Wins!')
