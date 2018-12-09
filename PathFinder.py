def PathFinder(startPoint,endPoint):
    from DistFormula import *

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

    openList = []
    startPoint.parent = 0
    closedList = [startPoint]
    orange = 1,1,1


    for n in range (0,6,1):
        if startPoint.neighbors[n] != 0 and startPoint.neighbors[n].xCoord == endPoint.xCoord and startPoint.neighbors[n].yCoord == endPoint.yCoord:
            startPoint.colors[n] = orange
            if n >= 3:
                endPoint.colors[n-3] = orange
            else:
                endPoint.colors[n+3] = orange
            closedList.append(endPoint)
            return closedList

    while 1:
        lastPoint = closedList[-1]
        for n in range (0,6,1):
            thisPoint = lastPoint.neighbors[n]
            if thisPoint != 0 and lastPoint.colors[n] == 0 and thisPoint not in openList and thisPoint not in closedList:
                thisPoint.parent = lastPoint
                dist = DistFormula(thisPoint,endPoint)
                if dist == 0:
                    closedList.append(thisPoint)
                    break
                thisPoint.cashCost = lastPoint.cashCost + thisPoint.cost + lastPoint.rivers[n]
                thisPoint.moveCost = lastPoint.moveCost + 1
                thisPoint.heuristic = thisPoint.cashCost + thisPoint.moveCost + dist
                openList.append(thisPoint)
        if dist == 0:
            break

        bestPoint = openList[0]
        for point in openList:
            if bestPoint.heuristic > point.heuristic:
                bestPoint = point

        openList.remove(bestPoint)
        closedList.append(bestPoint)
        if not openList:
            return 0
        #

    finalList = [closedList[-1]]
    closedList.reverse()
    for point in closedList:
        lastPoint = finalList[-1]
        if lastPoint.parent.xCoord == point.xCoord and lastPoint.parent.yCoord == point.yCoord:
            for n in range (0,6,1):
                if lastPoint.neighbors[n] != 0 and lastPoint.neighbors[n].xCoord == point.xCoord and lastPoint.neighbors[n].yCoord == point.yCoord:
                    lastPoint.colors[n] = orange
                    if n >= 3:
                        point.colors[n-3] = orange
                    else:
                        point.colors[n+3] = orange
            finalList.append(point)
    finalList.reverse()
    return finalList

