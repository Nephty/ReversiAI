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

## Performance

| AI Type               | Games Tested | Win Rate vs Random AI |
|-----------------------|--------------|-----------------------|
| Random AI (Reference)  | 10,000+      | Reference             |
| Weighted AI            | 10,000+      | ~68.11%               |
| Heatmap AI             | 10,000+      | ~88.91%               |
| DefensiveHeatmapAI     | 10,000+      | ~90.26%               |
| Hindrance AI           | 10,000+      | ~90.78%               |
| Greedy AI              | 2,000+       | ~67.25%               |
| Move Depriving AI      | 2,000+       | ~71.66%               |
