def Neighbors_Generator(ListOfMileposts,xMilePostSpacing,yMilePostSpacing):
    class milepost:
        def __init__(self):
            self.cost = 1
            self.xCoord = 0
            self.yCoord = 0
            self.TrackUp = ""
            self.TrackUpAndRight = ""
            self.TrackDownAndRight = ""
            self.riverUp = 0
            self.riverUpAndRight = 0
            self.riverDownAndRight = 0
            self.neighbors = [0,0,0,0,0,0]
            self.isReal = 1
            self.cumulativeCost = 0
            self.cashCost = 0
            self.movecost = 0
            self.turnRed = 0

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

    #Neighbors_Generator takes in a list of all of the mileposts on the board and enters the neighbors into a 1 x 6
    # list. The list is set up to go from the neighbor directly above a milepost around, clockwise. If a neighbor does
    #not exist in a direction, then the neighbor will have a value of 0. Otherwise, it will be a milepost.

    for post in ListOfMileposts:
        for potentialNeighbor in ListOfMileposts:
            x1 = post.xCoord
            y1 = post.yCoord
            x2 = potentialNeighbor.xCoord
            y2 = potentialNeighbor.yCoord
            if x1 == x2 and y1 + 2*yMilePostSpacing == y2:
                post.neighbors[0] = potentialNeighbor
                #Neighbor is directly above
            if x1 + xMilePostSpacing == x2 and y1 + yMilePostSpacing == y2:
                post.neighbors[1] = potentialNeighbor
                #Neighbor is above and diaganol to the right
            if x1 + xMilePostSpacing == x2 and y1 - yMilePostSpacing == y2:
                post.neighbors[2] = potentialNeighbor
                #Neighbor is below and diaganol to the right
            if x1 == x2 and y1 - 2*yMilePostSpacing == y2:
                post.neighbors[3] = potentialNeighbor
                #Neighbor is directly below
            if x1 - xMilePostSpacing == x2 and y1 - yMilePostSpacing == y2:
                post.neighbors[4] = potentialNeighbor
                #Neighbor is below and to the left
            if x1 - xMilePostSpacing == x2 and y1 + yMilePostSpacing == y2:
                post.neighbors[5] = potentialNeighbor
                #Neighbor is above and to the left


    return ListOfMileposts