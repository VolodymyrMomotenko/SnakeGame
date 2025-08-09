import pygame
import time
import random


# Settings of the game [can be changed]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

snake_speed_initially = 20
speed_increase = 1
speed_interval_increase = 20
gameover = 3        # seconds
''' music_volume = 1 '''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 




# Window size
window_x = 1000
window_y = 580

pygame.init()

game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake2023")

background_image = pygame.image.load("background(grass)_img.jpg").convert()
gameover_image = pygame.image.load("game_over_img.jpeg").convert()

sound = pygame.mixer.Sound("action_sound.mp3")
# pygame.mixer.music.set_volume(music_volume)
# mixer.music.pause()


# Refresh game screen
game_window.blit(background_image, [0,0])
pygame.display.update()
pygame.display.flip()

# FPS controller
fps  =  pygame.time.Clock()

done = False

# Defining colors
black  =  pygame.Color(0, 0, 0)
white  =  pygame.Color(255, 255, 255)
red    =  pygame.Color(255, 0, 0)
grey   =  pygame.Color(9, 9, 9)
green  =  pygame.Color(0, 255, 0)
blue   =  pygame.Color(0, 0, 255)
adcol  =  pygame.Color(163, 51, 61)

# Snake position and body
snake_x = random.randint(12, 60) * 10
snake_y = random.randint(8, 40) * 10
snake_position = [snake_x, snake_y]
rnum = random.randint(0,3)
if rnum == 0:
    snake_body = [  [snake_x, snake_y],
                    [snake_x - 10, snake_y],
                    [snake_x - 20, snake_y],
                    [snake_x - 30, snake_y]
            ]
    direction = 'RIGHT'
    change_to = direction
elif rnum == 2:
    snake_body = [  [snake_x, snake_y],
                    [snake_x + 10, snake_y],
                    [snake_x + 20, snake_y],
                    [snake_x + 30, snake_y]
            ]
    direction = 'LEFT'
    change_to = direction
elif rnum == 3:
    snake_body = [  [snake_x, snake_y],
                    [snake_x, snake_y + 10],
                    [snake_x, snake_y + 20],
                    [snake_x, snake_y + 30]
            ]
    direction = 'UP'
    change_to = direction
elif rnum == 1:
    snake_body = [  [snake_x, snake_y],
                    [snake_x, snake_y - 10],
                    [snake_x, snake_y - 20],
                    [snake_x, snake_y - 30]
            ]
    direction = 'DOWN'
    change_to = direction
    

# fruit posiiton 
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True


# initial score
score = 0


# display score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font,size)

    # create the display surface object
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)


# Game Over function
def game_over():
    game_window.blit(gameover_image, [0,0])
    pygame.display.update()
    # after x seconds we will quit the 
    # program
    time.sleep(gameover)
    # deactivating pygame library
    pygame.quit()
    # quit the program
    quit()


scorecount = 0
snake_speed = snake_speed_initially
while done == False:
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        
                
    # stopping from moving in 2 directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        pygame.mixer.Sound.play(sound)
        pygame.mixer.music.stop()
        fruit_spawn = False
        snake_speed = snake_speed_initially + (score // speed_interval_increase) * speed_increase
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True
    game_window.fill(grey) #[idk if i have to use this]

    for pos in snake_body:
        pygame.draw.rect(game_window, red, pygame.Rect(
          pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))



    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()


    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()


    # displaying score countinuously
    show_score(1, adcol, 'Montserrat', 35)


    # game_window.blit(background_image, [0,0])
    pygame.display.update()
    pygame.display.flip()
  

    # Frame Per Second /Refres Rate
    fps.tick(snake_speed)
