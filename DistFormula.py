def DistFormula(start, end):
    import sys,math
    from math import *

    class milepost:
        def __init__(self):
            self.cost = 1
            self.xCoord = 0
            self.yCoord = 0
            self.colors = [0, 0, 0, 0, 0, 0]
            self.rivers = [0, 0, 0, 0, 0, 0]
            self.neighbors = [0, 0, 0, 0, 0, 0]
            self.isReal = 1
            self.cumulativeCost = 0
            self.cashCost = 0
            self.moveCost = 0
            self.turnRed = 0
            self.parent = 0
            self.heuristic = 1000000000000000

    class mountain(milepost):
        def __init__(self):
            self.cost = 2

    class smallCity(milepost):
        def __init__(self):
            self.cost = 3
            self.name = ""
            self.Commodities = ""
            self.MaxPlayers = 2
            self.CurrentPlayers = 0

    class mediumCity(milepost):
        def __init__(self):
            self.cost = 3
            self.name = ""
            self.Commodities = ""
            self.MaxPlayers = 3
            self.CurrentPlayers = 0

    class majorCity(milepost):
        def __init__(self):
            self.cost = 5
            self.name = ""
            self.Commodities = ""
            self.MaxPlayers = 200
            self.CurrentPlayers = 0

    x1 = start.xCoord
    y1 = start.yCoord
    x2 = end.xCoord
    y2 = end.yCoord

    dist = math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist