import random

from gameobjects import Game, Board
from time import time
from random import randint

board_list = [
    None,   None,   None,   None,   None,   None,   None,   None,
    None,   None,   None,   None,   None,   None,   None,   None,
    None,   None,   None,   None,   None,   True,   None,   None,
    None,   None,   None,   True,   True,   None,   None,   None,
    None,   False,  False,  False,  False,  None,   None,   None,
    None,   None,   None,   None,   False,  None,   None,   None,
    None,   None,   None,   None,   None,   None,   None,   None,
    None,   None,   None,   None,   None,   None,   None,   None
]
board = Board(board_list)
game = Game(board=board)


def testEqual(value, expected):
    if value != expected:
        raise AssertionError(f"Test failed.\n"
                             f"    Expected result : {expected}\n"
                             f"                Got : {value}")


def testGetUpperNeighbor():
    testEqual(game.board.getUpperNeighbor(0), None)  # None, has no upper neighbor, is first row
    print(f"Test equal passed >> game.board.getUpperNeighbor(0), None")
    testEqual(game.board.getUpperNeighbor(26), None)  # True, has no upper neighbor
    print(f"Test equal passed >> game.board.getUpperNeighbor(26), None")
    testEqual(game.board.getUpperNeighbor(29), 29-8)  # None, has upper neighbor (True)
    print(f"Test equal passed >> game.board.getUpperNeighbor(29), 29-8")
    testEqual(game.board.getUpperNeighbor(41), 41-8)  # None, has upper neighbor (False)
    print(f"Test equal passed >> game.board.getUpperNeighbor(41), 41-8")


def testGetUpperRightNeighbor():
    testEqual(game.board.getUpperRightNeighbor(7), None)  # None, has no upper right neighbor, is upper right corner
    print(f"Test equal passed >> game.board.getUpperRightNeighbor(7), None")
    testEqual(game.board.getUpperRightNeighbor(21), None)  # True, has no upper right neighbor
    print(f"Test equal passed >> game.board.getUpperRightNeighbor(21), None")
    testEqual(game.board.getUpperRightNeighbor(28), 28-7)  # True, has upper right neighbor (True)
    print(f"Test equal passed >> game.board.getUpperRightNeighbor(28), 28-7")
    testEqual(game.board.getUpperRightNeighbor(51), 51-7)  # None, has upper right neighbor (False)
    print(f"Test equal passed >> game.board.getUpperRightNeighbor(51), 51-7")


def testGetRightNeighbor():
    testEqual(game.board.getRightNeighbor(14), None)  # None, has no right neighbor, is right side
    print(f"Test equal passed >> game.board.getRightNeighbor(14), None")
    testEqual(game.board.getRightNeighbor(21), None)  # True, has no right neighbor
    print(f"Test equal passed >> game.board.getRightNeighbor(21), None")
    testEqual(game.board.getRightNeighbor(27), 27+1)  # True, has right neighbor (True)
    print(f"Test equal passed >> game.board.getRightNeighbor(28), 28+1")
    testEqual(game.board.getRightNeighbor(32), 32+1)  # None, has right neighbor (False)
    print(f"Test equal passed >> game.board.getRightNeighbor(32), 32+1")


def testGetLowerRightNeighbor():
    testEqual(game.board.getLowerRightNeighbor(63), None)  # None, has no lower right neighbor, is lower right corner
    print(f"Test equal passed >> game.board.getLowerRightNeighbor(63, None")
    testEqual(game.board.getLowerRightNeighbor(21), None)  # True, has no lower right neighbor
    print(f"Test equal passed >> game.board.getLowerRightNeighbor(21), None")
    testEqual(game.board.getLowerRightNeighbor(27), 27+9)  # True, has lower right neighbor (True)
    print(f"Test equal passed >> game.board.getLowerRightNeighbor(27), 27+9")
    testEqual(game.board.getLowerRightNeighbor(26), 26+9)  # None, has lower right neighbor (False)
    print(f"Test equal passed >> game.board.getLowerRightNeighbor(26), 26+9")


def testGetLowerNeighbor():
    testEqual(game.board.getLowerNeighbor(57), None)  # None, has no lower neighbor, is first row
    print(f"Test equal passed >> game.board.getLowerNeighbor(57), None")
    testEqual(game.board.getLowerNeighbor(21), None)  # True, has no lower neighbor
    print(f"Test equal passed >> game.board.getLowerNeighbor(21), None")
    testEqual(game.board.getLowerNeighbor(19), 19+8)  # None, has lower neighbor (True)
    print(f"Test equal passed >> game.board.getLowerNeighbor(19), 19+8")
    testEqual(game.board.getLowerNeighbor(25), 25+8)  # None, has lower neighbor (False)
    print(f"Test equal passed >> game.board.getLowerNeighbor(25), 25+8")


def testGetLowerLeftNeighbor():
    testEqual(game.board.getLowerLeftNeighbor(59), None)  # None, has no lower left neighbor, is lower left corner
    print(f"Test equal passed >> game.board.getLowerLeftNeighbor(59), None")
    testEqual(game.board.getLowerLeftNeighbor(33), None)  # True, has no lower left neighbor
    print(f"Test equal passed >> game.board.getLowerLeftNeighbor(33), None")
    testEqual(game.board.getLowerLeftNeighbor(20), 20+7)  # True, has lower left neighbor (True)
    print(f"Test equal passed >> game.board.getLowerLeftNeighbor(20), 20+7")
    testEqual(game.board.getLowerLeftNeighbor(26), 26+7)  # None, has lower left neighbor (False)
    print(f"Test equal passed >> game.board.getLowerLeftNeighbor(26), 26+7")


def testGetLeftNeighbor():
    testEqual(game.board.getLeftNeighbor(8), None)  # None, has no left neighbor, is left side
    print(f"Test equal passed >> game.board.getLeftNeighbor(8), None")
    testEqual(game.board.getLeftNeighbor(27), None)  # True, has no left neighbor
    print(f"Test equal passed >> game.board.getLeftNeighbor(27), None")
    testEqual(game.board.getLeftNeighbor(28), 28-1)  # True, has left neighbor (True)
    print(f"Test equal passed >> game.board.getLeftNeighbor(28), 28-1")
    testEqual(game.board.getLeftNeighbor(36), 36-1)  # None, has left neighbor (False)
    print(f"Test equal passed >> game.board.getLeftNeighbor(36), 36-1")


def testGetUpperLeftNeighbor():
    testEqual(game.board.getUpperLeftNeighbor(0), None)  # None, has no upper left neighbor, is upper left corner
    print(f"Test equal passed >> game.board.getUpperLeftNeighbor(0), None")
    testEqual(game.board.getUpperLeftNeighbor(21), None)  # True, has no upper left neighbor
    print(f"Test equal passed >> game.board.getUpperLeftNeighbor(21), None")
    testEqual(game.board.getUpperLeftNeighbor(36), 36-9)  # True, has upper left neighbor (True)
    print(f"Test equal passed >> game.board.getUpperLeftNeighbor(36), 36-9")
    testEqual(game.board.getUpperLeftNeighbor(42), 42-9)  # None, has upper left neighbor (False)
    print(f"Test equal passed >> game.board.getUpperLeftNeighbor(42), 42-9")


def testIsPlayableByDirection():
    game.board[-3] = True
    game.board[-2] = False
    game.board[-1] = True
    testEqual(game.board._isPlayableByDirection(-4, True, 2), False)
    print(f"Test equal passed >> game.board._isPlayableByDirection(-4, True, 2), False")
    game.board[-3] = None
    game.board[-2] = None
    game.board[-1] = None

print(int("   2"))

"""
print()
testGetUpperNeighbor()
print()
testGetUpperRightNeighbor()
print()
testGetRightNeighbor()
print()
testGetLowerRightNeighbor()
print()
testGetLowerNeighbor()
print()
testGetLowerLeftNeighbor()
print()
testGetLeftNeighbor()
print()
testGetUpperLeftNeighbor()
print()
testIsPlayableByDirection()
"""