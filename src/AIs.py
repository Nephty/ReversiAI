from gameobjects import Game, Board
from random import choice, choices
from random import randint
from re import match


class Human:
    def __init__(self, color: bool, board_length: int = 8):
        self.color = color
        self.board_length = board_length

    def formatInputToIndex(self, game: Game, move: str):
        if move.startswith('('):
            move = move[1:]
        if move.endswith(')'):
            move = move[:-1]
        result = []
        result.append(int(move.split(",")[0]))
        result.append(int(move.split(",")[1]))
        return (result[1] - 1) * game.board.length + result[0] - 1

    # TODO : check if player can play the position lol
    def takeDecision(self, game: Game) -> int:
        print(f"{'White' if self.color else 'Black'}'s turn.\n"
              f"Enter a move in the following format : (a, b) or a, b\n"
              f"  where a is the column number (from 1 to {self.board_length})\n"
              f"  and b is the row number (from 1 to {self.board_length})")
        input_message = ">> "
        move = input(input_message)
        repeat_input = True
        move_index = -1
        while repeat_input:
            detailed_playable_positions = game.getWhitePlayablePositions() if self.color else game.getBlackPlayablePositions()
            if match("\(?[0-9]+,\s+[0-9]+\)?", move):
                move_index = self.formatInputToIndex(game, move)
                if True in detailed_playable_positions[move_index]:
                    repeat_input = False
                else:
                    print("Sorry, invalid move.")
            elif move.lower().strip() == "help":
                helper = HindranceAI(self.color)
                index = helper.getOrderedEnemyAndOwnPossibleMoves(game)[0]
                print(f"I suggest you play {(index + 1) % game.board.length + 1}, {(index + 1) // game.board.length + 1}")
            else:
                print("Sorry, couldn't read your move.")
            if repeat_input:
                move = input(input_message)
        return move_index


