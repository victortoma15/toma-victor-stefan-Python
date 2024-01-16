import random
from collections import deque

import pygame as pg


class Hexagon:
    def __init__ (self, hex_type: int, row: int, col: int) -> None:
        """
        Constructor for the Hexagon class.
        """
        self.hex_type = hex_type
        self.row = row
        self.col = col

    def setup_surface (self, position: tuple, margin: int, texture: pg.Surface, display: pg.Surface) -> None:
        """
        Sets up the surface of the hexagon.
        """
        self.display = display
        if texture is not None:
            self.texture = texture
            texture_width = texture.get_width()
            texture_height = texture.get_height()
            self.rect = pg.Rect((position[0] + margin, position[1] + margin),
                                (texture_width - margin * 2, texture_height - margin * 2))
        else:
            self.texture = None
            self.rect = pg.Rect(0, 0, 0, 0)

    def render (self) -> None:
        """
        Draws the hexagon.
        """
        self.display.blit(self.texture, self.rect.topleft)

    def update_type (self, new_type, new_texture) -> None:
        """
        Updates the type of the hexagon.
        """
        if self.hex_type != 1:
            self.hex_type = new_type
            self.texture = pg.transform.scale(new_texture,
                                              (new_texture.get_width() * 1.2, new_texture.get_height() * 1.2))
            self.render()


class GameButton:
    def __init__ (self, x: int, y: int, scale: float, image: pg.Surface, display: pg.Surface) -> None:
        """
        Constructor for the GameButton class.
        """
        self.display = display
        scaled_width = int(image.get_width() * scale)
        scaled_height = int(image.get_height() * scale)
        self.texture = pg.transform.scale(image, (scaled_width, scaled_height))
        self.rect = self.texture.get_rect(topleft=(x, y))

    def render (self) -> None:
        """
        Draws the button.
        """
        if self.texture is not None and self.rect is not None:
            self.display.blit(self.texture, self.rect.topleft)


def spawn_blocks (matrix: list, count: int) -> list:
    """
    Places a specified number of obstacles randomly on the board.
    """
    for _ in range(count):
        x, y = random.randint(1, 10), random.randint(1, 10)
        while matrix[x][y] == 3 or (x == 6 and y == 6):
            x, y = random.randint(1, 10), random.randint(1, 10)
        matrix[x][y] = 3

    return matrix