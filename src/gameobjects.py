from math import sqrt
from time import time


class Board:
    def __init__(self, board: list = None):
        if board is not None and int(sqrt(len(board))) ** 2 != len(board):
            raise ValueError("Board length must be a perfect square.")
        self.board = [
            None,   None,   None,   None,   None,   None,   None,   None,
            None,   None,   None,   None,   None,   None,   None,   None,
            None,   None,   None,   None,   None,   None,   None,   None,
            None,   None,   None,   True,   False,  None,   None,   None,
            None,   None,   None,   False,  True,   None,   None,   None,
            None,   None,   None,   None,   None,   None,   None,   None,
            None,   None,   None,   None,   None,   None,   None,   None,
            None,   None,   None,   None,   None,   None,   None,   None
        ] if board is None else board
        self.length = int(sqrt(len(self.board)))

        if board is None:
            self.whiteCount = 2
            self.blackCount = 2
        else:
            self.whiteCount = 0
            self.blackCount = 0
            for i in board:
                if i:
                    self.whiteCount += 1
                else:
                    self.blackCount += 1
        self.whitePlayablePositions = self.getWhitePlayablePositions()
        self.blackPlayablePositions = self.getBlackPlayablePositions()

    def __setitem__(self, key, value):
        # if the tile is not empty, we are changing the color of the piece on it (we are capturing it)
        # so, we need to remove one from the count of the opponent color
        # if the tile is empty, nothing has to be done
        if self.board[key] is not None:
            if value:
                self.blackCount -= 1
            else:
                self.whiteCount -= 1
        # set the new value for the tile
        self.board[key] = value
        # if we are not emptying a tile, add one to the count of the color we are placing down
        if value is not None:
            if value:
                self.whiteCount += 1
            else:
                self.blackCount += 1

    def __str__(self):
        """Returns the board as a nicely formatted string."""
        board_as_str = ""
        empty = " "
        white = "○"
        black = "◉"
        for i in range(len(self.board)):
            value = empty if self.board[i] is None else white if self.board[i] else black
            trailing_spaces_count = 3 - len(str(value))
            if (i + 1) % self.length == 0:
                board_as_str += f"{value}{' ' * trailing_spaces_count}\n"
            else:
                board_as_str += f"{value}{' ' * trailing_spaces_count}"
        return board_as_str

    def getPlayablePositions(self, color: bool) -> tuple[int, ...]:
        """Returns all playable positions as indices for the given color following the board convention."""
        if color:
            return self.getWhitePlayablePositions()
        return self.getBlackPlayablePositions()

    def getWhitePlayablePositions(self) -> tuple[int, ...]:
        """Returns all positions that are playable by the white player."""
        playable_indices = []
        for index in range(self.length ** 2):
            if self.isPlayable(index, True):
                playable_indices.append(index)
        return tuple(playable_indices)

    def getBlackPlayablePositions(self) -> tuple[int]:
        """Returns all positions that are playable by the black player."""
        playable_indices = []
        for index in range(self.length ** 2):
            if self.isPlayable(index, False):
                playable_indices.append(index)
        return tuple(playable_indices)

    def getUpperNeighbor(self, index: int) -> int:
        """Returns the index of the upper neighbor of the given position.
        Returns None if the position has no upper neighbor."""
        return index - self.length if self.length <= index < self.length ** 2 and self.board[index - self.length] \
            is not None else None

    def getUpperRightNeighbor(self, index: int) -> int:
        """Returns the index of the upper right neighbor of the given position.
        Returns None if the position has no upper neighbor."""
        return index - self.length + 1 if self.length <= index and (index + 1) % self.length != 0 \
            and self.board[index - self.length + 1] is not None and index < self.length ** 2 else None

    def getRightNeighbor(self, index: int) -> int:
        """Returns the index of the right neighbor of the given position.
        Returns None if the position has no right neighbor."""
        return index + 1 if (index + 1) % self.length != 0 and self.board[index + 1] is not None \
            and index < self.length ** 2 else None

    def getLowerRightNeighbor(self, index: int) -> int:
        """Returns the index of the lower right neighbor of the given position.
        Returns None if the position has no upper neighbor."""
        return index + self.length + 1 if index < self.length ** 2 - 1 - self.length \
            and (index + 1) % self.length != 0 and self.board[index + self.length + 1] is not None \
            and index < self.length ** 2 else None

    def getLowerNeighbor(self, index: int) -> int:
        """Returns the index of the lower neighbor of the given position.
        Returns None if the position has no lower neighbor."""
        return index + self.length if index < self.length ** 2 - 1 - self.length and self.board[index + self.length] \
            is not None and index < self.length ** 2 else None

    def getLowerLeftNeighbor(self, index: int) -> int:
        """Returns the index of the lower left neighbor of the given position.
        Returns None if the position has no upper neighbor."""
        return index + self.length - 1 if index < self.length ** 2 - 1 - self.length and index % self.length != 0 \
            and self.board[index + self.length - 1] is not None and index < self.length ** 2 else None

    def getLeftNeighbor(self, index: int) -> int:
        """Returns the index of the left neighbor of the given position.
        Returns None if the position has no left neighbor."""
        return index - 1 if index % self.length != 0 and self.board[index - 1] is not None \
            and index < self.length ** 2 else None

    def getUpperLeftNeighbor(self, index: int) -> int:
        """Returns the index of the upper left neighbor of the given position.
        Returns None if the position has no upper neighbor."""
        return index - self.length - 1 if self.length ** 2 > index >= self.length and index % self.length != 0 \
            and self.board[index - self.length - 1] is not None else None

    def isPlayable(self, index: int, color: bool) -> bool:
        """Checks if the cell at the given index is playable by the player with the given color.
        We use a method we'll call 'quick removal' where we check all the neighbors of the cell, and if they are None,
        we won't even bother calling the _isPlayableByDirection method upon them to reduce computational time.
        """
        for direction in [0, 1, 2, 3, 4, 5, 6, 7]:
            if self._isPlayableByDirection(index, color, direction):
                return True
        return False

    def _matchDirectionToCheckNeighborMethodAndIteratorIncrement(self, direction: int) -> tuple[callable, int]:
        checkNeighborMethod = None
        incrementIteratorBy = None
        if direction == 0:
            checkNeighborMethod = self.getUpperNeighbor
            incrementIteratorBy = - self.length
        elif direction == 1:
            checkNeighborMethod = self.getUpperNeighbor
            incrementIteratorBy = - self.length + 1
        elif direction == 2:
            checkNeighborMethod = self.getRightNeighbor
            incrementIteratorBy = 1
        elif direction == 3:
            checkNeighborMethod = self.getLowerRightNeighbor
            incrementIteratorBy = self.length + 1
        elif direction == 4:
            checkNeighborMethod = self.getLowerNeighbor
            incrementIteratorBy = self.length
        elif direction == 5:
            checkNeighborMethod = self.getLowerLeftNeighbor
            incrementIteratorBy = self.length - 1
        elif direction == 6:
            checkNeighborMethod = self.getLeftNeighbor
            incrementIteratorBy = -1
        elif direction == 7:
            checkNeighborMethod = self.getUpperLeftNeighbor
            incrementIteratorBy = - self.length - 1
        return checkNeighborMethod, incrementIteratorBy

    def _isPlayableByDirection(self, index: int, color: bool, direction: int) -> bool:
        """Checks if the cell at the given index is playable by the player with the given color by checking the given
        direction. Checking the given direction means that we look at the row/column in the given direction and check
        if it allows for a move, that is, if it contains an alignment of positions owned by the other player and one
        position owned by the current player.

        Example :
        Checking the left direction :
        . . B W W W X .
        The X position is playable by the black color, because it is followed on the left by an alignment of white
        positions and a black position.
        """
        # TODO : this method represents ~66% of the entire game's time if we add up all calls to it
        # check if the position is available
        if self.board[index] is not None:
            return False

        # the right method to check for neighbors
        # and how the iterator will vary (go up, right, down or left by changing the index)
        checkNeighborMethod, incrementIteratorBy = self._matchDirectionToCheckNeighborMethodAndIteratorIncrement(direction)

        # check that there is at least two neighbors in the given direction
        if checkNeighborMethod(index) is None:
            return False
        if checkNeighborMethod(checkNeighborMethod(index)) is None:
            return False

        iterating_index = index
        hasFoundOpponentPiece = False

        # iterate over all neighbors in the given direction :
        # if we encounter an opponent piece, mark it down in a boolean variable
        # if we encounter an allied piece :
        #   - if we have already encountered an enemy  : original position is playable !
        #   - if we have not encountered any enemy yet : original position is not playable :(
        while checkNeighborMethod(iterating_index) is not None:
            # change iterating_index to the position of the next upper neighbor
            iterating_index += incrementIteratorBy

            if not hasFoundOpponentPiece:
                if self.board[iterating_index] is None or self.board[iterating_index] is color:
                    return False
                elif self.board[iterating_index] is not color:
                    hasFoundOpponentPiece = True
            else:
                if self.board[iterating_index] is None:
                    return False
                elif self.board[iterating_index] is color:
                    return True

        # if we have iterated over all upper neighbors but haven't found an ally piece following enemy pieces,
        # the position is not playable
        return False

    def playMove(self, index: int, color: bool) -> None:
        """Plays the given move : places a piece of the given color at the given index.
        Assumes the move is allowed and doesn't check if it is legal."""
        flip_indices = []  # indices of pieces that must change color because of the move
        playable_directions = []
        # gather all playable directions from the given index
        for direction in [0, 1, 2, 3, 4, 5, 6, 7]:
            if self._isPlayableByDirection(index, color, direction):
                playable_directions.append(direction)
        # iterate over all neighbors in all playable direction and mark them
        for playable_direction in playable_directions:
            checkNeighborMethod, incrementIteratorBy = self._matchDirectionToCheckNeighborMethodAndIteratorIncrement(
                playable_direction)
            iterating_index = index
            opponent_color = False if color else True
            while checkNeighborMethod(iterating_index) is not None and self.board[checkNeighborMethod(iterating_index)] is opponent_color:
                # change iterating_index to the position of the next upper neighbor
                iterating_index += incrementIteratorBy
                flip_indices.append(iterating_index)

        # flip every neighbor that we marked just before
        for flip_index in flip_indices:
            self[flip_index] = color

        # put down a new piece (the played move)
        self[index] = color

        # TODO : most costly operation (~75% of the method execution time is spent here)
        self.updatePlayablePositions()

    def isFull(self):
        """Returns whether the game is finished or not (based upon remaining tiles to play upon)."""
        return self.whiteCount + self.blackCount == len(self.board)

    def updatePlayablePositions(self):
        """Updates the locally stored playable positions as to relieve computational load."""
        self.whitePlayablePositions = self.getWhitePlayablePositions()
        self.blackPlayablePositions = self.getBlackPlayablePositions()


