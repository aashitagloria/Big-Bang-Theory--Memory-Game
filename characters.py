import random
import os
import game_config as gc

from pygame import image, transform

characters_count = dict((a, 0) for a in gc.ASSET_FILES)

def available_characters():
    return [character for character, count in characters_count.items() if count < 2]

class Character:
    def __init__(self, index):
        self.index = index
        self.name = random.choice(available_characters())
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.skip = False
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))

        characters_count[self.name] += 1
