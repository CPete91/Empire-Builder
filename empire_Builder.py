import sys

import pygame

from Map_Generator import *
from Neighbors_Generator import *
from PathFinder import *

mouse_pressing = True
pygame.init()


class milepost:
    def __init__(self):
        self.cost = 1
        self.xCoord = 0
        self.yCoord = 0
        self.colors = [0,0,0,0,0,0]
        self.rivers = [0,0,0,0,0,0]
        self.neighbors = [0,0,0,0,0,0]
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

class player:
    def __init__(self):
        self.color = (0, 0, 0)
        self.testColor = self.color[0] + 1, self.color[1] + 1, self.color[2] + 1
        self.name = ""
        self.Commodities = ""
        self.money = 50
        self.playerNumber = 0

if __name__ == '__main__':

    size = width, height = 500, 500 #Define the size of the pygame screen on the window
    xWidth = 10
    yHeight = 10

    ListOfMileposts, ListOfBlankSpaces, XMilePostSpacing, YMilePostSpacing = Map_Generator(xWidth,yHeight,width, height)
    #Generate the map
    ListOfMileposts = Neighbors_Generator(ListOfMileposts,XMilePostSpacing,YMilePostSpacing)
    #Give each milepost in the map an idea of who its neighbors are for path finding and determining legal builds.

    black = 1, 1, 1
    white = 255, 255, 255
    green = 0, 255, 0
    orange = 255, 128, 0
    blue = 0, 0, 255
    purple = 255, 0, 255
    TestYellow = 255, 255, 0
    redColor = (255, 0, 0)
    oceanBlue = 0, 0, 153

    MilePostRadius = int(round(YMilePostSpacing/4))

    EmpireBuilderWindow = pygame.display.set_mode(size)
    pygame.display.set_caption('Empire Builder, but like, a shittier version.')
    EmpireBuilderWindow.fill(oceanBlue)
    PotentialPath = 0
    endingPoint = 0
    PlayerList = [player()]
    PlayerList[-1].color = black
    PlayerList[-1].testColor = TestYellow


    running = 1
    flag = 0
    correction = 1
    NumSelectedMilePosts = 0
    while running:



        for post in ListOfMileposts:


            pygame.draw.rect(EmpireBuilderWindow, white, (post.xCoord - XMilePostSpacing/2, post.yCoord - YMilePostSpacing/2, XMilePostSpacing, YMilePostSpacing))
            if post.turnRed == 0:
                pygame.draw.circle(EmpireBuilderWindow,black, (post.xCoord, post.yCoord), MilePostRadius,0)
            elif post.turnRed == 1:
                pygame.draw.circle(EmpireBuilderWindow, redColor, (post.xCoord, post.yCoord), MilePostRadius, 0)

        for post in ListOfBlankSpaces:
            pygame.draw.rect(EmpireBuilderWindow, white, (post.xCoord - XMilePostSpacing / 2, post.yCoord - YMilePostSpacing / 2, XMilePostSpacing, YMilePostSpacing))


        for post in ListOfMileposts:
            for n in range (0,6):
                if post.colors[n] != 0:

                    pygame.draw.line(EmpireBuilderWindow, post.colors[n],(post.xCoord - correction, post.yCoord - correction),(post.neighbors[n].xCoord - correction, post.neighbors[n].yCoord - correction))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pygame.mouse.get_focused() == True:
                xMouse, yMouse = pygame.mouse.get_pos()
                for post in ListOfMileposts:
                    if xMouse >= post.xCoord - MilePostRadius and xMouse <= post.xCoord + MilePostRadius and yMouse >= post.yCoord - MilePostRadius and yMouse <= post.yCoord + MilePostRadius:
                        NumSelectedMilePosts += 1

                        if NumSelectedMilePosts ==1:
                            print "Ran for first click condition"


                            for post2 in ListOfMileposts:
                                post2.turnRed = 0
                                post2.parent = 0
                                #Purge any old values. This is only useful when we're returning.
                            post.turnRed = 1
                            endingPoint = 0
                            startingPoint = post


                        elif NumSelectedMilePosts ==  2:
                            print "Ran for second click condition"
                            endingPoint = post
                            post.turnRed = 1

                            PathFinder(startingPoint, endingPoint,PlayerList[-1].testColor)



                        elif NumSelectedMilePosts == 3:
                            print "Ran for third click condition"

                            for point in ListOfMileposts:
                                point.turnRed = 0
                            #Make all of the mileposts black again.

                            if post.xCoord == endingPoint.xCoord and post.yCoord == endingPoint.yCoord:
                                NumSelectedMilePosts = 0
                                flag = 1

                            else:
                                print "Went into the else statement"
                                post.turnRed = 1
                                endingPoint = 0
                                startingPoint = post
                                NumSelectedMilePosts = 1
                                flag = 1

                            #Literally just copying and pasting the code from the condition where I've only selected
                            #one milepost. Tacked on an update in case we are selecting a new milepost so that it can
                            #purge if need be.


                            endingPoint = 0



            if event.type == pygame.MOUSEBUTTONUP:
                None
            if event.type == pygame.MOUSEMOTION:
                None
        if NumSelectedMilePosts == 0 and flag == 1:
            print "Ran through the flagged part"
            for post in ListOfMileposts:
                for n in range(0,6,1):
                    if post.colors[n] == PlayerList[-1].testColor:
                        print "I tried to change a color"
                        post.colors[n] = PlayerList[-1].color
                        print PlayerList[-1].color
                        print post.colors[n]
            print ListOfMileposts[0].colors[3]
            flag = 0


        if NumSelectedMilePosts == 1 and flag == 1:
            print "Ran through the second flagged part"
            for post in ListOfMileposts:
                for n in range (0,6):
                    if post.colors[n] == PlayerList[-1].testColor:
                        print "I tried to delete a value"
                        post.colors[n] = 0
            flag = 0


        # for neighbor in ListOfMileposts[10].neighbors:
        #     if neighbor != 0:
        #          pygame.draw.line(EmpireBuilderWindow, redColor, (ListOfMileposts[10].xCoord - correction,ListOfMileposts[10].yCoord - correction),(neighbor.xCoord - correction,neighbor.yCoord - correction),2)
        # pygame.draw.line(EmpireBuilderWindow,black,(ListOfMileposts[8].xCoord - correction,ListOfMileposts[8].yCoord - correction),(ListOfMileposts[11].xCoord - correction,ListOfMileposts[11].yCoord - correction),2)
        pygame.display.flip()