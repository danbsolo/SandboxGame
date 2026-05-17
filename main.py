import pygame as pg
import sys
from scripts.entities import PhysicsEntity, PlayerEntity # BackgroundEntity
from scripts.header import *
from scripts.utils import *
from scripts.tileMap import TileMap

class Game:
    def __init__(self):        
        pg.init()
        pg.display.set_caption("Sandbox Game!")
        
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create the window
        self.container = pg.Surface((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        self.clock = pg.time.Clock()
        
        tileSize = 20
        self.assets = {
            "decor": loadImages("tiles/decor", tileSize, tileSize),
            "grass": loadImages("tiles/grass", tileSize, tileSize),
            "large_decor": loadImages("tiles/large_decor", tileSize, tileSize),
            "stone": loadImages("tiles/stone", tileSize, tileSize)
        }

        self.horizontalMovement = {}
        self.verticalMovement = {}

        self.playerId = 0
        self.playerEntity = PlayerEntity(self, self.playerId, "player", (70, 70), (8, 15), imgPath='entities/player.png', convert=False, colorKey=False)

        self.tileMap = TileMap(self, tileSize)


    def run(self):
        while True:
            self.container.fill((51, 150, 0))  # resets screen

            self.tileMap.render(self.container)

            self.playerEntity.update(self.tileMap)
            self.playerEntity.render(self.container)

            speed = 4

            #print(self.tileMap.physicsRectsSurrounding(self.playerEntity.pos))

            for event in pg.event.get():  # get user input
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:  # key pressed
                    if event.key == pg.K_LEFT:
                        self.horizontalMovement[self.playerId][0] = speed
                    elif event.key == pg.K_RIGHT:
                        self.horizontalMovement[self.playerId][1] = speed
                    elif event.key == pg.K_UP:
                        if self.playerEntity.isGrounded:
                            self.playerEntity.isUpright = not self.playerEntity.isUpright
                            self.playerEntity.img = pg.transform.flip(self.playerEntity.img, flip_x=False, flip_y=True)
                elif event.type == pg.KEYUP:  # key released
                    if event.key == pg.K_LEFT:
                        self.horizontalMovement[self.playerId][0] = 0
                    elif event.key == pg.K_RIGHT:
                        self.horizontalMovement[self.playerId][1] = 0
                    # elif event.key == pg.K_UP:
                    #   self.playerEntity.isUpright = not self.playerEntity.isUpright
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print(f"Mouse clicked: ({x}, {y})")

            self.screen.blit(pg.transform.scale(self.container, (SCREEN_WIDTH, SCREEN_HEIGHT)))
            pg.display.update()  # update the display with any changes
            self.clock.tick(60)  # force loop to run at 60 fps


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
