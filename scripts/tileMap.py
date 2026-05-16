from scripts.header import *


NEIGHBOUR_OFFSETS = [(-1, -1), (0, -1), (1, -1),
                    (-1, 0), (0, 0), (1, 0),
                    (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {"grass", "stone"}


class TileMap:
    def __init__(self, game, tileSize=16):
        self.game = game
        self.tileSize = tileSize
        self.tileMap = {}
        self.offgridTiles = []

        for i in range(10):
            self.tileMap[f"{str(3 + i)};10"] = {"tileType": "grass", "variant": 1, "pos": (3 + i, 10)}
            self.tileMap[f"13;{str(1 + i)}"] = {"tileType": "stone", "variant": 1, "pos": (13, 1 + i)}
            
            # We're representing coordinates with a string instead of a tuple to make some future process easier for the sake of the tutorial
            # This tile dictionary containing tile, variant, and pos could be encapsulated into a Tile class instead
    
    def tilesSurrounding(self, pos):
        surroundingTiles = []
        tileLocation = (int(pos[0] // self.tileSize), int(pos[1] // self.tileSize))
        for offset in NEIGHBOUR_OFFSETS:
            checkLocation = f"{tileLocation[0] + offset[0]};{tileLocation[1] + offset[1]}"
            if checkLocation in self.tileMap:
                surroundingTiles.append(self.tileMap[checkLocation])
        return surroundingTiles

    def physicsRectsSurrounding(self, pos):
        physicsRects = []
        for tile in self.tilesSurrounding(pos):
            if tile["tileType"] in PHYSICS_TILES:
                physicsRects.append(
                    pg.Rect(tile["pos"][0] * self.tileSize, tile["pos"][1] * self.tileSize, 
                            self.tileSize, self.tileSize)
                )
        return physicsRects

    def render(self, surface):
        for tile in self.offgridTiles:
            surface.blit(self.game.assets[tile["tileType"]][tile["variant"]], tile["pos"])

        for loc in self.tileMap:
            tile = self.tileMap[loc]
            surface.blit(self.game.assets[tile["tileType"]][tile["variant"]],
                         (tile["pos"][0] * self.tileSize, tile["pos"][1] * self.tileSize))