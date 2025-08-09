import pygame
import time
import random
from datetime import datetime
import os       # needed to delete a temporary file


# Settings of the game [can be changed]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

snake_speed_initially = 15      # start speed of the snake
speed_increase = 1              # how much the speed will increase
speed_interval_increase = 40    # how often the speed will increase
gameover = 2                    # seconds
''' music_volume = 1 '''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



# Window size
window_x = 1000
window_y = 580

pygame.init()

game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake2023")

background_image = pygame.image.load("background(grass)_img2.jpg").convert()
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
grey   =  pygame.Color(9, 9, 9)   # [previous background color]
green  =  pygame.Color(0, 255, 0)
blue   =  pygame.Color(0, 0, 255)
#adcol  =  pygame.Color(163, 51, 61)

score_color =  pygame.Color(230, 230, 250)
#snake_color =  pygame.Color(255, 235, 0)
snake_color =  pygame.Color(255, 180, 255)


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
    background_image.blit(score_surface, score_rect)


# Game Over function
def game_over(score):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    tempFileName = "tempUsernameFile.txt"   # the name / location of the file
    
    tempFile = open(tempFileName, "r")      # opening the file with the username
    name = tempFile.read()          # reading the username from the file
    tempFile.close()            # closing the temporary file

    os.remove(tempFileName)     # deleting the file

    if name == "":          # if the user did not enter their name for some reason
        name = "Player"     # then just calling them "Player"
    
    now = datetime.now()
    dtnow = now.strftime("%d/%m/%Y %H:%M")   # getting accurate date and time

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    hScore = "0"
    fileData = [""]*2
    lastWrittenData = ""
    
    file = open("highest-score.txt", "r")
    if file.read() == "":       # checking if the file is empty or not 
        fileEmpty = True
    else:
        fileEmpty = False
    file.close()

    lastWrittenData = str(score) + "  -  " + name + "  -  " + str(dtnow) # saving the data for next operations
    
    if fileEmpty == True:       # if the file was empty then write down current score and date
        file = open("highest-score.txt", "w")
        file.write(str(score) + "  -  " + name + "  -  " + dtnow)
        file.close()
    else:                       # if not, getting the existing data from the file
        file = open("highest-score.txt", "r")
        fileData = file.readline().split("  -  ")
        hScore = fileData[0]    # getting the score separately
        name = fileData[1]      # getting the name of the player
        hDate = fileData[2]     # getting the date separately
        file.close
        
        file = open("highest-score.txt", "w")
        if score >= int(hScore):
            hScore = str(score)
            file.write(hScore +  "  -  " + name + "  -  " + dtnow) # writing data back to the file (if [1])
        else:
            file.write(hScore +  "  -  " + name + "  -  " + hDate) # writing data back to the file (if [2])
        file.close()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    file = open("games-history.txt", "r")
    fileData2 = file.read()         # opening the file and copying it copying the entire thing
    file.close()                    # closing the file

    file = open("games-history.txt", "w")
    file.write(lastWrittenData)     # writing the current data to the file
    file.write("\n" + fileData2)    # returning everything back to the file AFTER the current data
    file.close()
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    
    game_window.blit(gameover_image, [0,0])
    pygame.display.update()
    # after x seconds we will quit the 
    # program
    time.sleep(gameover)
    
    import SnakeGame
    SnakeGame.main()
    


scorecount = 0
snake_speed = snake_speed_initially
while done == False:            
    background_image = pygame.image.load("background(grass)_img2.jpg").convert()
    '''background_image = pygame.image.load("image.jpg").convert()'''
    #game_window.blit(background_image, [0,0])
    #pygame.display.update()
    #pygame.display.flip()
    
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                change_to = 'UP'
            if (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                change_to = 'DOWN'
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                change_to = 'LEFT'
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
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
    #game_window.fill(grey) #[idk if i have to use this]

    for pos in snake_body:
        pygame.draw.rect(background_image, snake_color, pygame.Rect(
          pos[0], pos[1], 10, 10))

    pygame.draw.rect(background_image, white, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))



    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over(score)
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over(score)


    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over(score)


    # displaying score countinuously
    show_score(1, score_color, 'Montserrat', 35)


    game_window.blit(background_image, [0,0])
    pygame.display.update()
    pygame.display.flip()
  

    # Frame Per Second / Refresh Rate
    fps.tick(snake_speed)
