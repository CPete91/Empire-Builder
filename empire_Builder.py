import sys, math
from math import *

import pygame

from Map_Generator import *
from Neighbors_Generator import *
from PathFinder import *

mouse_pressing = True
pygame.init()


# Hi
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
    zoomFactor = 0
    zoomIncrement = 0.05


    running = 1
    flag = 0
    correction = 1
    NumSelectedMilePosts = 0
    while running:



        for post in ListOfMileposts:


            pygame.draw.rect(EmpireBuilderWindow, white, (math.floor((post.xCoord - XMilePostSpacing/2)*(1+zoomFactor)), math.floor((post.yCoord - YMilePostSpacing/2)*(1+zoomFactor)), math.ceil((1 + zoomFactor) * XMilePostSpacing), math.ceil((1 + zoomFactor) *YMilePostSpacing)))
            if post.turnRed == 0:
                pygame.draw.circle(EmpireBuilderWindow,black, (int(post.xCoord * (1+ zoomFactor)), int(post.yCoord * (1 + zoomFactor))), int(MilePostRadius * (1 + zoomFactor)),0)
            elif post.turnRed == 1:
                pygame.draw.circle(EmpireBuilderWindow, redColor, (int(post.xCoord * (1+ zoomFactor)), int(post.yCoord * (1 + zoomFactor))), int(MilePostRadius * (1 + zoomFactor)),0)

        for post in ListOfBlankSpaces:
            pygame.draw.rect(EmpireBuilderWindow, white, (math.floor((post.xCoord - XMilePostSpacing/2)*(1+zoomFactor)), math.floor((post.yCoord - YMilePostSpacing/2)*(1+zoomFactor)), math.ceil((1 + zoomFactor) * XMilePostSpacing), math.ceil((1 + zoomFactor) *YMilePostSpacing)))

        for post in ListOfMileposts:
            for n in range (0,6):
                if post.colors[n] != 0:

                    pygame.draw.line(EmpireBuilderWindow, post.colors[n],int(((post.xCoord - correction)*(1 + zoomFactor)), int((post.yCoord - correction)*(1 + zoomFactor))),int(((post.neighbors[n].xCoord - correction)*(1 + zoomFactor)), int((post.neighbors[n].yCoord - correction))*(1 + zoomFactor)))


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
                            for post2 in ListOfMileposts:
                                post2.turnRed = 0
                                post2.parent = 0
                                #Purge any old values. This is only useful when we're returning.
                            post.turnRed = 1
                            endingPoint = 0
                            startingPoint = post


                        elif NumSelectedMilePosts ==  2:
                            endingPoint = post
                            post.turnRed = 1

                            PathFinder(startingPoint, endingPoint,PlayerList[-1].testColor)
                            print "This build will cost", endingPoint.cashCost, "million dollars."
                            print "Building at 20 million dollars/turn, this will take", math.ceil(endingPoint.cashCost/20.0), "turns to build."
                            print "This build will take", endingPoint.moveCost, "moves to complete."
                            print "That translates to", math.ceil(endingPoint.moveCost/8.0), "turns of moving"




                        elif NumSelectedMilePosts == 3:

                            for point in ListOfMileposts:
                                point.turnRed = 0
                                point.cashCost = 0
                                point.moveCost = 0
                                point.heuristic = 0
                            #Make all of the mileposts revert to their old states for pathfinder again.

                            if post.xCoord == endingPoint.xCoord and post.yCoord == endingPoint.yCoord:
                                NumSelectedMilePosts = 0
                                flag = 1

                            else:
                                post.turnRed = 1
                                endingPoint = 0
                                startingPoint = post
                                NumSelectedMilePosts = 1
                                flag = 1
                            endingPoint = 0
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4 and zoomFactor < 1:
                for post in ListOfMileposts:
                    pygame.draw.rect(EmpireBuilderWindow, oceanBlue, (
                    math.floor((post.xCoord - XMilePostSpacing / 2) * (1 + zoomFactor)),
                    math.floor((post.yCoord - YMilePostSpacing / 2) * (1 + zoomFactor)),
                    math.ceil((1 + zoomFactor) * XMilePostSpacing), math.ceil((1 + zoomFactor) * YMilePostSpacing)))

                for post in ListOfBlankSpaces:
                    pygame.draw.rect(EmpireBuilderWindow, oceanBlue, (
                    math.floor((post.xCoord - XMilePostSpacing / 2) * (1 + zoomFactor)),
                    math.floor((post.yCoord - YMilePostSpacing / 2) * (1 + zoomFactor)),
                    math.ceil((1 + zoomFactor) * XMilePostSpacing), math.ceil((1 + zoomFactor) * YMilePostSpacing)))

                zoomFactor += zoomIncrement
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5 and zoomFactor > -1:
                for post in ListOfMileposts:
                    pygame.draw.rect(EmpireBuilderWindow, oceanBlue, ((
                        int((post.xCoord - XMilePostSpacing / 2) * (1 + zoomFactor)),
                        int((post.yCoord - YMilePostSpacing / 2) * (1 + zoomFactor))),
                    (int((1 + zoomFactor) * XMilePostSpacing), int((1 + zoomFactor) * YMilePostSpacing))))

                for post in ListOfBlankSpaces:
                    pygame.draw.rect(EmpireBuilderWindow, oceanBlue,(int((post.xCoord - XMilePostSpacing / 2) * (1 + zoomFactor)),int((post.yCoord - YMilePostSpacing / 2) * (1 + zoomFactor)),int((1 + zoomFactor) * XMilePostSpacing),int((1 + zoomFactor) * YMilePostSpacing)))


                zoomFactor -= zoomIncrement



            if event.type == pygame.MOUSEBUTTONUP:
                None
            if event.type == pygame.MOUSEMOTION:
                None
        if NumSelectedMilePosts == 0 and flag == 1:
            for post in ListOfMileposts:
                for n in range(0,6,1):
                    if post.colors[n] == PlayerList[-1].testColor:
                        post.colors[n] = PlayerList[-1].color
            flag = 0


        if NumSelectedMilePosts == 1 and flag == 1:
            for post in ListOfMileposts:
                for n in range (0,6):
                    if post.colors[n] == PlayerList[-1].testColor:
                        post.colors[n] = 0
            flag = 0

        pygame.display.flip()