class Game:
    def __init__(self, board: Board = None):
        self.board = Board() if board is None else board

    def __str__(self):
        """Returns the board of the game as a nicely formatted string."""
        return self.board.__str__()

    def getPlayablePositions(self, color: bool) -> tuple[int, ...]:
        """Returns all playable positions of the board as indices for the given color following the board convention."""
        if color:
            return self.getWhitePlayablePositions()
        return self.getBlackPlayablePositions()

    def getWhitePlayablePositions(self) -> tuple[int, ...]:
        """Returns all positions that are playable by the white player."""
        return self.board.whitePlayablePositions

    def getBlackPlayablePositions(self) -> tuple[int]:
        """Returns all positions that are playable by the black player."""
        return self.board.blackPlayablePositions

    def playMove(self, index: int, color: bool, verbose: bool = False) -> None:
        """Plays the given move : places a piece of the given color at the given index.
        Assumes the move is allowed and doesn't check if it is legal."""
        self.board.playMove(index, color)
        if verbose:
            print(f"Played move '{'White' if color else 'Black'}' on tile {index}")

    def isFinished(self):
        """Returns whether the game is finished or not (based upon remaining tiles to play upon)."""
        return self.board.isFull() or self.board.whiteCount == 0 or self.board.blackCount == 0 or \
            (len(self.board.whitePlayablePositions) + len(self.board.blackPlayablePositions) == 0)

    def conclude(self, verbose=bool) -> int:
        """Concludes the game by checking who wins and printing the results. Returns the winning color."""
        winner = True if self.board.whiteCount > self.board.blackCount else False if self.board.whiteCount < self.board.blackCount else None
        if verbose:
            print(f"{'White wins !' if winner else 'Black wins !' if winner is False else 'Tie !'} - (W >   {self.board.whiteCount} - {self.board.blackCount}   < B)")
        return winner
