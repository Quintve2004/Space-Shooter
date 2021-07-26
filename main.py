import pygame
import os

# Window Setup
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game @Quint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VEL = 5
BULLET_VEL = 7

RED_EVENT = pygame.USEREVENT + 1
YELLOW_EVENT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

BORDERLINE = pygame.Rect(WIDTH/2 -5, 0, 10, HEIGHT)

RED_BULLET = []
YELLOW_BULLET = []

def draw_window(red, yellow, red_bullet, yellow_bullet):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))

    for bullet in red_bullet:
        pygame.draw.rect(WIN, BLACK, bullet)
    for bullet in yellow_bullet:
        pygame.draw.rect(WIN, BLACK, bullet)

    pygame.draw.rect(WIN, BLACK, BORDERLINE)
    pygame.display.update() #Updates display


def yellow_handle_movement(keys_pressed, yellow):
    if yellow.x > 0:
        if keys_pressed[pygame.K_a]:  # Left
            yellow.x -= VEL
    if yellow.x <= WIDTH/2 - 50:
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
    if red.x > WIDTH/2:
        if keys_pressed[pygame.K_LEFT]:  # Left
            red.x -= VEL
    if red.y < 450:
        if keys_pressed[pygame.K_DOWN]:  # Down
            red.y += VEL
    if red.y > 0:
        if keys_pressed[pygame.K_UP]:  # Up
            red.y -= VEL

def bullet_handling(red_bullet, yellow_bullet, red, yellow):

    for bullet in YELLOW_BULLET:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_EVENT))
            yellow_bullet.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullet.remove(bullet)

    for bullet in RED_BULLET:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_EVENT))
            red_bullet.remove(bullet)
        elif bullet.x < 0:
            red_bullet.remove(bullet)
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(YELLOW_BULLET) < 3:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 + 2, 10, 5)
                    YELLOW_BULLET.append(bullet)

                if event.key == pygame.K_RSHIFT and len(RED_BULLET) < 3:
                    bullet = pygame.Rect(red.x - red.width, red.y + red.height // 2 + 2, 10, 5)
                    RED_BULLET.append(bullet)

            if event.type == RED_EVENT:
                print(1)
            if event.type == YELLOW_EVENT:
                print(2)

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        bullet_handling(RED_BULLET, YELLOW_BULLET, red, yellow)
        draw_window(red, yellow, RED_BULLET, YELLOW_BULLET) # call Draw window

    pygame.quit()

if __name__ == "__main__":
    main()
