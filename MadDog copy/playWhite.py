import pygame
import chess
import tensorflow as tf
import os
import numpy as np
from model import Model

name = "Kasparov"

model = Model(name)

currentDirectory = os.getcwd()

values = {
    '.' : '0',
    'P' : '1',
    'N' : '2',
    'B' : '3',
    'R' : '4',
    'Q' : '5',
    'K' : '6',
    'p' : '12',
    'n' : '22',
    'b' : '32',
    'r' : '42',
    'q' : '52',
    'k' : '62'
}

paths = {
    'p' : f'{currentDirectory}/pieces/BlackPawn.png',
    'P' : f'{currentDirectory}/pieces/WhitePawn.png',
    'n' : f'{currentDirectory}/pieces/BlackNight.png',
    'N' : f'{currentDirectory}/pieces/WhiteNight.png',
    'b' : f'{currentDirectory}/pieces/BlackBishop.png',
    'B' : f'{currentDirectory}/pieces/WhiteBishop.png',
    'r' : f'{currentDirectory}/pieces/BlackRook.png',
    'R' : f'{currentDirectory}/pieces/WhiteRook.png',
    'q' : f'{currentDirectory}/pieces/BlackQueen.png',
    'Q' : f'{currentDirectory}/pieces/WhiteQueen.png',
    'k' : f'{currentDirectory}/pieces/BlackKing.png',
    'K' : f'{currentDirectory}/pieces/WhiteKing.png',
}

def getSimbol(a):
    return chr(ord('a') + a - 1)

def make_matrix(board): #type(board) == chess.Board()
    pgn = board.epd()
    foo = []  #Final board
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = []  #This is the row I make
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('.')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo

def convert_to_text(board):
    matrix = list(make_matrix(board))
    answer = ""
    for i in range(len(matrix)):
        for g in range(len(matrix[i])):
            elem = matrix[i][g]
            answer += values[elem] + ' '
    return answer


board = chess.Board()

name = "Carlsen"

black = (235, 211, 95)
white = (255, 255, 255)
square = 75

pygame.init()
screen = pygame.display.set_mode((square * 8, square * 8))
screen.fill(black)
pygame.display.set_caption(name)
clock = pygame.time.Clock()
running = True

clicked_first = ''
clicked_second = ''

while running:
    matrix = make_matrix(board)
    for i in range(8):
        for g in range(8):
            if (i + g) % 2 == 0:
                color = white
            else:
                color = black
            pygame.draw.rect(screen, color, pygame.Rect(i * square, g * square, square, square))
    for i in range(len(matrix)):
        for g in range(len(matrix[i])):
            if matrix[i][g] == '.':
                continue
            my_image = pygame.image.load(paths[matrix[i][g]]).convert_alpha()
            my_image = pygame.transform.scale(my_image, (square, square))
            my_image = my_image.convert()
            screen.blit(my_image, (i * square, g * square))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the mouse position at the time of the click
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0] // square + 1
            y = mouse_pos[1] // square + 1
            #swap(x, y)

            c = x
            x = y
            y = c

            print(f'x = {x} y = {y}')

            #if make_matrix(board)[x - 1][y - 1] != '.':
            if clicked_first == '':
                simbol = chr(ord('a') + x - 1)
                clicked_first = f'{simbol}{8 - y + 1}'
            else:
                print('a')
                simbol = chr(ord('a') + x - 1)
                clicked_second = f'{simbol}{8 - y + 1}'
                print(f"move = {clicked_first}{clicked_second}")
                move = chess.Move.from_uci(f'{clicked_first}{clicked_second}')
                board.push(move)
                clicked_first = ''
                clicked_second = ''
                print(board)

                bot_move = model.getMove(board)
                print(bot_move)

                board.push(chess.Move.from_uci(bot_move))

            print(f'clicked_first = {clicked_first} clicked_second = {clicked_second}')

            #print("Left mouse button clicked at:", mouse_pos)
    pygame.display.update()
    clock.tick(60) 
  
pygame.quit()
quit()