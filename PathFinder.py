def PathFinder(startPoint,endPoint,testColor):
    from DistFormula import DistFormula

    #Known issue: Repeated use of this function is introducting random bullshit that ruins everything. I'm going to bed
    #Right now, but I plan to fix it eventually some day.

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



    # Use A* path finding algorithem to find the best path between any two points. Return a list of all of the points
    #from start to end, with a temporary coloring to tell the user what the proposed path would be. In the final verison,
    #the user will have to confirm their selection. Still working toward that.

    openList = []
    startPoint.parent = 0
    closedList = [startPoint]



    while 1:
        lastPoint = closedList[-1]

        for n in range (0,6,1):
            #I stored everything per index in lists. I know, I know, bad practice per Jim, but it works and I didn't
            #have a better solution.
            #neighbors, colors, and rivers are each 6-item-long lists, with 0 values for anything that isn't occupied.
            #neighbors[0] corresponds to colors[0], letting me know that the path between the point and the neighbor
            #in the [0] position should be that player's color.
            thisPoint = lastPoint.neighbors[n]
            if thisPoint != 0 and lastPoint.colors[n] == 0 and thisPoint not in openList and thisPoint not in closedList:
                #Bigass check. The point has to exist (if it's zero, then there isn't a point there). It has to be a legal
                #build (colors[n] = 0 means that no one has built there), and it can't already be in the open or closed
                #list. By definition, if it's in one of those lists, we've already evaluated it with the best possible
                #path. Those last two checks aren't super necessary, but they speed things up imperceptably, so of course
                #I added them.

                thisPoint.parent = lastPoint
                dist = DistFormula(thisPoint,endPoint)
                thisPoint.cashCost = lastPoint.cashCost + thisPoint.cost + lastPoint.rivers[n]
                thisPoint.moveCost = lastPoint.moveCost + 1
                thisPoint.heuristic = thisPoint.cashCost + thisPoint.moveCost + dist + lastPoint.heuristic
                #Working to determine everything per the criteria we're looking for. Eventually this will probably
                #be able to search for the cheapest monetary cost between points A and B, or the quickest move cost.
                #For now, one move is weighted equal to $1.
                openList.append(thisPoint)

                if dist == 0:
                    closedList.append(thisPoint)
                    break
                    #Checking to see if we made it to the end point. If we did, then we don't need to evaluate anything
                    #else.
        if dist == 0:
            break
            #The first break only exits the for loop. This one gets us out of the infinite while loop.

        bestPoint = openList[0]
        for point in openList:
            if bestPoint.heuristic > point.heuristic:
                bestPoint = point

        if not openList:
            return 0

        openList.remove(bestPoint)
        closedList.append(bestPoint)
        #Once we determine the most attractive potential point, we remove it from the open list and add it to the
        #closed list. When the loop starts up again, we'll examine that point's neighbors (but NOT items already in
        #the open and closed lists)



        #If this thing runs 10,000 times, then there's no path to get there.

    finalList = [closedList[-1]]
    closedList.reverse()
    for point in closedList:
        lastPoint = finalList[-1]
        if lastPoint.parent.xCoord == point.xCoord and lastPoint.parent.yCoord == point.yCoord:
            for n in range (0,6,1):
                if lastPoint.neighbors[n] != 0 and lastPoint.neighbors[n].xCoord == point.xCoord and lastPoint.neighbors[n].yCoord == point.yCoord and lastPoint.neighbors[n].xCoord == lastPoint.parent.xCoord and lastPoint.neighbors[n].yCoord == lastPoint.parent.yCoord:
                    lastPoint.colors[n] = testColor
                    if n >= 3:
                        point.colors[n-3] = testColor
                    else:
                        point.colors[n+3] = testColor
            finalList.append(point)
    finalList.reverse()
    for point in closedList:
        point.parent = 0
    print finalList[0].cashCost
    return

