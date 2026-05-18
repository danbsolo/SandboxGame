import pygame as pg
from random import randint, uniform, choice

SCREEN_WIDTH = 1920 #1366 #640
SCREEN_HEIGHT = 1080 #768 #480

CONTAINER_DIVIDER = 2

NEIGHBOUR_OFFSETS = [(-1, -1), (0, -1), (1, -1),
                    (-1, 0), (0, 0), (1, 0),
                    (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {"grass", "stone", "spikes"}
DEATH_TILES = {"spikes"}
TILEMAP_PATH = "data/maps/"

TILE_SIZE = 20