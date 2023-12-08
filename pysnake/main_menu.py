"""File for our main menu."""

import pygame
from pygame.surface import Surface
from scenes import Scene


class MainMenu(Scene):
    """Class for main menu scene."""

    def __init__(self, name: str, screen: Surface) -> None:
        """Initialisation method.

        Args:
            name (str): scene name
            screen (Surface): the screen to write to
        """
        super().__init__(name, screen)

        # plan is to have the background colour shifting - static for now
        self.start_colour = pygame.Color("blue")

    def update(self, _: float) -> Scene:
        """Update method.

        Called once per frame.

        Args:
            delta_time (float): time since the last frame

        Returns:
            Scene: returns self
        """
        self.screen.fill(self.start_colour)
        return self
