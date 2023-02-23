import chess.engine

def stockfish_evaluation(board, time_limit = 0.5):
    engine = chess.engine.SimpleEngine.popen_uci("/Users/danila/Documents/MadDog/Stockfish-master")
    result = engine.analyse(board, chess.engine.Limit(time=time_limit))
    return result['score']

board = chess.Board("rnbqkbnr/ppp1pppp/7B/3p4/3P4/8/PPP1PPPP/RN1QKBNR b KQkq - 0 1")
result = stockfish_evaluation(board)
print(result)