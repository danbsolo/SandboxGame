import pygame as pg
import sys

class Game:
    def __init__(self):        
        pg.init()
        pg.display.set_caption("Ninja Game!")
        self.screen = pg.display.set_mode((640, 480))  # create the window
        self.clock = pg.time.Clock()

        self.img = pg.image.load('data/images/entities/toonLinkPixelTransparent.png')
        self.img = pg.transform.scale(self.img, (130, 146))
        # self.img.set_colorkey((0, 0, 0))  # make black pixels transparent
        self.imgPos = [260, 100]
        self.imgMovX = [False, False]  # [left, right]
        self.imgMovY = [False, False]  # [up, down]

        self.collisionArea = pg.Rect(500, 300, 100, 100)

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))  # (14, 219, 248) -> sky blue

            speed = 13
            self.imgPos[1] += (self.imgMovY[1] * speed) - (self.imgMovY[0] * speed)  # True == 1. False == 0.
            self.imgPos[0] += (self.imgMovX[1] * speed) - (self.imgMovX[0] * speed)  # True == 1. False == 0.

            imgHitbox = pg.Rect(self.imgPos[0], self.imgPos[1], self.img.get_width(), self.img.get_height())

            if imgHitbox.colliderect(self.collisionArea):
                pg.draw.rect(self.screen, (150, 0, 0), self.collisionArea)
            else:
                pg.draw.rect(self.screen, (150, 100, 0), self.collisionArea)

            self.screen.blit(self.img, self.imgPos)

            for event in pg.event.get():  # get user input
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:  # key pressed
                    if event.key == pg.K_UP:
                        self.imgMovY[0] = True
                    elif event.key == pg.K_DOWN:
                        self.imgMovY[1] = True
                    elif event.key == pg.K_LEFT:
                        self.imgMovX[0] = True
                    elif event.key == pg.K_RIGHT:
                        self.imgMovX[1] = True
                elif event.type == pg.KEYUP:  # key released
                    if event.key == pg.K_UP:
                        self.imgMovY[0] = False
                    elif event.key == pg.K_DOWN:
                        self.imgMovY[1] = False
                    elif event.key == pg.K_LEFT:
                        self.imgMovX[0] = False
                    elif event.key == pg.K_RIGHT:
                        self.imgMovX[1] = False

            pg.display.update()  # update the display with any changes
            self.clock.tick(60)  # force loop to run at 60 fps


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
