import pygame
import sys
import time
import random
from datetime import datetime
import os       # needed to delete a temporary file

pygame.init()


def StartScreen():
    width = 1000
    height = 580
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("Start Window")





    MDS = 19    # max amount of scores displayed
    counter = -1

    # opening games history file
    file = open("games-history.txt", "r")

    scores = [""] * MDS
    score = [""] * MDS
    lineSep = [""] * 2

    for line in file:
        counter += 1
        if counter >= MDS:
            break
        if line == "":
            break
        scores[counter] = line[:-1]
        lineSep = scores[counter].split("  -  ")
        spaces1 = 5 - len(lineSep[0])
        spaces2 = 8 - len(lineSep[1])

        scores[counter] = lineSep[0] + str(spaces1 * "  ") + "-     "  + lineSep[1] + ("   " * spaces2) + "-   " + lineSep[2]
    
    file.close()




    file = open("highest-score.txt", "r")

    theBestScore = file.read()
    
    file.close()




    # colors
    screen_color = (60,25,60)                       # TO BE CHANGED

    white = (255,255,255)

    color_light = (170, 170, 170)                   # might need to be changed
    color_dark = (100, 100, 100)                    # might need to be changed

    color_active = pygame.Color('lightskyblue3')    # TO BE CHANGED 
    color_passive = pygame.Color('chartreuse4')     # TO BE CHANGED 


    # fonts
    CRFONT = pygame.font.SysFont('Corbel', 15)
    
    inputFONT = pygame.font.SysFont('Corbel', 40)
    inputinfoFONT = pygame.font.SysFont('Corbel', 15)

    HistoryFONT = pygame.font.SysFont('Corbel', 25)
    scoresFONT = pygame.font.SysFont('Corbel', 20)

    startFONT = pygame.font.SysFont('Corbel', 60)
    quitFONT = pygame.font.SysFont('Corbel', 30)

    BestScoreFONT = pygame.font.SysFont('Corbel', 25)
    bsFONT = pygame.font.SysFont('Corbel', 20)


    # textboxes

    copyrights = CRFONT.render('© All rights reserved', True, white)
    
    inputinfo = inputinfoFONT.render('* press in the box above to enter your name', True, white)

    START = startFONT.render('START' , True , white)
    QUIT = quitFONT.render('QUIT', True, white)

    BestScore = BestScoreFONT.render('Best score:', True, white)
    bs = bsFONT.render(theBestScore, True, white)

    History = HistoryFONT.render("Previous games:", True, white)
    for i in range(MDS):
        score[i] = scoresFONT.render(scores[i], True, white)

    userText = ""
    inputRECT = pygame.Rect(400, 150, 200, 50)
    current_color = color_passive

    active = False

    while True:
        for event in pygame.event.get():
            # closing pygame window if presing the "close" button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # if START pressed then loading the actual snake game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 400 <= mouse[0] <= 600 and 350 <= mouse[1] <= 450:
                    tempFile = open("tempUsernameFile.txt", "w")

                    if len(userText) >= 10:
                        userText = userText[0:10] + "..."
                        
                    tempFile.write(userText)
                    tempFile.close()
                
                    MainGame()
                

            # if QUIT presses then closing the whole thing
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 550 and 480 <= mouse[1] <= 530:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputRECT.collidepoint(event.pos):
                    active = True
                else:
                    active = False
        
            if event.type == pygame.KEYDOWN and active:
                # checking for backspace
                if event.key == pygame.K_BACKSPACE:
                    # taking back the last symbol from the line
                    userText = userText[:-1]
                else:
                    userText += event.unicode
            

        # fills the screen with a color
        screen.fill(screen_color)

        if active:
            current_color = color_active
        else:
            current_color = color_passive
        
        # getting the position of the mouse
        mouse = pygame.mouse.get_pos()





        #  - - - - - drawing the INPUT box and changing color / size of it - - - - - - - - - - - - - - - - - - - - 

        pygame.draw.rect(screen, current_color, inputRECT)

        text_surface = inputFONT.render(userText, True, white)
    
        screen.blit(text_surface, (inputRECT.x + 9, inputRECT.y + 6))

        inputRECT.w = max(200, text_surface.get_width() + 10)

        '''pygame.display.flip()'''
    
        #  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 




        #  - - - - - drawing START and QUIT buttons and changing colors if mouse hovers over them - - - - - - - - -
    
        # if mouse is hovered on th START button it changes to lighter shade
        if 400 <= mouse[0] <= 600 and 350 <= mouse[1] <= 450:
            pygame.draw.rect(screen, color_light, [400, 350, 200, 100])
        else:
            pygame.draw.rect(screen, color_dark, [400, 350, 200, 100])

        # if mouse is hovered on the QUIT button it changes to lighter shade
        if 450 <= mouse[0] <= 550 and 480 <= mouse[1] <= 530:
            pygame.draw.rect(screen, color_light, [450, 480, 100, 50])
        else:
            pygame.draw.rect(screen, color_dark, [450, 480, 100, 50])


        # displaying text

        screen.blit(copyrights, (860, 550))
    
        screen.blit(inputinfo, (385, 210))
        screen.blit(START, (417, 372))
        screen.blit(QUIT, (466, 492))
        screen.blit(History, (30, 40))

        for i in range(MDS):
            screen.blit(score[i], (18, 75 + i*22))

        screen.blit(BestScore, (696, 40))
        screen.blit(bs, (684, 75))

        #  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 




        # update the frames of the game
        pygame.display.update()



def MainGame():
    # Settings of the game [can be changed]
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    snake_speed_initially = 15      # start speed of the snake
    speed_increase = 1              # how much the speed will increase
    speed_interval_increase = 50    # how often the speed will increase
    gameover = 3                    # seconds
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
        while name[-1] == "\n":
            name = name[:-1]
    
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
            hname = fileData[1]      # getting the name of the player
            hDate = fileData[2]     # getting the date separately
            file.close
        
            file = open("highest-score.txt", "w")
            if score >= int(hScore):
                hScore = str(score)
                file.write(hScore +  "  -  " + name + "  -  " + dtnow) # writing data back to the file (if [1])
            else:
                file.write(hScore +  "  -  " + hname + "  -  " + hDate) # writing data back to the file (if [2])
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
    
        StartScreen()
    


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
            pygame.draw.rect(background_image, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(background_image, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))



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



StartScreen()
