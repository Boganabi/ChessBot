"""
Main driver file for handling user input and displaying current GameState object
"""

import pygame as p
import chessEngine

WIDTH = HEIGHT = 512 # 400 is another option
DIMENSION = 8 # chessboard is 8x8
MULTIPLIER = 1 # 3.5

SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animations later

IMAGES = {}

'''
init a global dict of images, called once in main
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("pieces/testPieces/" + piece + ".png"), (SQ_SIZE * MULTIPLIER, SQ_SIZE * MULTIPLIER))
        # IMAGES[piece] = p.image.load("pieces/" + piece + ".svg")
        # note that we can access an image by saying IMAGES['wp']

'''
main driver for code, handling user input and updating graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState()

    loadImages() # only do once

    running = True
    sqSelected = () # no square selected initially, keeps track of user (tuple: (row, col))
    playerClicks = [] # keep track of player clicks (two tuples: [(6, 4), (4, 4)])

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col): # check to see if square was clicked twice
                    sqSelected = () # deselect
                    playerClicks = [] # clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # append for both 1st and 2nd clicks
                
                if len(playerClicks) == 2: # after 2nd click
                    move = chessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () # reset user clicks
                    playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
responsible for graphics within current game state
'''
def drawGameState(screen, gs):
    drawBoard(screen) # draw squares on the board
    # add in piece highlighting or move suggestion later
    drawPieces(screen, gs.board) # draw pieces on top of squares

'''
draw the squares on the board
top left is always light square
'''
def drawBoard(screen):
    colors = [p.Color(255, 217, 183), p.Color(135, 99, 67)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)] # even squares are white, odd are black
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
draw the pieces on tha board using current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": # not empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()