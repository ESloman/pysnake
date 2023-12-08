"""File for our scene class."""

from pygame.surface import Surface


class Scene:
    """Our scene class."""

    def __init__(self, name: str, screen: Surface) -> None:
        """Initialisation method.

        Args:
            name (str): the scene's name
            screen (Surface): the surface we can update
        """
        self.name = name
        self.screen = screen

    def update(self, delta_time: float) -> None:
        """Our update method.

        Called once per frame.

        Args:
            delta_time (float): the time since the last frame

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
