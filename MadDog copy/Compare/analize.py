import chess
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class analize:
    def __init__(self, name, game):
        self.model = tf.keras.models.load_model(f'{name}_model.model')
        self.name = name
        self.game = game
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
    
    def Summarize(self, confidence):
        aver = 0
        for i in confidence:
            aver += i
        aver /= len(confidence)
        return aver

    def plot_confidence(self, confidence_player_1, confidence_player_2, best_player_1, best_player_2):
        index_1 = []
        for i in range(len(confidence_player_1)):
            index_1.append(i + 1)
        index_2 = []
        for i in range(len(confidence_player_2)):
            index_2.append(i + 1)
        plt.plot(index_1, confidence_player_1, 'r')
        plt.plot(index_1, best_player_1, 'y')
        plt.plot(index_2, confidence_player_2, 'g')
        plt.plot(index_2, best_player_2, 'b')
        plt.show()

    def maximum(self, mas):
        max = -1e18
        for i in mas:
            if i > max:
                max = i
        return max
    
    def analize(self):
        confidence_player_1 = []
        best_player_1 = []
        confidence_player_2 = []
        best_player_2 = []
        board = chess.Board()
        turn = 0
        for move in self.game.mainline_moves():
            board.push(move)
            #pred = self.model.predict([])
            text_board = self.convert_to_text(board).split()
            cur = []
            for elem in text_board:
                cur.append(int(elem))
            pred = self.model.predict([cur])[0]
            played_move = self.convert_move_to_text(move)
            print(f"[analize] {self.name} is {pred[played_move]} confident in the move {move} ")
            if turn == 0:
                confidence_player_1.append(pred[played_move])
                best_player_1.append(self.maximum(pred))
            else:
                confidence_player_2.append(pred[played_move])
                best_player_2.append(self.maximum(pred))
            turn = abs(turn - 1)
        print(f'RESULT || overall array of confidence for player 1 = {confidence_player_1}')
        print(f'RESULT || overall array of confidence for player 2 = {confidence_player_2}')
        print(f'RESULT || confidence in play of player 1 = {self.Summarize(confidence_player_1)}')
        print(f'RESULT || confidence in play of player 2 = {self.Summarize(confidence_player_2)}')
        self.plot_confidence(confidence_player_1, confidence_player_2, best_player_1, best_player_2)
        


