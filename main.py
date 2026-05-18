import pygame as pg
import sys
from scripts.entities import PhysicsEntity, PlayerEntity # BackgroundEntity
from scripts.header import *
from scripts.utils import *
from scripts.tileMap import TileMap

class Game:
    def __init__(self):        
        pg.init()
        pg.display.set_caption("UUUUU")
        
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create the window
        self.container = pg.Surface((SCREEN_WIDTH/CONTAINER_DIVIDER, SCREEN_HEIGHT/CONTAINER_DIVIDER))

        self.clock = pg.time.Clock()
        
        self.assets = {
            #"decor": loadImages("tiles/decor", TILE_SIZE, TILE_SIZE),
            "grass": loadImages("tiles/grass", TILE_SIZE, TILE_SIZE),
            #"large_decor": loadImages("tiles/large_decor", TILE_SIZE, TILE_SIZE),
            "stone": loadImages("tiles/stone", TILE_SIZE, TILE_SIZE),
            "spikes": loadImages("tiles/spikes", TILE_SIZE, TILE_SIZE),
            "victory": loadImages("tiles/victory", TILE_SIZE, TILE_SIZE)
        }

        self.victoryAchieved = False

        self.horizontalMovement = {}
        self.verticalMovement = {}

        self.playerId = 0
        self.playerEntity = PlayerEntity(self, self.playerId, "player", (60/CONTAINER_DIVIDER, 480/CONTAINER_DIVIDER), (8, 15), imgPath='entities/player.png', convert=False, colorKey=False)

        self.tileMap = TileMap(self, 4)


    def run(self):
        while True:
            self.container.fill((14, 140, 160))  # resets screen

            self.tileMap.render(self.container)

            self.playerEntity.update(self.tileMap)
            self.playerEntity.render(self.container)

            speed = 4

            if self.victoryAchieved:
                text_surface = pg.font.SysFont('arialrounded', 50, bold=True).render('GGs!', True, (0, 0, 0))
                self.container.blit(text_surface, (1154 / CONTAINER_DIVIDER, 644 / CONTAINER_DIVIDER))

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
                            self.playerEntity.flipGravity()
                    elif event.key == pg.K_SPACE:
                        self.playerEntity.resetPosition()
                elif event.type == pg.KEYUP:  # key released
                    if event.key == pg.K_LEFT:
                        self.horizontalMovement[self.playerId][0] = 0
                    elif event.key == pg.K_RIGHT:
                        self.horizontalMovement[self.playerId][1] = 0
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print(f"Mouse clicked: ({x}, {y}) -> ({x // CONTAINER_DIVIDER // TILE_SIZE}, {y // CONTAINER_DIVIDER // TILE_SIZE})")

            self.screen.blit(pg.transform.scale(self.container, (SCREEN_WIDTH, SCREEN_HEIGHT)))
            pg.display.update()  # update the display with any changes
            self.clock.tick(60)  # force loop to run at 60 fps


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
