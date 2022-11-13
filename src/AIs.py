from gameobjects import Game
from random import choice, choices
from random import randint


class AI:
    """
    First AI.
    Decision making process :
      1) Compute all possible moves ;
      2) Keep all moves with the highest heuristic (estimated score,
         how much it would benefit us if we played on a tile) ;
      3) Randomly choose one of the tiles from step 2).
    """
    def __init__(self, color: bool, board_length: int):
        self.heatmap = []
        max_index = board_length - 1
        for line_index in range(board_length):
            for column_index in range(board_length):
                # Corners = 1 (found trying all combinations)
                if (line_index, column_index) in [(0, 0), (0, max_index), (max_index, 0),
                                                  (max_index, max_index)]:
                    self.heatmap.append(1)
                # Next to corner = 0.2 (found trying all combinations)
                elif (line_index, column_index) in [(0, 1), (1, 0),
                                                    (0, max_index - 1), (1, max_index),
                                                    (max_index - 1, 0), (max_index, 1),
                                                    (max_index, max_index - 1), (max_index - 1, max_index)]:
                    self.heatmap.append(0.2)
                # Diagonally next to corner = 0.2 (found trying all combinations)
                elif (line_index, column_index) in [(1, 1), (1, max_index - 1), (max_index - 1, 1),
                                                    (max_index - 1, max_index - 1)]:
                    self.heatmap.append(0.1)
                # Remaining on edges = 0.4 (found trying all combinations)
                elif line_index == 0 or line_index == max_index or column_index == 0 or column_index == max_index:
                    self.heatmap.append(0.5)
                # Remaining on second/before last edges = 0.6 (found trying all combinations)
                elif line_index == 1 or line_index == max_index - 1 or column_index == 1 or column_index == max_index - 1:
                    self.heatmap.append(0.8)
                # 0.4
                else:
                    self.heatmap.append(0.7)
        self.color = color

    def takeDecision(self, game: Game):
        """Takes a decision based on the current state of the game.
        Process : choose one of the moves that has the highest estimated score (heuristic).
        Returns a numerical value based on the conventions."""
        # How does it work ? Glad you asked !
        # The objective is to only list the moves with the highest estimated score. Why ? Doing so, we don't have to
        # compute the maximum of the scores, then keep the moves with this score and finally choose one of them.
        # First, create a list that will contain all the possible moves with a heuristic value of {max_score}
        # Initialize max_score as 0, and iterate over all possible moves
        # We want to append to the possibles moves every move with the known highest score. So, if the move as a higher
        # estimated score, we update max_score and dump every previously stored move (they sucked anyway) and we'll only
        # keep the current move. If the move has a score that is equal to max_score, it's one of the best move at the
        # moment ! We'll keep it warm in the list of possible moves.
        # We then end up with a list of the moves with the highest estimated score and choose one randomly.
        possible_moves = []
        max_score = 0
        positions_method = game.getWhitePlayablePositions if self.color else game.getBlackPlayablePositions
        for index in positions_method():
            if self.heatmap[index] > max_score:
                max_score = self.heatmap[index]
                possible_moves = [index]
            elif self.heatmap[index] == max_score:
                possible_moves.append(index)
        if len(possible_moves) == 1:
            return possible_moves[0]
        else:
            return choice(possible_moves)


class WeightedAI:
    """
    Second AI.
    Decision making process :
      1) Compute all possible moves ;
      2) Randomly choose a move from step 1) with weighted probabilities according to their heuristic.
    """
    def __init__(self, color: bool, board_length: int):
        self.heatmap = []
        max_index = board_length - 1
        for line_index in range(board_length):
            for column_index in range(board_length):
                # Corners = 1 (found trying all combinations)
                if (line_index, column_index) in [(0, 0), (0, max_index), (max_index, 0),
                                                  (max_index, max_index)]:
                    self.heatmap.append(1)
                # Next to corner = 0.2 (found trying all combinations)
                elif (line_index, column_index) in [(0, 1), (1, 0),
                                                    (0, max_index - 1), (1, max_index),
                                                    (max_index - 1, 0), (max_index, 1),
                                                    (max_index, max_index - 1), (max_index - 1, max_index)]:
                    self.heatmap.append(0.2)
                # Diagonally next to corner = 0 (found trying all combinations)
                elif (line_index, column_index) in [(1, 1), (1, max_index - 1), (max_index - 1, 1),
                                                    (max_index - 1, max_index - 1)]:
                    self.heatmap.append(0.2)
                # Remaining on edges = 0.3 (found trying all combinations)
                elif line_index == 0 or line_index == max_index or column_index == 0 or column_index == max_index:
                    self.heatmap.append(0.6)
                # Remaining on second/before last edges = 0.6 (found trying all combinations)
                elif line_index == 1 or line_index == max_index - 1 or column_index == 1 or column_index == max_index - 1:
                    self.heatmap.append(0.6)
                # 0.4
                else:
                    self.heatmap.append(0.4)
        self.color = color

    def takeDecision(self, game: Game):
        """Takes a decision based on the current state of the game.
        Process : choose one of the moves that has the highest estimated score (heuristic).
        Returns a numerical value based on the conventions."""
        possible_moves = []
        # based on the color of the AI, list all possible moves and their estimated score
        # note that in both lists, move of index i corresponds to the score of index i
        # this will be useful when picking the moves with the highest score when there are multiple moves with the
        #   highest estimated score
        positions_method = game.getWhitePlayablePositions if self.color else game.getBlackPlayablePositions
        for index in positions_method():
            possible_moves.append([self.heatmap[index], index])
        return choices([move[1] for move in possible_moves], weights=[move[0] for move in possible_moves])[0]


class RandomAI:
    """
    Randomly choosing AI. Reference for evaluation (considered to be the "worst" AI, or at least I think my AI will
    never be worse than a randomly choosing AI. If so, I'm quitting this project).
    Decision making process :
      1) Compute all possible moves ;
      2) Randomly choose one of the moves from step 1) following a uniform law.
    """
    def __init__(self, color: bool):
        self.color = color

    def takeDecision(self, game: Game):
        """Takes a decision based on the current state of the game.
        Process : choose a random move.
        Returns a numerical value based on the conventions."""
        return choice(game.getWhitePlayablePositions() if self.color else game.getBlackPlayablePositions())
