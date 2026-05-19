from scripts.header import *
import json
import os


class TileMap:
    def __init__(self, game, tileMapVariation):
        self.game = game
        self.tileMap = {}
        self.offgridTiles = []

        with open(os.path.join(TILEMAP_PATH, f"{tileMapVariation}.json"), "r") as mapFile:
            self.tileMap = json.load(mapFile)["tilemap"]
        
        # We're representing coordinates with a string instead of a tuple to make some future process easier for the sake of the tutorial
        # This tile dictionary containing tile, variant, and pos could be encapsulated into a Tile class instead
    
    def tilesSurrounding(self, pos):
        surroundingTiles = []
        tileLocation = (int(pos[0] // TILE_SIZE), int(pos[1] // TILE_SIZE))
        for offset in NEIGHBOUR_OFFSETS:
            checkLocation = f"{tileLocation[0] + offset[0]};{tileLocation[1] + offset[1]}"
            if checkLocation in self.tileMap:
                surroundingTiles.append(self.tileMap[checkLocation])
        return surroundingTiles


    def render(self, surface):
        for tile in self.offgridTiles:
            surface.blit(self.game.assets[tile["tileType"]][tile["variant"]], tile["pos"])

        for loc in self.tileMap:
            tile = self.tileMap[loc]
            surface.blit(self.game.assets[tile["tileType"]][tile["variant"]],
                         (tile["pos"][0] * TILE_SIZE, tile["pos"][1] * TILE_SIZE))