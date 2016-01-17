'''/* -*- mode: python; indent-tabs-mode: nil; tab-width: 4 -*- */'''

import pygame
import math


class Plotter(pygame.sprite.Sprite):

    ### corner is the top left corner location of the plot
    def __init__(self, cornerX, cornerY, sizeX, sizeY, surface, title='WOOOOO'):

        self.animationCap = 12
        self.surface = surface

        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()

        #self.displayedX = []
        #self.displayedY = []
        
        self.dataX = []
        self.dataY = []

        self.dataX2 = []
        self.dataY2 = []

        self.counter = 0

        self.cornerX = cornerX
        self.cornerY = cornerY
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.xmin = -0.5
        self.xmax = 10
        
        self.ymin = -0.05
        self.ymax = 1.1

        self.PTCOLOR = (  0, 200,  60)
        self.PTCOLOR2 = (255, 10,  90)

        self.animate1 = False
        self.a1index = -1
        self.animate2 = False
        self.a2index = -1

        self.lastAnimate1 = 0
        self.lastAnimate2 = 0
        self.animateWait = 20

        self.a1progress = 0
        self.a2progress = 0

        self.fontObj = pygame.font.Font("RopaSans-Regular.ttf", 24)
        self.title = title

    def getData(self, x, y):
        self.dataX = x
        self.dataY = y

    def getData2(self, x, y):
        self.dataX2 = x
        self.dataY2 = y

    def setColor(self, r, g, b):
        self.PTCOLOR = (r,g,b)

    def setColor2(self, r, g, b):
        self.PTCOLOR2 = (r,g,b)

    def alert(self, which, index):
        if self.canAnimate(which):
            if which == 1:
                self.animate1 = True
                self.a1index = index
                self.lastAnimate1 = 0
            else:
                self.animate2 = True
                self.a2index = index
                self.lastAnimate2 = 0

    def canAnimate(self, which):
        if which == 1:
            if self.animate1:
                return False
        else:
            if self.animate2: 
                return False
        #print True
        return True

    def draw(self):

        animate1 = self.animate1
        a1index = self.a1index
        animate2 = self.animate2
        a2index = self.a2index

        BLACK = (  0,   0,   0)
        WHITE = (255, 255, 255)
        BLUE =  (  0,   0, 255)
        GREEN = (  0, 255,   0)
        RED =   (255,   0,   0)

        xRange = self.xmax - self.xmin
        yRange = self.ymax - self.ymin

        prevX = 0
        prevY = 0


        xAxis = (0 - self.xmin) / float(xRange) * self.sizeX
        yAxis = (0 - self.ymin) / float(yRange) * self.sizeY

        if xAxis < 0:
            xAxis = 0
        if xAxis > self.sizeX:
            xAxis = self.sizeX 
        if yAxis < 0:
            yAxis = 0
        if yAxis > self.sizeY:
            yAxis = self.sizeY 

        screenX = self.cornerX + xAxis
        screenY = self.cornerY + (self.sizeY - yAxis)

        textSurfaceObj1 = self.fontObj.render(self.title, True, (100, 200, 170))
        textRectObj1 = textSurfaceObj1.get_rect()
        textRectObj1.center = (self.cornerX + self.sizeX / 2, self.cornerY + 5)
        self.surface.blit(textSurfaceObj1, textRectObj1)

        pygame.draw.line(self.screen, BLACK, [int(screenX), int(self.cornerY)], [int(screenX), int(self.cornerY + self.sizeY)], 1)
        pygame.draw.line(self.screen, BLACK, [int(self.cornerX), int(screenY)], [int(self.cornerX + self.sizeX), int(screenY)], 1)

        if len(self.dataX) == 0:
            return

        if self.animate1:
            last = a1index
            self.a1progress = self.a1progress + 1
        else:
            last = len(self.dataX)
            self.a1progress = 0
            self.lastAnimate1 = self.lastAnimate1 + 1

        for i in range(last):
            plotX = (self.dataX[i] - self.xmin) / float(xRange) * self.sizeX
            plotY = (self.dataY[i] - self.ymin) / float(yRange) * self.sizeY
            
            if plotX > self.sizeX or plotX < 0 or plotY > self.sizeY or plotY < 0:
                print 'bad'
            else:
                screenX = self.cornerX + plotX
                screenY = self.cornerY + (self.sizeY - plotY)

                pygame.draw.circle(self.screen, self.PTCOLOR, [int(screenX), int(screenY)], 3)

                if i != 0:
                    pygame.draw.line(self.screen, self.PTCOLOR, [int(prevX), int(prevY)], [int(screenX), int(screenY)], 3)
                
                prevX = screenX
                prevY = screenY

        if self.animate1:
            wantX = self.a1progress / float(self.animationCap) * (self.dataX[a1index] - self.dataX[a1index - 1]) + self.dataX[a1index - 1]
            wantY = self.a1progress / float(self.animationCap) * (self.dataY[a1index] - self.dataY[a1index - 1]) + self.dataY[a1index - 1]
            plotX = (wantX - self.xmin) / float(xRange) * self.sizeX
            plotY = (wantY - self.ymin) / float(yRange) * self.sizeY
            
            if plotX > self.sizeX or plotX < 0 or plotY > self.sizeY or plotY < 0:
                print 'bad'
            else:
                screenX = self.cornerX + plotX
                screenY = self.cornerY + (self.sizeY - plotY)

                pygame.draw.circle(self.screen, self.PTCOLOR, [int(screenX), int(screenY)], 3)
                pygame.draw.line(self.screen, self.PTCOLOR, [int(prevX), int(prevY)], [int(screenX), int(screenY)], 3)

            if self.a1progress > self.animationCap:
                self.animate1 = False
                self.a1progress = 0


        if self.animate2:
            last = a2index
            self.a2progress = self.a2progress + 1
        else:
            last = len(self.dataX2)
            self.a2progress = 0
            self.lastAnimate2 = self.lastAnimate2 + 1

        # print 'data2 range is' + str(last) + ' ' + str(len(self.dataX2))

        for i in range(last):
            plotX = (self.dataX2[i] - self.xmin) / float(xRange) * self.sizeX
            plotY = (self.dataY2[i] - self.ymin) / float(yRange) * self.sizeY
            
            if plotX > self.sizeX or plotX < 0 or plotY > self.sizeY or plotY < 0:
                print 'bad'
            else:
                screenX = self.cornerX + plotX
                screenY = self.cornerY + (self.sizeY - plotY)

                pygame.draw.circle(self.screen, self.PTCOLOR2, [int(screenX), int(screenY)], 3)

                if i != 0:
                    pygame.draw.line(self.screen, self.PTCOLOR2, [int(prevX), int(prevY)], [int(screenX), int(screenY)], 3)
                
                prevX = screenX
                prevY = screenY

        if self.animate2:
            wantX = self.a2progress / float(self.animationCap) * (self.dataX2[a2index] - self.dataX2[a2index - 1]) + self.dataX2[a2index - 1]
            wantY = self.a2progress / float(self.animationCap) * (self.dataY2[a2index] - self.dataY2[a2index - 1]) + self.dataY2[a2index - 1]
            plotX = (wantX - self.xmin) / float(xRange) * self.sizeX
            plotY = (wantY - self.ymin) / float(yRange) * self.sizeY
            
            if plotX > self.sizeX or plotX < 0 or plotY > self.sizeY or plotY < 0:
                print 'bad'
            else:
                screenX = self.cornerX + plotX
                screenY = self.cornerY + (self.sizeY - plotY)

                pygame.draw.circle(self.screen, self.PTCOLOR2, [int(screenX), int(screenY)], 3)
                pygame.draw.line(self.screen, self.PTCOLOR2, [int(prevX), int(prevY)], [int(screenX), int(screenY)], 3)

            if self.a2progress > self.animationCap:
                self.animate2 = False
                self.a2progress = 0
    
    def zoomFit(self):

        if len(self.dataX) == 0:
            self.xmin = -0.5
            self.xmax = 10
            #self.ymin = -2
            #self.ymax = 10
        elif len(self.dataX) == 1:
            self.xmin = self.dataX[0] - abs(self.dataX[0])
            self.xmax = self.dataX[0] + abs(self.dataX[0])
            #self.ymin = self.dataY[0] - abs(self.dataY[0])
            #self.ymax = self.dataY[0] + abs(self.dataY[0])
        else:

            listmin = min(self.dataX)
            listmax = max(self.dataX)

            listOffset = (listmax - listmin) * 0.1
            self.xmin = math.floor(listmin - listOffset)
            self.xmax = math.ceil(listmax + listOffset)

            #print '-------------------------------------------------------------'
            #print self.dataY    
'''
            listmin = min(self.dataY)
            listmax = max(self.dataY)
'''
            #print type(listmin)
            #print type(listmax)
            #print type(listOffset)

            #print listmax - listmin

'''
            listOffset = (listmax - listmin) * 0.1
            self.ymin = math.floor(listmin - listOffset)
            self.ymax = math.ceil(listmax + listOffset)
'''     


