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
from AIs import Human, HeatmapAI, RandomAI, WeightedAI, HeatmapPriorityAI, HindranceAI, EvaluatingAI
from time import time


board_length = 8
white = Human(color=True)
black = HindranceAI(color=False)
ai_wins = 0
n = 1
begin = time()

for i in range(1, n+1):
    print(i)
    game = Game()
    playing = True
    turn = True  # color of whose turn it is
    verbose = True
    if verbose:
        print(game)

    while playing:
        if len(game.getPlayableIndices(turn)) > 0:
            if turn:
                decision = white.takeDecision(game)
            else:
                decision = black.takeDecision(game)
            game.playMove(decision, turn, verbose=verbose)
        else:
            print(f"{'White' if turn else 'Black'} skips turn.")
        turn = not turn

        if verbose:
            print(game)
            #print(f"evaluation for white : {whiteBot.evaluateBoard(game)}")

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