class RandomAI:
    """
    Randomly choosing AI. Reference for evaluation (considered to be the "worst" AI, or at least I think my AIs will
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
        detailed_positions = game.getWhitePlayablePositions() if self.color else game.getBlackPlayablePositions()
        playable_positions = []
        for position in range(len(detailed_positions)):
            if True in detailed_positions[position]:
                playable_positions.append(position)
        return choice(playable_positions)


class HeatmapAI:
    """
    Heatmap AI.
    Decision making process :
      1) Compute all possible moves ;
      2) Keep all moves with the highest heuristic (estimated score,
         how much it would benefit us if we played on a tile) ;
      3) Randomly choose one of the tiles from step 2).
    """
    def __init__(self, color: bool, board_length: int = 8):
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

    def getBestPossibleMoves(self, game: Game):
        # How does it work ? Glad you asked !
        # The objective is to only list the moves with the highest estimated score. Why ? Doing so, we don't have to
        # compute the maximum of the scores, then keep the moves with this score and finally choose one of them.
        # First, create a list that will contain all the possible moves with a heuristic value of {max_score}
        # Initialize max_score as 0, and iterate over all possible moves
        # We want to append to the possibles moves every move with the known highest score. So, if the move as a higher
        # estimated score, we update max_score and dump every previously stored move (they sucked anyway) and we'll only
        # keep the current move. If the move has a score that is equal to max_score, it's one of the best move at the
        # moment ! We'll keep it warm in the list of possible moves.
        # We then end up with a list of the moves with the highest estimated score.
        possible_moves = []
        max_score = 0
        detailed_positions = game.getWhitePlayablePositions() if self.color else game.getBlackPlayablePositions()
        playable_positions = []
        for position in range(len(detailed_positions)):
            if True in detailed_positions[position]:
                playable_positions.append(position)
        for index in playable_positions:
            if self.heatmap[index] > max_score:
                max_score = self.heatmap[index]
                possible_moves = [index]
            elif self.heatmap[index] == max_score:
                possible_moves.append(index)
        return possible_moves

    def takeDecision(self, game: Game):
        """Takes a decision based on the current state of the game.
        Process : choose one of the moves that has the highest estimated score (heuristic).
        Returns a numerical value based on the conventions."""
        possible_moves = self.getBestPossibleMoves(game)
        if len(possible_moves) == 1:
            return possible_moves[0]
        else:
            return choice(possible_moves)

    def evaluatedBoardBi(self, board: Board):
        """
        Fully evaluated the board : takes both white and black positions into account.
        :param board: the ongoing game
        :return: a score indicating how "good" the game is going : positive score means
        the game is going good for us, negative score means the game is going good for
        the opponent. The score's absolute value shows how much the game is in favor of
        either player.
        NB : this method isn't located in the Board or Game class because it is considered
        a "skill" of some AIs and the game is evaluated by the AI and its point of view
        upon the game. For example : the random AI doesn't have this skill, thus it shouldn't
        know how to evaluate the board.
        """
        score = 0
        for tile_index in range(len(board)):
            if board.board[tile_index] is self.color:
                score += self.heatmap[tile_index]
            elif board.board[tile_index] is (not self.color):
                score -= self.heatmap[tile_index]
        return score

    def evaluateBoardMono(self, board: Board, color: bool = None):
        """
        Evaluates the board for a single color. The value of the score will always be
        positive and indicates how good the game is going for the color.
        Warning : a score of 1 returned by evaluateBoardMono is not the same as a score
        of 1 returned by evaluateBoardBi. Mono returns 1 because your positions give you
        a score of 1, whereas Bi returns 1 because your positions are better than the ones
        of your opponent by a scalar of 1 (this means that in a game where Bi returns 1,
        Mono could return 5, 7, 10... ; it all depends on the opponent's positions).
        NB : this method isn't located in the Board or Game class because it is considered
        a "skill" of some AIs and the game is evaluated by the AI and its point of view
        upon the game. For example : the random AI doesn't have this skill, thus it shouldn't
        know how to evaluate the board.
        :param board: the ongoing game
        :param color: the color of the player whose positions will be evaluated. This parameter
        can be changed for the color of the opponent, since this method enables the AI to
        evaluated how good the opponent's positions are (the AI is aware of the full board, and not
        only its positions). None by default means that we evaluated the player upon who this method
        is called.
        :return: a score indicating how "good" the player's positions are.
        """
        if color is None:
            color = self.color
        score = 0
        for tile_index in range(len(board.board)):
            if board.board[tile_index] is color:
                score += self.heatmap[tile_index]
        return score


class WeightedAI(HeatmapAI):
    """
    Weighted AI.
    Decision making process :
      1) Compute all possible moves ;
      2) Randomly choose a move from step 1) with weighted probabilities according to their heuristic.
    """
    def __init__(self, color: bool, board_length: int = 8):
        super(WeightedAI, self).__init__(color, board_length)

    def takeDecision(self, game: Game):
        """Takes a decision based on the current state of the game.
        Process : choose one of the moves that has the highest estimated score (heuristic).
        Returns a numerical value based on the conventions."""
        possible_moves = []
        # based on the color of the AI, list all possible moves and their estimated score
        # note that in both lists, move of index i corresponds to the score of index i
        # this will be useful when picking the moves with the highest score when there are multiple moves with the
        #   highest estimated score
        positions = game.getPlayableIndices(self.color)
        for index in positions:
            possible_moves.append([self.heatmap[index], index])
        return choices([move[1] for move in possible_moves], weights=[move[0] for move in possible_moves])[0]


class HeatmapPriorityAI(HeatmapAI):
    """
    Heatmap Priority AI.
    Decision making process :
      1) Compute all possible moves ;
      2) Keep all moves with the highest heuristic (estimated score,
         how much it would benefit us if we played on a tile) ;
      3) If the enemy can play one of these moves, we shall play the first one we encounter ;
      4) Otherwise, randomly choose one of the tiles from step 2).
    """
    def __init__(self, color: bool, board_length: int = 8):
        super(HeatmapPriorityAI, self).__init__(color, board_length)

    def takeDecision(self, game: Game):
        possible_moves = self.getBestPossibleMoves(game)
        for index in possible_moves:
            enemy_positions = game.getBlackPlayablePositions() if self.color else game.getWhitePlayablePositions()
            if True in enemy_positions[index]:
                return index
        if len(possible_moves) == 1:
            return possible_moves[0]
        else:
            return choice(possible_moves)


class HindranceAI(HeatmapAI):
    """
    Hindrance AI.
    Decision making process :
      1) Compute all possible moves of the enemy ;
      2) Order these move according to their heuristic (estimated score,
         how much it would benefit us if we played on a tile) but only keep those who have a score
         of at least the score of a tile on the edge (this means we will only play on enemy playable
         tiles that are corners, edges and before last edges ;
      3) If the enemy can play one of these moves, we shall play the first one we encounter (because
         they are sorted) ;
      4) If none of the enemy tiles are playable, follow the Heatmap Priority AI decision method.
    """
    def __init__(self, color: bool, board_length: int = 8):
        super(HindranceAI, self).__init__(color, board_length)

    def getOrderedEnemyAndOwnPossibleMoves(self, game: Game):
        # I honestly have no idea how to name the vars so I gave them explicit names
        enemy_playable_indices = game.getPlayableIndices(not self.color)
        my_playable_indices = game.getPlayableIndices(self.color)

        my_playable_indices_and_score = [(index, self.heatmap[index]) for index in my_playable_indices]
        my_playable_indices_and_score_sorted = sorted(my_playable_indices_and_score, key=lambda x:x[1], reverse=True)

        min_score_for_steal = self.heatmap[2]
        enemy_playable_indices_that_i_can_play = list(set(enemy_playable_indices) & set(my_playable_indices))
        enemy_playable_indices_and_score_that_i_can_play_and_will_steal = [(index, self.heatmap[index]) for index in enemy_playable_indices_that_i_can_play if self.heatmap[index] >= min_score_for_steal]
        enemy_playable_indices_and_score_that_i_can_play_and_will_steal_sorted = sorted(enemy_playable_indices_and_score_that_i_can_play_and_will_steal, key=lambda x:x[1], reverse=True)

        enemy_corners = []
        enemy_other_positions = []
        my_corners = []
        my_other_positions = []

        for move_index, move_score in enemy_playable_indices_and_score_that_i_can_play_and_will_steal_sorted:
            if move_score >= self.heatmap[0]:
                enemy_corners.append(move_index)
            else:
                enemy_other_positions.append(move_index)

        for move_index, move_sore in my_playable_indices_and_score_sorted:
            if move_sore >= self.heatmap[0]:
                my_corners.append(move_index)
            else:
                my_other_positions.append(move_index)

        return enemy_corners + enemy_other_positions + my_corners + my_other_positions

    def takeDecision(self, game: Game):
        return self.getOrderedEnemyAndOwnPossibleMoves(game)[0]


class GreedyAI(HeatmapAI):
    """
    Evaluating AI.
    Decision making process :
      1) For all possible moves, evaluate how many positions you own after a move
      2) Play the move that gives you the most positions
    """
    def __init__(self, color: bool, board_length: int = 8):
        super(GreedyAI, self).__init__(color, board_length)

    def takeDecision(self, game: Game):
        possible_moves = game.getPlayableIndices(self.color)
        scores = []
        for move in possible_moves:
            scores.append(self.evaluateBoardMono(game.getBoardResultAfterMove(move, self.color)))
        return possible_moves[scores.index(max(scores))]


class MoveDeprivingAI(HeatmapAI):
    """
    Move depriving AI.
    Decision making process :
      1) For all possible moves, evaluate how many positions will be playable by the enemy AI.
      2) If I can play a corner, do so
      3) If not, play the move that gives the enemy the least playable positions
    """
    def __init__(self, color: bool, board_length: int = 8):
        super(MoveDeprivingAI, self).__init__(color, board_length)

    def takeDecision(self, game: Game):
        possible_moves = game.getPlayableIndices(self.color)
        number_of_enemy_possible_moves = []
        currently_possible_moves = len(game.getPlayableIndices(not self.color))
        for move in possible_moves:
            step = game.getBoardResultAfterMove(move, self.color)
            new_number_of_possible_moves = len(step.getPlayableIndices(not self.color))
            number_of_enemy_possible_moves.append(new_number_of_possible_moves - currently_possible_moves)
            if self.heatmap[move] == self.heatmap[0]:
                return move
        return possible_moves[number_of_enemy_possible_moves.index(min(number_of_enemy_possible_moves))]
