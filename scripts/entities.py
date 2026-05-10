import pygame as pg

class PhysicsEntity:
    def __init__(self, game, entityType, pos, size, velocity=[0, 0]):
        self.game = game
        self.entityType = entityType
        self.pos = list(pos)  # list() makes a new reference to a new list
        self.size = size
        self.velocity = velocity


    def update(self):
        self.pos[0] += self.game.horizontalMovement[self.entityType][1] - self.game.horizontalMovement[self.entityType][0] + self.velocity[0]
        self.pos[1] += self.game.verticalMovement[self.entityType][1] - self.game.verticalMovement[self.entityType][0] + self.velocity[1]


    def teleport(self, pos):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
    
    def changeVelocity(self, velocity):
        self.velocity = velocity

    def setSize(self, size):
        self.size = size

    def render(self, destinationSurface):
        destinationSurface.blit(self.game.assets[self.entityType], self.pos)
