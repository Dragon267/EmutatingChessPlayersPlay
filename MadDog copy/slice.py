import os
import chardet

currentDirectory = os.getcwd()
name = "Giri"

path = f'{currentDirectory}/data/{name}.pgn'

with open(path, 'rb') as f:
    encoding = chardet.detect(f.read())

with open(path, encoding=encoding["encoding"]) as file:
    text = file.readlines()
    file.close()

os.mkdir(f'data/{name}')

pos = 0

games = []
cur = []

for line in text:
    if pos % 2 == 0 and pos != 0:
        games.append(cur)
        cur = []
        pos = 0
    if line == '\n':
        pos += 1
        cur.append(line)
        continue
    cur.append(line)

max_games = 1000000

for i in range(max_games):
    with open(f'{currentDirectory}/data/{name}/{i + 1}.pgn', 'w') as file:
        file.writelines(games[i])
        file.close()
