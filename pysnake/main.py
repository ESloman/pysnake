"""Main entrypoint file."""

import pygame

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill("grey")
    clock = pygame.time.Clock()
    dt = 1
    running = True

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.circle(screen, "red", player_pos, 10)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()
