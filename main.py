import pygame as pg
import sys
from scripts.entities import PhysicsEntity, PlayerEntity, BackgroundEntity
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
        self.playerEntity = PlayerEntity(self, self.playerId, "player", (SCREEN_WIDTH-200, SCREEN_HEIGHT-200), (130, 146), imgPath='entities/toonLinkPixelTransparent.png', convert=False, colorKey=False)
        
        treeOptions = {
            "tiles/large_decor/2.png": (33, 44)
        }
        for _ in range(50):
            treePath = choice(list(treeOptions.keys()))
            sizeMultiplier = uniform(1, 5)
            sizeVar = (treeOptions[treePath][0] * sizeMultiplier, treeOptions[treePath][1] * sizeMultiplier)

            BackgroundEntity(self, uuid.uuid4(), "movingBackground", (randint(0, SCREEN_WIDTH), randint(250, SCREEN_HEIGHT)),
                        sizeVar, (5, 0), treePath,
                        minPosY=250, maxPosY=SCREEN_HEIGHT
                        )
        cloudOptions = {
            "clouds/cloud_1.png": (55, 20),
            "clouds/cloud_2.png": (39, 14)
        }
        for _ in range (10):
            cloudPath = choice(list(cloudOptions.keys()))
            sizeMultiplier = uniform(1, 3)
            sizeVar = (cloudOptions[cloudPath][0] * sizeMultiplier, cloudOptions[cloudPath][1] * sizeMultiplier)

            BackgroundEntity(self, uuid.uuid4(), "movingBackground", (randint(0, SCREEN_WIDTH), randint(0, 200)),
                        sizeVar, (randint(1, 5), 0), cloudPath,
                        minPosY=0, maxPosY=200
                        )

    def run(self):
        while True:
            self.screen.fill((51, 150, 0))  # resets screen # sky blue 

            pg.draw.rect(self.screen, (14, 219, 248), (0, 0, SCREEN_WIDTH, 250))
            pg.draw.circle(self.screen, (255, 255, 51), (75, 75), 50)
            pg.draw.rect(self.screen, (255, 255, 51), (66, 150, 18, 70), border_radius=10)
            pg.draw.rect(self.screen, (255, 255, 51), (150, 41, 70, 18), border_radius=10)
            
            # Angled rectangle
            rectVar = pg.Rect((125, 140, 85, 18))
            shape_surf = pg.Surface(rectVar.size, pg.SRCALPHA)
            pg.draw.rect(shape_surf, (255, 255, 51), (0, 0, *rectVar.size), 0, border_radius=10)
            rotated_surf = pg.transform.rotate(shape_surf, 315)
            self.screen.blit(rotated_surf, rotated_surf.get_rect(center = rectVar.center))

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
                        self.playerEntity.img = pg.transform.flip(self.playerEntity.img, True, False)
                elif event.type == pg.KEYUP:  # key released
                    if event.key == pg.K_UP:
                        self.verticalMovement[self.playerId][0] = 0
                    elif event.key == pg.K_DOWN:
                        self.verticalMovement[self.playerId][1] = 0
                    elif event.key == pg.K_LEFT:
                        self.horizontalMovement[self.playerId][0] = 0
                    elif event.key == pg.K_RIGHT:
                        self.horizontalMovement[self.playerId][1] = 0
                        self.playerEntity.img = pg.transform.flip(self.playerEntity.img, True, False)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print(f"Mouse clicked: ({x}, {y})")

            pg.display.update()  # update the display with any changes
            self.clock.tick(60)  # force loop to run at 60 fps


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
