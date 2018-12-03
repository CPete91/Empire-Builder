import sys, pygame
import sys, math
from pygame.locals import *
from math import *
from Map_Generator import *
pygame.init()


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

if __name__ == '__main__':

    size = width, height = 225, 151 #Define the size of the pygame screen on the window
    xWidth = 5
    yHeight = 5

    ListOfMileposts, ListOfBlankSpaces, XMilePostSpacing, YMilePostSpacing = Map_Generator(xWidth,yHeight,width, height)

    print XMilePostSpacing
    print YMilePostSpacing

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #xMouse, yMouse = pygame.mouse.get_pos()
            print "The mouse button thing worked"
        #     for post in ListOfMileposts:
        #         if xMouse <= post.xCoord + MilePostRadius and xMouse >= post.xCoord - MilePostRadius and yMouse <= post.yCoord + MilePostRadius and yMouse >= post.yCoord - MilePostRadius:
        #             pygame.draw.circle(EmpireBuilderWindow, redColor, (post.xCoord, post.yCoord), 3*MilePostRadius, 0)
        # Jim/ Sam help request -- I can't figure out why this keeps crashing on me. It won't evaluate. Am I asking it to check too much too quickly?
    EmpireBuilderWindow.fill(oceanBlue)
    while 1:
        for post in ListOfMileposts:
            pygame.draw.rect(EmpireBuilderWindow, white, (post.xCoord - XMilePostSpacing/2, post.yCoord - YMilePostSpacing/2, XMilePostSpacing, YMilePostSpacing))
            pygame.draw.circle(EmpireBuilderWindow,black, (post.xCoord, post.yCoord), MilePostRadius,0)
        for post in ListOfBlankSpaces:
            pygame.draw.rect(EmpireBuilderWindow, white, (post.xCoord - XMilePostSpacing / 2, post.yCoord - YMilePostSpacing / 2, XMilePostSpacing, YMilePostSpacing))
        pygame.draw.line(EmpireBuilderWindow,black,(ListOfMileposts[0].xCoord,ListOfMileposts[0].yCoord),(ListOfMileposts[6].xCoord,ListOfMileposts[6].yCoord),2)
        pygame.draw.line(EmpireBuilderWindow, purple, (ListOfMileposts[1].xCoord, ListOfMileposts[1].yCoord),(ListOfMileposts[7].xCoord, ListOfMileposts[7].yCoord), 2)
        pygame.display.flip()

