import pygame as pg

BASE_IMG_PATH = "data/images/"

def loadImage(path, convert=True, colorKey=(0, 0, 0), size=None):
    # convert() makes image more efficient for rendering
    img = pg.image.load(BASE_IMG_PATH + path) #.convert()
    
    if convert:
        img = img.convert()

    if colorKey:
        img.set_colorkey((0, 0, 0))

    if size:
        img = pg.transform.scale(img, size)

    return img
