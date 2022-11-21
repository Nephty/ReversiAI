# ReversiAI
Simple Reversi AIs.

## Available AIs :
* Random AI : Random choice.
* Weighted AI : Random choice but weights different positions using heuristic values.
* Heatmap AI : Using the same heuristic values, chooses one move among the ones with the highest heuristic value.
* Heatmap Priority AI : Follow the same pattern as HeatmapAI but if my opponent is able to play one of my best moves, play this one in priority.
* Hindrance AI : Try to prevent my opponent from playing good spots by giving these moves a priority.
* Evaluating AI : Looks how "good" the game would be for itself after played all possible moves and chooses the one which makes the game the "best" for itself.

## AIs performance (tested upon 10.000 games) :
* Random AI : chosen as reference.
* Weighted AI : ~68.11% win rate against the random AI.
* Heatmap AI : ~88.91% win rate against the random AI.
* Heatmap Priority AI : ~90.26% win rate against the random AI.
* Hindrance AI :  ~90.78% win rate against the random AI.
* Evaluating AI : ~67.25% win rate against the random AI (tested over 2000 games, takes much more time to take a decision)
