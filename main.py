import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    v = 20  # пикселей в секунду
    fps = 60
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 100), 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                pygame.draw.rect(screen, (0, 255, 0), (x, y, 100, 100), 0)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()