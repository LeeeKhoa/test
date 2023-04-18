import pygame
import random
screen_width = 480
screen_height = 480

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rắn săn mồi")
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(screen_width / 2, screen_height / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        self.score = 0

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
def move_snake(snake):
    head_x, head_y = snake.positions[0]

    if snake.direction == UP:
        new_head = (head_x, head_y - 10)
    elif snake.direction == DOWN:
        new_head = (head_x, head_y + 10)
    elif snake.direction == LEFT:
        new_head = (head_x - 10, head_y)
    elif snake.direction == RIGHT:
        new_head = (head_x + 10, head_y)

    snake.positions = [new_head] + snake.positions[:-1]

def handle_keys(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
