import pygame as pg
import sys
from scripts.entities import PhysicsEntity, CloudEntity
from scripts.utils import loadImage
import uuid
from scripts.header import *

class Game:
    def __init__(self):        
        pg.init()
        pg.display.set_caption("Sandbox Game!")
        
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create the window
        self.clock = pg.time.Clock()
        
        self.assets = {}
        self.horizontalMovement = {}
        self.verticalMovement = {}
        self.entities = []

        self.playerId = 0
        self.player = PhysicsEntity(self, self.playerId, "player", (100, 100), (130, 146), imgPath='entities/toonLinkPixelTransparent.png', convert=False, colorKey=False)
        
        for _ in range(30):
            sizeMultiplier = uniform(1, 5)
            sizeVar = (55 * sizeMultiplier, 20 * sizeMultiplier)

            CloudEntity(self, uuid.uuid4(), "cloud", (randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)),
                        sizeVar, (randint(2, 10), 0), 'clouds/cloud_1.png'
                        )

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))  # resets screen # sky blue 

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
                        self.verticalMovement[self.playerId][0] = speed
                    elif event.key == pg.K_DOWN:
                        self.verticalMovement[self.playerId][1] = speed
                    elif event.key == pg.K_LEFT:
                        self.horizontalMovement[self.playerId][0] = speed
                    elif event.key == pg.K_RIGHT:
                        self.horizontalMovement[self.playerId][1] = speed
                elif event.type == pg.KEYUP:  # key released
                    if event.key == pg.K_UP:
                        self.verticalMovement[self.playerId][0] = 0
                    elif event.key == pg.K_DOWN:
                        self.verticalMovement[self.playerId][1] = 0
                    elif event.key == pg.K_LEFT:
                        self.horizontalMovement[self.playerId][0] = 0
                    elif event.key == pg.K_RIGHT:
                        self.horizontalMovement[self.playerId][1] = 0

            pg.display.update()  # update the display with any changes
            self.clock.tick(60)  # force loop to run at 60 fps


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
