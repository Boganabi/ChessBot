"""
responsible for storing all the information about teh current state of a chess game

determines valid moves at the current state

keeps a move log
"""

class GameState():
    def __init__(self):
        # might need to make this a numpy array later
        # board is 8x8 2d list, each element has 2 characters
        # first char is color [w or b] and the second is type of piece [K, Q, R, B, N, or p]
        # two dashes [--] represents an empty space with no piece
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []