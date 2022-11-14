class SquareGraph:
    def __init__(self):
        self.upperRightCornerNode = UpperRightCornerNode(None)
        self.lowerRightCornerNode = LowerRightCornerNode(None)
        self.lowerLeftCornerNode = LowerLeftCornerNode(None)
        self.upperLeftCornerNode = UpperLeftCornerNode(None)
        self.upperEdgeNodes = [UpperEdgeNode(None), UpperEdgeNode(None), UpperEdgeNode(None), UpperEdgeNode(None), UpperEdgeNode(None), UpperEdgeNode(None)]
        self.rightEdgeNodes = [RightEdgeNode(None), RightEdgeNode(None), RightEdgeNode(None), RightEdgeNode(None), RightEdgeNode(None), RightEdgeNode(None)]
        self.lowerEdgeNodes = [LowerEdgeNode(None), LowerEdgeNode(None), LowerEdgeNode(None), LowerEdgeNode(None), LowerEdgeNode(None), LowerEdgeNode(None)]
        self.leftEdgeNodes = [LowerEdgeNode(None), LowerEdgeNode(None), LowerEdgeNode(None), LowerEdgeNode(None), LowerEdgeNode(None), LowerEdgeNode(None)]
        self.centerNodes = [CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None),
                            CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None),
                            CenterNode(None), CenterNode(None), CenterNode(True), CenterNode(False), CenterNode(None), CenterNode(None),
                            CenterNode(None), CenterNode(None), CenterNode(False), CenterNode(True), CenterNode(None), CenterNode(None),
                            CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None),
                            CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None), CenterNode(None)]



class Node:
    def __init__(self, value: None or bool):
        self.value = value


class CenterNode(Node):
    """
    ○ ○ ○
    ○ ◉ ○
    ○ ○ ○
    """

    def __init__(self, value, upperNeighbor, upperRightNeighbor, rightNeighbor, lowerRightNeighbor, lowerNeighbor,
                 lowerLeftNeighbor, leftNeighbor, upperLeftNeighbor):
        super().__init__(value)
        self.upperNeighbor = upperNeighbor
        self.upperRightNeighbor = upperRightNeighbor
        self.rightNeighbor = rightNeighbor
        self.lowerRightNeighbor = lowerRightNeighbor
        self.lowerNeighbor = lowerNeighbor
        self.lowerLeftNeighbor = lowerLeftNeighbor
        self.leftNeighbor = leftNeighbor
        self.upperLeftNeighbor = upperLeftNeighbor


class UpperEdgeNode(Node):
    """
    ○ ◉ ○
    ○ ○ ○
    ○ ○ ○
    """

    def __init__(self, value, rightNeighbor, lowerRightNeighbor, lowerNeighbor,
                 lowerLeftNeighbor, leftNeighbor):
        super().__init__(value)
        self.rightNeighbor = rightNeighbor
        self.lowerRightNeighbor = lowerRightNeighbor
        self.lowerNeighbor = lowerNeighbor
        self.lowerLeftNeighbor = lowerLeftNeighbor
        self.leftNeighbor = leftNeighbor


class RightEdgeNode(Node):
    """
    ○ ○ ○
    ○ ○ ◉
    ○ ○ ○
    """

    def __init__(self, value, upperNeighbor, lowerNeighbor,
                 lowerLeftNeighbor, leftNeighbor, upperLeftNeighbor):
        super().__init__(value)
        self.upperNeighbor = upperNeighbor
        self.lowerNeighbor = lowerNeighbor
        self.lowerLeftNeighbor = lowerLeftNeighbor
        self.leftNeighbor = leftNeighbor
        self.upperLeftNeighbor = upperLeftNeighbor


class LowerEdgeNode(Node):
    """
    ○ ○ ○
    ○ ○ ○
    ○ ◉ ○
    """

    def __init__(self, value, upperNeighbor, upperRightNeighbor, rightNeighbor, leftNeighbor, upperLeftNeighbor):
        super().__init__(value)
        self.upperNeighbor = upperNeighbor
        self.upperRightNeighbor = upperRightNeighbor
        self.rightNeighbor = rightNeighbor
        self.leftNeighbor = leftNeighbor
        self.upperLeftNeighbor = upperLeftNeighbor


class LeftEdgeNode(Node):
    """
    ○ ○ ○
    ◉ ○ ○
    ○ ○ ○
    """

    def __init__(self, value, upperNeighbor, upperRightNeighbor, rightNeighbor, lowerRightNeighbor, lowerNeighbor):
        super().__init__(value)
        self.upperNeighbor = upperNeighbor
        self.upperRightNeighbor = upperRightNeighbor
        self.rightNeighbor = rightNeighbor
        self.lowerRightNeighbor = lowerRightNeighbor
        self.lowerNeighbor = lowerNeighbor


class UpperRightCornerNode(Node):
    """
    ○ ○ ◉
    ○ ○ ○
    ○ ○ ○
    """

    def __init__(self, value, lowerNeighbor,
                 lowerLeftNeighbor, leftNeighbor):
        super().__init__(value)
        self.lowerNeighbor = lowerNeighbor
        self.lowerLeftNeighbor = lowerLeftNeighbor
        self.leftNeighbor = leftNeighbor


class LowerRightCornerNode(Node):
    """
    ○ ○ ○
    ○ ○ ○
    ○ ○ ◉
    """

    def __init__(self, value, upperNeighbor, leftNeighbor, upperLeftNeighbor):
        super().__init__(value)
        self.upperNeighbor = upperNeighbor
        self.leftNeighbor = leftNeighbor
        self.upperLeftNeighbor = upperLeftNeighbor


class LowerLeftCornerNode(Node):
    """
    ○ ○ ○
    ○ ○ ○
    ◉ ○ ○
    """

    def __init__(self, value, upperNeighbor, upperRightNeighbor, rightNeighbor):
        super().__init__(value)
        self.upperNeighbor = upperNeighbor
        self.upperRightNeighbor = upperRightNeighbor
        self.rightNeighbor = rightNeighbor


class UpperLeftCornerNode(Node):
    """
    ◉ ○ ○
    ○ ○ ○
    ○ ○ ○
    """

    def __init__(self, value, rightNeighbor, lowerRightNeighbor, lowerNeighbor):
        super().__init__(value)
        self.rightNeighbor = rightNeighbor
        self.lowerRightNeighbor = lowerRightNeighbor
        self.lowerNeighbor = lowerNeighbor
