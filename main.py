import pygame
import os

# Window Setup
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game @Quint")

pygame.font.init()

HEALTH_FONT = pygame.font.SysFont("Courier", 24)
WINNER_FONT = pygame.font.SysFont("comicsans", 120)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (40, 62, 175)

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


def draw_window(red, yellow, red_bullet, yellow_bullet, red_health, yellow_health):
    WIN.fill(BLACK)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)

    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    for bullet in red_bullet:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullet:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.draw.rect(WIN, WHITE, BORDERLINE)
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

def draw_winner(text):
        textWinner = WINNER_FONT.render(str(text), 1, BLUE)
        WIN.blit(textWinner, (WIDTH/2 - textWinner.get_width()/2 + 20, HEIGHT/2))
        pygame.display.update()
        pygame.time.delay(5000)

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) # Up, Down, Left, Right keys
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) # W, A, S ,D keys

    clock = pygame.time.Clock()
    run = True

    red_health = 100
    yellow_health = 100

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(YELLOW_BULLET) < 3:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 + 2, 10, 5)
                    YELLOW_BULLET.append(bullet)

                if event.key == pygame.K_RSHIFT and len(RED_BULLET) < 3:
                    bullet = pygame.Rect(red.x - red.width, red.y + red.height // 2 + 2, 10, 5)
                    RED_BULLET.append(bullet)

            if event.type == RED_EVENT:
                red_health -= 20
                print(red_health)

            if event.type == YELLOW_EVENT:
                yellow_health -= 20
                print(yellow_health)

        scoreText = ""
        if red_health <= 0:
            scoreText = "Yellow wins"

        if yellow_health <= 0:
            scoreText = "Red wins"

        if scoreText != "":
            draw_winner(scoreText)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        bullet_handling(RED_BULLET, YELLOW_BULLET, red, yellow)
        draw_window(red, yellow, RED_BULLET, YELLOW_BULLET, red_health, yellow_health) # call Draw window

    main()

if __name__ == "__main__":
    main()
