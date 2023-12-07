"""Main entrypoint file."""

from enum import IntEnum

import pygame


class Direction(IntEnum):
    """Direction enum."""

    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


# map the direction enums to the corresponding vector
DIRECTIONS: dict[Direction, pygame.Vector2] = {
    Direction.UP: pygame.Vector2(0, -1),
    Direction.DOWN: pygame.Vector2(0, 1),
    Direction.RIGHT: pygame.Vector2(1, 0),
    Direction.LEFT: pygame.Vector2(-1, 0),
}


def _get_direction(direction: Direction) -> Direction:
    """Function to get the direction from player input.

    Queries the active keys pressed and returns the Direction from that.
    Returns the current direction if nothing is pressed.

    Allows WASD or standard keyboard arrow movement.

    Args:
        direction (Direction): the current direction

    Returns:
        Direction: the direction
    """
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        return Direction.UP

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        return Direction.DOWN

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        return Direction.RIGHT

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        return Direction.LEFT

    return direction


if __name__ == "__main__":
    pygame.init()

    # initialise some variables
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    running: bool = True
    delta_time: float = 0

    # player vars
    speed: int = 50
    size: int = 10
    direction: Direction = Direction.RIGHT
    # set player position to middle of screen
    player_pos: pygame.Vector2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    # constant loop
    while running:
        # handle events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # move the player
        direction = _get_direction(direction)
        player_pos += DIRECTIONS[direction] * speed * delta_time

        # redraw the screen
        # redraw the player at the new position
        screen.fill("grey")
        pygame.draw.circle(screen, "red", player_pos, size)

        # KEEP AT THE END
        # updates the screen with any rendering updates from above
        # keeps the framerate constant and gets the time between each frame
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

    pygame.quit()
