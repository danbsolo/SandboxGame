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
        self.collisions = {"up": False, "down": False, "left": False, "right": False}

        # Load image if applicable
        if imgPath:
            self.img = loadImage(imgPath, convert, colorKey, self.size)
            self.game.assets[self.id] = self.img
        
        # Add to game collections
        self.game.horizontalMovement[self.id] = [0, 0]
        self.game.verticalMovement[self.id] = [0, 0]


    def update(self):
        self.velocity[1] = min(5, self.velocity[1] + 0.1)  # terminal velocity defines max speed

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
    def __init__(self, game, id, entityType, pos, size=None, velocity=[0, 0], imgPath=None, convert=True, colorKey=(0, 0, 0)):
        PhysicsEntity.__init__(self, game, id, entityType, pos, size, velocity, imgPath, convert, colorKey)
        self.isGrounded = None
        self.isUpright = True

    def getCollisionRect(self):
        return pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tileMap):
        self.collisions = {"up": False, "down": False, "left": False, "right": False}

        frameMovement = (self.game.horizontalMovement[self.id][1] - self.game.horizontalMovement[self.id][0] + self.velocity[0],
                         self.game.verticalMovement[self.id][1] - self.game.verticalMovement[self.id][0] + self.velocity[1]) 

        self.pos[0] += frameMovement[0]
        entityRect = self.getCollisionRect()
        for physicsRect in tileMap.physicsRectsSurrounding(self.pos):
            if entityRect.colliderect(physicsRect):
                if frameMovement[0] > 0: # if moving right and colliding with a tile
                    entityRect.right = physicsRect.left
                    self.collisions["right"] = True
                if frameMovement[0] < 0:
                    entityRect.left = physicsRect.right
                    self.collisions["left"] = True
                self.pos[0] = entityRect.x
                
        self.pos[1] += frameMovement[1]
        entityRect = self.getCollisionRect()  
        for physicsRect in tileMap.physicsRectsSurrounding(self.pos):
            if entityRect.colliderect(physicsRect):
                if frameMovement[1] > 0:
                    entityRect.bottom = physicsRect.top
                    self.collisions["down"] = True
                if frameMovement[1] < 0:
                    entityRect.top = physicsRect.bottom
                    self.collisions["up"] = True
                self.pos[1] = entityRect.y

        if self.isUpright:
            self.velocity[1] = 5  # terminal velocity defines max speed
        else:
            self.velocity[1] = -5

        if self.collisions["up"] or self.collisions["down"]:
            self.isGrounded = True
            #self.velocity[1] = 0
        else:
            self.isGrounded = False

        
# class BackgroundEntity(PhysicsEntity):
#     def __init__(self, game, id, entityType, pos, size, velocity=[0, 0], imgPath=None, convert=True, colorKey=(0, 0, 0), minPosY=0, maxPosY=SCREEN_HEIGHT):
#         PhysicsEntity.__init__(self, game, id, entityType, pos, size, velocity, imgPath, convert, colorKey)

