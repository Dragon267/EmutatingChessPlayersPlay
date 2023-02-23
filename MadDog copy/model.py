import tensorflow as tf
import chess
import numpy as np
import random

class Model:
    def __init__(self, name):
        self.name = name
        self.model = tf.keras.models.load_model(f'{name}_model.model')
        self.values = {
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
    
    def convert_move_to_text(self, move):
        str_move = str(move)
        x1 = ord(str_move[0]) - ord('a') + 1
        y1 = ord(str_move[1]) - ord('0')
        x2 = ord(str_move[2]) - ord('a') + 1
        y2 = ord(str_move[3]) - ord('0')
        string = f'{x1}{y1}{x2}{y2}'
        add = ((int(string[0]) - 1) * 8 + int(string[1]) - 1) * 64 + ((int(string[2]) - 1) * 8 + int(string[3]) - 1)
        return add

    def getSimbol(self, a):
        return chr(ord('a') + a - 1)

    def make_matrix(self, board): #type(board) == chess.Board()
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

    def convert_to_text(self, board):
        matrix = list(self.make_matrix(board))
        answer = ""
        for i in range(len(matrix)):
            for g in range(len(matrix[i])):
                elem = matrix[i][g]
                answer += self.values[elem] + ' '
        return answer

    def sort_indexes(self, arr):
        return sorted(range(len(arr)), key=lambda i: arr[i], reverse=True)
    
    def getMove(self, board, best_range=3):
        cur = []
        text = self.convert_to_text(board).split()
        for i in text:
            cur.append(int(i))
        pred = self.model.predict([cur])

        print(pred[0])

        ind = self.sort_indexes(pred[0].tolist())

        #print(f'ind = {ind}')

        legal_moves = board.legal_moves

        times = 0

        while True:
            if times > 5:
                break
            wait = random.randint(1, best_range)
            print(f'wait = {wait}')
            pos = 0

            for index in ind:
                #print(f"index = {index}")
                x = index // 64
                y = index % 64
                #((cur[0] - 1) * 8 + cur[1] - 1) * 64 + ((cur[2] - 1) * 8 + cur[3] - 1)
                xx = x // 8 + 1
                xy = x % 8 + 1
                yx = y // 8 + 1
                yy = y % 8 + 1

                bot_move = f'{self.getSimbol(xx)}{xy}{self.getSimbol(yx)}{yy}'

                try:
                    move = chess.Move.from_uci(bot_move)

                    if move in legal_moves:
                        pos += 1
                        if pos == wait:
                            return bot_move
                except:
                    continue
                times += 1
        for index in ind:
            #print(f"index = {index}")
            x = index // 64
            y = index % 64
            #((cur[0] - 1) * 8 + cur[1] - 1) * 64 + ((cur[2] - 1) * 8 + cur[3] - 1)
            xx = x // 8 + 1
            xy = x % 8 + 1
            yx = y // 8 + 1
            yy = y % 8 + 1

            bot_move = f'{self.getSimbol(xx)}{xy}{self.getSimbol(yx)}{yy}'

            try:
                move = chess.Move.from_uci(bot_move)

                if move in legal_moves:
                    return bot_move
            except:
                continue
