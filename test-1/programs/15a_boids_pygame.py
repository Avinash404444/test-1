# Install: pip install pygame
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
boids = [
    [random.randint(50, 550), random.randint(50, 350),
     random.choice([-2, 2]), random.choice([-2, 2])]
    for _ in range(15)
]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    for boid in boids:
        boid[0] += boid[2]
        boid[1] += boid[3]
        if boid[0] <= 0 or boid[0] >= 600:
            boid[2] *= -1
        if boid[1] <= 0 or boid[1] >= 400:
            boid[3] *= -1
        pygame.draw.circle(screen, "blue", (int(boid[0]), int(boid[1])), 5)
    pygame.display.update()
    clock.tick(30)
pygame.quit()
