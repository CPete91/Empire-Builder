import sys, pygame
import sys, math
from pygame.locals import *
from math import *
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

if __name__ == '__main__':

    size = width, height = 500, 500 #Define the size of the pygame screen on the window
    xWidth = 10
    yHeight = 10

    ListOfMileposts, ListOfBlankSpaces, XMilePostSpacing, YMilePostSpacing = Map_Generator(xWidth,yHeight,width, height)
    #Generate the map
    ListOfMileposts = Neighbors_Generator(ListOfMileposts,XMilePostSpacing,YMilePostSpacing)
    #Give each milepost in the map an idea of who its neighbors are for path finding and determining legal builds.

    black = 0, 0, 0
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



    running = 1
    NumSelectedMilePosts = 0
    while running:

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = 0
        #         sys.exit()
        #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pygame.mouse.get_focused() == True:
        #         xMouse, yMouse = pygame.mouse.get_pos()
        #         for post in ListOfMileposts:
        #             if xMouse >= post.xCoord - MilePostRadius and xMouse <= post.xCoord + MilePostRadius and yMouse >= post.yCoord - MilePostRadius and yMouse <= post.yCoord + MilePostRadius:
        #                 pygame.draw.circle(EmpireBuilderWindow, redColor, (post.xCoord, post.yCoord), MilePostRadius, 0)
        #                 NumSelectedMilePosts += 1
        #                 if NumSelectedMilePosts > 1:
        #                     endingPoint = post
        #                     PathFinder(startingPoint,endingPoint,ListOfMileposts)
        #                     NumSelectedMilePosts = 0
        #                 else:
        #                     startingPoint = post
        #                 print 'x coordinate is', post.xCoord
        #                 print 'y coordinate is', post.yCoord
        #     if event.type == pygame.MOUSEBUTTONUP:
        #         None
        #     if event.type == pygame.MOUSEMOTION:
        #         None

        for post in ListOfMileposts:
            pygame.draw.rect(EmpireBuilderWindow, white, (post.xCoord - XMilePostSpacing/2, post.yCoord - YMilePostSpacing/2, XMilePostSpacing, YMilePostSpacing))
            if post.turnRed == 0:
                pygame.draw.circle(EmpireBuilderWindow,black, (post.xCoord, post.yCoord), MilePostRadius,0)
            elif post.turnRed == 1:
                pygame.draw.circle(EmpireBuilderWindow, redColor, (post.xCoord, post.yCoord), MilePostRadius, 0)

        if PotentialPath != 0:
            for point in PotentialPath:
                for n in range (0,6,1):
                    if point.colors[n] != 0 and point.neighbors[n] != 0:
                        pygame.draw.line(EmpireBuilderWindow,point.colors[n],(point.xCoord,point.yCoord),(point.neighbors[n].xCoord, point.neighbors[n].yCoord))

        for post in ListOfBlankSpaces:
            pygame.draw.rect(EmpireBuilderWindow, white, (post.xCoord - XMilePostSpacing / 2, post.yCoord - YMilePostSpacing / 2, XMilePostSpacing, YMilePostSpacing))

        if PotentialPath != 0:
            for point in PotentialPath:
                for n in range(0, 6, 1):
                    if point.colors[n] != 0 and point.neighbors[n] != 0:
                        pygame.draw.line(EmpireBuilderWindow, point.colors[n], (point.xCoord, point.yCoord),(point.neighbors[n].xCoord, point.neighbors[n].yCoord))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pygame.mouse.get_focused() == True:
                xMouse, yMouse = pygame.mouse.get_pos()
                for post in ListOfMileposts:
                    if xMouse >= post.xCoord - MilePostRadius and xMouse <= post.xCoord + MilePostRadius and yMouse >= post.yCoord - MilePostRadius and yMouse <= post.yCoord + MilePostRadius:
                        pygame.draw.circle(EmpireBuilderWindow, redColor, (post.xCoord, post.yCoord),MilePostRadius, 0)
                        post.turnRed = 1
                        print "I registered that click"
                        NumSelectedMilePosts += 1
                        if NumSelectedMilePosts > 1:
                            endingPoint = post
                            PotentialPath = PathFinder(startingPoint, endingPoint)
                            print 'returned from PathFinder'
                            # NumSelectedMilePosts = 0
                        else:
                            startingPoint = post

            if event.type == pygame.MOUSEBUTTONUP:
                None
            if event.type == pygame.MOUSEMOTION:
                None

        correction = 1
        # for neighbor in ListOfMileposts[10].neighbors:
        #     if neighbor != 0:
        #          pygame.draw.line(EmpireBuilderWindow, redColor, (ListOfMileposts[10].xCoord - correction,ListOfMileposts[10].yCoord - correction),(neighbor.xCoord - correction,neighbor.yCoord - correction),2)
        # pygame.draw.line(EmpireBuilderWindow,black,(ListOfMileposts[8].xCoord - correction,ListOfMileposts[8].yCoord - correction),(ListOfMileposts[11].xCoord - correction,ListOfMileposts[11].yCoord - correction),2)
        pygame.display.flip()