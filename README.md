# EmutatingChessPlayersPlay
A program to emutate how would a chess player play

To create a model of a certain player you need to get .pgn file with a lot of games of that player (1000 minimum). After that run slice.py
and change there the variable name to the name of the player (the name of the file should look like : <name>.pgn and it should be in the folder data).
Then run the file convertPGN.py change the variable name to the name of the player and the variable official_name to how the player is written in the
.pgn file. Then run the file createModel.py and change the name variable to the name of the player. When you will be running the file createModel.py you
could change the tensorflow model to what you need. The model i put there takes ~17 minites to train. A better model could take ~1 hour 30 minites to
train. After this you have the model ready. To make a game review of a game go to Compare/game_review.py and change the variable string_pgn to the pgn
of the game and change in line 20 the model you want to use. Then it will give you a good report of the game. 

Note : Don't listen to what the model says it makes really bad moves here is one of the games it played against a other model

![BLUNDERS](https://user-images.githubusercontent.com/112898086/220990693-afde3513-7f2b-4a5d-8f78-4beb343dd7e7.jpg)

But the model does show you how close you are to the playing style of the player.
