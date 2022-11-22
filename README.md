# ReversiAI
Simple Reversi AIs.

## Available AIs
### Regular, fast as heeeell AIs :
* Random AI : Random choice.
* Weighted AI : Random choice but weights different positions using heuristic values.
* Heatmap AI : Using the same heuristic values, chooses one move among the ones with the highest heuristic value.
* DefensiveHeatmapAI : Follow the same pattern as HeatmapAI but if my opponent is able to play one of my best moves, play this one in priority.
* Hindrance AI : Try to prevent my opponent from playing good spots by giving these moves a priority. 

### Ahead looking, slower AIs :
* Greedy AI : Maximizes the number of tiles it covers.
* Move depriving AI : Tries to reduce the number of moves the enemy will be able to play.

## AIs performance
### Fast boys, tested upon 10.000+ games :
* Random AI : chosen as reference.
* Weighted AI : ~68.11% win rate against the random AI.
* Heatmap AI : ~88.91% win rate against the random AI.
* DefensiveHeatmapAI : ~90.26% win rate against the random AI.
* Hindrance AI :  ~90.78% win rate against the random AI.

### Slower babies, tested upon 2.000+ games :
* Greedy AI : ~67.25% win rate against the random AI
* Move depriving AI : ~71.66% win rate against the random AI
