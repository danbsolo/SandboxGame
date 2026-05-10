import pygame as pg
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import loadImage
from random import randint, uniform
import uuid

class Game:
    def __init__(self):        
        pg.init()
        pg.display.set_caption("Sandbox Game!")
        
        self.screenWidth = 640
        self.screenHeight = 480
        
        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight))  # create the window
        self.clock = pg.time.Clock()
        
        self.player = PhysicsEntity(self, "player", (100, 100), None)
        
        self.cloudEntities = []
        for _ in range(30):
            self.cloudEntities.append(
                PhysicsEntity(self, 
                              f"cloud{uuid.uuid4()}", 
                              (randint(0, self.screenWidth), randint(0, self.screenHeight)),
                               None,
                               (randint(2, 10), 0)
                               )
                )

        self.entities = [self.player]
        self.entities.extend(self.cloudEntities)

        self.assets = {}

        self.horizontalMovement = {
            "player": [0, 0]
        }

        self.verticalMovement = {
            "player": [0, 0]
        }

        for cloudEntity in self.cloudEntities:
            sizeMultiplier = uniform(1, 5)
            sizeVar = (55 * sizeMultiplier, 20 * sizeMultiplier)
            cloudEntity.setSize(sizeVar)

            self.assets[cloudEntity.entityType] = loadImage('clouds/cloud_1.png', size=sizeVar)
            self.horizontalMovement[cloudEntity.entityType] = [0, 0]
            self.verticalMovement[cloudEntity.entityType] = [0, 0]

        self.assets["player"] = loadImage('entities/toonLinkPixelTransparent.png', False, None, (130, 146))

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))  # resets screen # sky blue 

            for cloudEntity in self.cloudEntities:
                if cloudEntity.pos[0] >= self.screenWidth:
                    cloudEntity.teleport((0 - cloudEntity.size[0], randint(0, self.screenHeight)))
                    cloudEntity.changeVelocity((randint(2, 10), 0))

            for entity in self.entities:
                entity.update()
                entity.render(self.screen)

            speed = 5

            for event in pg.event.get():  # get user input
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:  # key pressed
                    if event.key == pg.K_UP:
                        self.verticalMovement["player"][0] = speed
                    elif event.key == pg.K_DOWN:
                        self.verticalMovement["player"][1] = speed
                    elif event.key == pg.K_LEFT:
                        self.horizontalMovement["player"][0] = speed
                    elif event.key == pg.K_RIGHT:
                        self.horizontalMovement["player"][1] = speed
                elif event.type == pg.KEYUP:  # key released
                    if event.key == pg.K_UP:
                        self.verticalMovement["player"][0] = 0
                    elif event.key == pg.K_DOWN:
                        self.verticalMovement["player"][1] = 0
                    elif event.key == pg.K_LEFT:
                        self.horizontalMovement["player"][0] = 0
                    elif event.key == pg.K_RIGHT:
                        self.horizontalMovement["player"][1] = 0

            pg.display.update()  # update the display with any changes
            self.clock.tick(60)  # force loop to run at 60 fps


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
