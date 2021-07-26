import pygame
import os

# Window Setup
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game @Quint")

WHITE = (255, 255, 255)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VEL = 5

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    pygame.display.update() #Updates display

def yellow_handle_movement(keys_pressed, yellow):
    if yellow.x > 0:
        if keys_pressed[pygame.K_a]:  # Left
            yellow.x -= VEL
    if yellow.x <= 380:
        if keys_pressed[pygame.K_d]:  # Right
            yellow.x += VEL
    if yellow.y < 450:
        if keys_pressed[pygame.K_s]:  # Down
            yellow.y += VEL
    if yellow.y > 0:
        if keys_pressed[pygame.K_w]:  # Up
            yellow.y -= VEL

def red_handle_movement(keys_pressed, red):
    if red.x < 850:
        if keys_pressed[pygame.K_RIGHT]:  # Right
            red.x += VEL
    if red.x >= 420:
        if keys_pressed[pygame.K_LEFT]:  # Left
            red.x -= VEL
    if red.y < 450:
        if keys_pressed[pygame.K_DOWN]:  # Down
            red.y += VEL
    if red.y > 0:
        if keys_pressed[pygame.K_UP]:  # Up
            red.y -= VEL

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) # Up, Down, Left, Right keys
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) # W, A, S ,D keys

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        draw_window(red, yellow) # call Draw window

    pygame.quit()

if __name__ == "__main__":
    main()
