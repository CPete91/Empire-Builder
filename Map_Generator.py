def Map_Generator(x_range,y_range,window_width,window_height):
    class milepost:
        def __init__(self):
            self.cost = 1
            self.xCoord = 0
            self.yCoord = 0
            self.TrackUp = ""
            self.TrackUpAndRight = ""
            self.TrackDownAndRight = ""
            self.neighbors = []
            self.isReal = 1

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







    ListOfMileposts = []
    ListOfBlankSpaces = []
    ListOfMilepostsIndexDummyVariable =0
    xOffset = 0 #xOffset is making sure that the lines alternate their starting points. If I didn't have an offset,
    # #I'd have a square grid instead of a hex grid. The offset alternates between 0 and 1 to tell whether to

    # if window_width<window_height:
    #     XMilePostSpacing =(window_width-40)/(17*2)
    #     YMilePostSpacing = XMilePostSpacing/2
    # else:
    #     YMilePostSpacing = (window_height-40)/17
    #     XMilePostSpacing = YMilePostSpacing * 2
    XMilePostSpacing = 17*2
    YMilePostSpacing = 17
    # Mile post spacing is kinda weird. Hexagons are, essentially, 6 equilateral triangles at once. When they're bisected
    # by the coordinate plane, the math works out that the x coordinates need to be 2 square roots of 3 apart (1.73*2),
    # and the y coordinates need to be 1 square root of 3 apart. I multiplied that distance by 10 to avoid roundoff error.

    boarder_width = int((window_width - (XMilePostSpacing*x_range))/2)
    boarder_height = int((window_height - (YMilePostSpacing*y_range))/2 + YMilePostSpacing/2)
    print ("The boarder width is ",(boarder_width))
    print ("The boarder height is ", (boarder_height))

    for y in range (0,y_range):
        if xOffset == 0:
            xOffset = 1
        else:
            xOffset = 0
        for x in range(0,x_range,2):
            ListOfMileposts.append(milepost())
            ListOfBlankSpaces.append(milepost())
            if xOffset ==0:
                ListOfMileposts[ListOfMilepostsIndexDummyVariable].xCoord = boarder_width + x*XMilePostSpacing
                ListOfBlankSpaces[ListOfMilepostsIndexDummyVariable].xCoord = boarder_width + (x+1)*XMilePostSpacing
            else:
                ListOfMileposts[ListOfMilepostsIndexDummyVariable].xCoord = boarder_width + (x + 1)*XMilePostSpacing
                ListOfBlankSpaces[ListOfMilepostsIndexDummyVariable].xCoord = boarder_width + (x) * XMilePostSpacing
            ListOfMileposts[ListOfMilepostsIndexDummyVariable].yCoord = boarder_height + y*YMilePostSpacing
            ListOfBlankSpaces[ListOfMilepostsIndexDummyVariable].yCoord = boarder_height + y*YMilePostSpacing
            ListOfMilepostsIndexDummyVariable += 1

    return (ListOfMileposts,ListOfBlankSpaces, XMilePostSpacing, YMilePostSpacing)