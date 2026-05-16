import pygame as pg
from scripts.utils import loadImage
from scripts.header import *


class PhysicsEntity:
    def __init__(self, game, id, entityType, pos, size, velocity=[0, 0], imgPath=None, convert=True, colorKey=(0, 0, 0)):
        self.game = game
        self.id = id
        self.entityType = entityType
        self.pos = list(pos)  # list() makes a new reference to a new list
        self.size = size
        self.velocity = velocity

        # Load image if applicable
        if imgPath:
            self.img = loadImage(imgPath, convert, colorKey, self.size)
            self.game.assets[self.id] = self.img
        
        # Add to game collections
        self.game.horizontalMovement[self.id] = [0, 0]
        self.game.verticalMovement[self.id] = [0, 0]
        
        self.game.entities.append(self)

    def update(self):
        self.pos[0] += self.game.horizontalMovement[self.id][1] - self.game.horizontalMovement[self.id][0] + self.velocity[0]
        self.pos[1] += self.game.verticalMovement[self.id][1] - self.game.verticalMovement[self.id][0] + self.velocity[1]

    def teleport(self, pos):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]

    def setVelocity(self, velocity):
        self.velocity = velocity

    def setSize(self, size):
        self.size = size

    def render(self, destinationSurface):
        destinationSurface.blit(self.img, self.pos)


class PlayerEntity(PhysicsEntity):
    def __init__(self, game, id, entityType, pos, size, velocity=[0, 0], imgPath=None, convert=True, colorKey=(0, 0, 0)):
        PhysicsEntity.__init__(self, game, id, entityType, pos, size, velocity, imgPath, convert, colorKey)


# class BackgroundEntity(PhysicsEntity):
#     def __init__(self, game, id, entityType, pos, size, velocity=[0, 0], imgPath=None, convert=True, colorKey=(0, 0, 0), minPosY=0, maxPosY=SCREEN_HEIGHT):
#         PhysicsEntity.__init__(self, game, id, entityType, pos, size, velocity, imgPath, convert, colorKey)

