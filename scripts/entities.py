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

    def getCollisionRect(self):
        return pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        frame_movement = (self.game.horizontalMovement[self.id][1] - self.game.horizontalMovement[self.id][0] + self.velocity[0],
                         self.game.verticalMovement[self.id][1] - self.game.verticalMovement[self.id][0] + self.velocity[1]) 

        
        self.pos[0] += frame_movement[0]
        entity_rect = self.getCollisionRect()
        for rect in tilemap.physicsRectsSurrounding(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
        
        self.pos[1] += frame_movement[1]
        entity_rect = self.getCollisionRect()
        for rect in tilemap.physicsRectsSurrounding(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0




# class BackgroundEntity(PhysicsEntity):
#     def __init__(self, game, id, entityType, pos, size, velocity=[0, 0], imgPath=None, convert=True, colorKey=(0, 0, 0), minPosY=0, maxPosY=SCREEN_HEIGHT):
#         PhysicsEntity.__init__(self, game, id, entityType, pos, size, velocity, imgPath, convert, colorKey)

