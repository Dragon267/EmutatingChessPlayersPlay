from model import Model
import chess.pgn
import chess
import os
import random

class fight:
    def __init__(self, name1, name2):
        self.model_1 = Model(name1)
        self.model_2 = Model(name2)
        self.name1 = name1
        self.name2 = name2
    
    def play_game(self, range=3):
        board = chess.Board()
        pos = 0
        while board.is_checkmate() != True and board.can_claim_threefold_repetition() != True and board.can_claim_draw() != True:
            print(f'pos = {pos}')
            bot_1 = self.model_1.getMove(board, best_range=range)
            board.push(chess.Move.from_uci(bot_1))
            bot_2 = self.model_1.getMove(board, best_range=range)
            board.push(chess.Move.from_uci(bot_2))
            pos += 1
        
        game = chess.pgn.Game()
        node = game
        for move in board.move_stack:
            node = node.add_variation(move)

        with open(f'tournament/{self.name1}-{self.name2}-{random.randint(1, 10000)}.pgn', 'w') as file:
            file.write(str(game))
        
        if board.result() == '1-0':
            return 1
        elif board.result() == '0-1':
            return 0
        else:
            return 0.5
