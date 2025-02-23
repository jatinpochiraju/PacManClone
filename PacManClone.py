import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Clone")

# Load assets
pacman = pygame.Rect(300, 300, GRID_SIZE, GRID_SIZE)
velocity = GRID_SIZE

ghosts = [pygame.Rect(random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
                      random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE, GRID_SIZE, GRID_SIZE)]

direction = "STOP"
pellets = [pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, 5, 5) for x in range(WIDTH // GRID_SIZE) for y in
           range(HEIGHT // GRID_SIZE)]

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"

    # Move Pac-Man
    if direction == "UP":
        pacman.y -= velocity
    elif direction == "DOWN":
        pacman.y += velocity
    elif direction == "LEFT":
        pacman.x -= velocity
    elif direction == "RIGHT":
        pacman.x += velocity

    # Keep Pac-Man within bounds
    pacman.x %= WIDTH
    pacman.y %= HEIGHT

    # Draw Pac-Man
    pygame.draw.rect(screen, YELLOW, pacman)

    # Draw pellets
    for pellet in pellets[:]:
        pygame.draw.rect(screen, WHITE, pellet)
        if pacman.colliderect(pellet):
            pellets.remove(pellet)

    # Move and draw ghosts
    for ghost in ghosts:
        pygame.draw.rect(screen, RED, ghost)
        if pacman.colliderect(ghost):
            running = False

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
