from model import Model
import chess
from ELO.elosports.elo import Elo
import random
from play_game import fight

players = ["Carlsen", "Kasparov", "Giri"]

system = Elo(k=32)

for player in players:
    system.addPlayer(player, rating=1000)

games = 5
acc = 2

results = []

for i in range(games):
    player_1 = ''
    player_2 = ''
    while player_1 == player_2:
        player_1 = players[random.randint(0, len(players) - 1)]
        player_2 = players[random.randint(0, len(players) - 1)]
    print(f'player_1 = {player_1}, player_2 = {player_2}')
    arena = fight(player_1, player_2)
    result = arena.play_game(range=acc)
    if result == 1:
        system.gameOver(winner=player_1, loser=player_2, winnerHome=False)
    elif result == 0:
        system.gameOver(winner=player_2, loser=player_1, winnerHome=False)
    print(f'result = {result}')

    results.append(result)

print(f'ratings of players : ')
for player in players:
    print(f'ratings of {player} is {system.ratingDict[player]}')

print(f'res = {results}')

