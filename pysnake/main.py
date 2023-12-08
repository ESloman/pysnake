"""Main entrypoint file."""

import pygame
from main_menu import MainMenu

if __name__ == "__main__":
    pygame.init()

    # initialise some variables
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    running: bool = True
    delta_time: float = 0

    current_scene = MainMenu("menu", screen)

    # constant loop
    while running:
        # handle events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_scene = current_scene.update(delta_time)

        # KEEP AT THE END
        # updates the screen with any rendering updates from above
        # keeps the framerate constant and gets the time between each frame
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

    pygame.quit()
