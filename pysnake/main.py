"""Main entrypoint file."""

import pygame

DIRECTIONS = [
    (0, -1),  # UP
    (1, 0),  # RIGHT
    (-1, 0),  # LEFt
    (0, 1),  # DOWN
]

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill("grey")
    clock = pygame.time.Clock()
    dt = 0
    speed = 50
    running = True

    direction = DIRECTIONS[0]

    player_pos: pygame.Vector2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            direction = DIRECTIONS[0]
        if keys[pygame.K_s]:
            direction = DIRECTIONS[3]
        if keys[pygame.K_d]:
            direction = DIRECTIONS[1]
        if keys[pygame.K_a]:
            direction = DIRECTIONS[2]

        player_pos += (speed * direction[0] * dt, speed * direction[1] * dt)

        screen.fill("grey")
        pygame.draw.circle(screen, "red", player_pos, 10)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()
