# ReversiAI
Simple Reversi AIs.

## Available AIs :
* Random AI : random choice among all possible moves, uniform law
* Weighted AI : random choice among all possibilities, weighted values (better move = higher odds of being picked)
* Heatmap AI : random choice among the best possible moves (those who share the same maximum estimated score), uniform law
* Heatmap Priority AI : if, among the best possible moves, my opponent is able to play one of them, play this move (the first one encountered if there are multiple). Otherwise, use the same decision method as the Heatmap AI.

## AIs performance (tested upon 10.000 games) :
* Random AI : chosen as reference.
* Weighted AI : ~68.11% win rate against the random AI
* Heatmap AI : ~88.91% win rate against the random AI
* Heatmap Priority AI : ~90.45% win rate against the random AI
