import pygame, radom
from pygame.locaos import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)
    
    def collision(c1, c2):
        return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('snake')

snake = [(200, 200), (210, 300), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill ((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
            if event.type == KEYDOWN:
                If event.key == K_UP:
                    my_direction UP
                If event.key == K_DOWN:
                    my_direction DOWN
                If event.key == K_LEFT:
                    my_direction LEFT
                If event.key == K_RIGHT:
                    my_direction RIGHT
            
            if collision(snake[0], apple_pos):
                apple_pos = on_grid_random()
                snake.append((0,0))
      
      for i in range(len(snake)-1, 0, -1):
                 snake[i]  = (snake[i-1][0], snake[i-1][1])
      
            if my_direction == UP:
                sbake[0] = (snake[0][0], snake[0][1] - 10)
            if my_direction == DOWN:
                sbake[0] = (snake[0][0], snake[0][1] + 10)
            if my_direction == RIGHT:
                sbake[0] = (snake[0][0] + 10, snake[0][1])
            if my_direction == LEFT:
                sbake[0] = (snake[0][0] - 10, snake[0][1] ) 
            
    screen.fill((0,0,0,))
    screen.blit(apple, apple_pos)
    for pos in snake:
            screen.blit(pygame.Surface(snake_skin, pos)
            
    pygame.display.update()