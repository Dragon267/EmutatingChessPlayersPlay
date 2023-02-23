import chess.pgn
import chess
import os

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

def convert_move_to_text(move):
    str_move = str(move)
    x1 = ord(str_move[0]) - ord('a') + 1
    y1 = ord(str_move[1]) - ord('0')
    x2 = ord(str_move[2]) - ord('a') + 1
    y2 = ord(str_move[3]) - ord('0')
    return f'{x1}{y1}{x2}{y2}'

currentDirectory = os.getcwd()
name = "Giri"
official_name = "Giri,A"
path = f'{currentDirectory}/data/{name}'
number_of_games = 100000000

data_board = ""
played_move = ""

for i in range(number_of_games):
    try:
        print(i)
        game_path = f'{path}/{i + 1}.pgn'
        gamei = chess.pgn.read_game(open(game_path))

        player = 0
        if gamei.headers["Black"] == official_name:
            player = 1

        board = chess.Board()
        pos_move = 0
        for move in gamei.mainline_moves():
            if pos_move % 2 == player:
                try:
                    played_move += convert_move_to_text(move) + '\n'
                    data_board += convert_to_text(board) + '\n'
                except:
                    continue
            board.push(move)
            pos_move += 1
    except:
        break

os.mkdir(f'data/{name}_data')

with open(f'{os.getcwd()}/data/{name}_data/x_train.txt', 'w') as file:
    file.write(data_board)
    file.close()

with open(f'{os.getcwd()}/data/{name}_data/y_train.txt', 'w') as file:
    file.write(played_move)
    file.close()