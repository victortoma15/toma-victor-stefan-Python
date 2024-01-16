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
            self.texture = pg.transform.scale(new_texture,(new_texture.get_width() * 1.2, new_texture.get_height() * 1.2))
            self.render()