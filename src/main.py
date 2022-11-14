"""
A Reversi AI.
Conventions :

a) Cells & colors
    - White : True
    - Black : False
    - Empty : None
b) Directions :
    - Up : 0
    - Up/Right diagonal : 1
    - Right : 2
    - Down/Right diagonal : 3
    - Down : 4
    - Down/Left diagonal : 5
    - Left : 6
    - Up/Left diagonal : 7
c) Moves :
    - Place on tile of index x : x
    - Skip turn : -1
A white/black position is a tile of the board containing a white/black piece.
"""

from gameobjects import Game, Board
from AIs import AI, RandomAI, WeightedAI
from time import time
import matplotlib.pyplot as plt


board_length = 8
whiteBot = AI(color=True, board_length=8)
blackBot = RandomAI(color=False)
ai_wins = 0
n = 1
begin = time()

for i in range(1, n+1):
    print(i)
    game = Game()  # ~ 1ms to create the board
    playing = True
    turn = True  # color of whose turn it is
    verbose = True
    while playing:
        print("\n"*20)
        print("SPACER")
        if turn:
            # takeDecision represents ~1% of computational time whereas playMove represents ~99%
            if len(game.getWhitePlayablePositions()) > 0:
                decision = whiteBot.takeDecision(game)
                print("took decision") # TODO DOUBLE CALL TO CHECK PLAYABLE ? RUN AND SEE CONSOLE, SEEMS TO BE RAN TWICE IN PLAY MOVE
                game.playMove(decision, True, verbose=verbose)
                print("played move")
        else:
            if len(game.getBlackPlayablePositions()) > 0:
                decision = blackBot.takeDecision(game)
                print("took decision")
                game.playMove(decision, False, verbose=verbose)
                print("played move")
        turn = not turn
        if game.isFinished():
            playing = False
            winner = game.conclude(verbose=verbose)
            if winner:
                ai_wins += 1
end = time()


print(f"Summary :\n"
      f"{n} games played over {round(end - begin, 1)} seconds ({round((end - begin)/n, 3)} sec/game).\n"
      f"{ai_wins} wins for the AI.\n"
      f"{n - ai_wins} wins for the random AI.\n"
      f"\n"
      f"{ai_wins} - {n - ai_wins} => {round(100*ai_wins/n, 2)}% win rate for the AI.")

""""
for diag_next in range(6):
    for edge in range(6):
        for secon_b_last_edge in range(6):
            for other in range(6):
                whiteBot = AI(color=True, board_length=8, a=diag_next*modificator, b=edge*modificator,
                              c=secon_b_last_edge*modificator, d=other*modificator)

                for i in range(n):
                    board = Board()
                    game = Game(board=board)

                    playing = True
                    turn = True  # color of whose turn it is
                    verbose = False

                    while playing:
                        if turn:
                            if len(game.getWhitePlayablePositions()) > 0:
                                game.playMove(whiteBot.takeDecision(game), True, verbose=verbose)
                        else:
                            if len(game.getBlackPlayablePositions()) > 0:
                                game.playMove(blackBot.takeDecision(game), False, verbose=verbose)
                        turn = not turn
                        if game.isFinished():
                            playing = False
                            winner = game.conclude(verbose=verbose)
                            if winner:
                                ai_wins += 1
                            else:
                                random_ai_wins += 1

                res.append([round(ai_wins/n, 2), [diag_next*modificator, edge*modificator, secon_b_last_edge*modificator, other*modificator]])
                ai_wins = 0
                random_ai_wins = 0
                print(res)

end = time()
res = sorted(res, key=lambda x:x[0])
print()
print()
print()
print()
print(end-begin)
print(res)
"""

"""

plt.stem([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], win_rates)
plt.show()
"""

