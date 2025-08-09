import pygame
import sys


pygame.init()

width = 1000
height = 580
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Start Window")





MDS = 19    # max amount of scores displayed
counter = 0

# opening games history file
file = open("games-history.txt", "r")

scores = [""] * MDS
score = [""] * MDS
lineSep = [""] * 2

for line in file:
    scores[counter] = line[:-1]
    lineSep = scores[counter].split("  -  ")
    spaces1 = 5 - len(lineSep[0])
    spaces2 = 8 - len(lineSep[1])
    
    scores[counter] = lineSep[0] + str(spaces1 * "  ") + "-     "  + lineSep[1] + ("   " * spaces2) + "-   " + lineSep[2]
    if counter == MDS:
        break
    counter += 1
    
file.close()






# colors
screen_color = (60,25,60)                       # TO BE CHANGED

white = (255,255,255)

color_light = (170, 170, 170)                   # might need to be changed
color_dark = (100, 100, 100)                    # might need to be changed

color_active = pygame.Color('lightskyblue3')    # TO BE CHANGED 
color_passive = pygame.Color('chartreuse4')     # TO BE CHANGED 


# fonts
inputFONT = pygame.font.SysFont('Corbel', 40)
inputinfoFONT = pygame.font.SysFont('Corbel', 15)

HistoryFONT = pygame.font.SysFont('Corbel', 25)
scoresFONT = pygame.font.SysFont('Corbel', 20)

startFONT = pygame.font.SysFont('Corbel', 60)
quitFONT = pygame.font.SysFont('Corbel', 30)


# textboxes
inputinfo = inputinfoFONT.render('* press in the box above to enter your name', True, white)

START = startFONT.render('START' , True , white)
QUIT = quitFONT.render('QUIT', True, white)

History = HistoryFONT.render("Last games' scores:", True, white)
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
                tempFile.write(userText)
                tempFile.close()
                
                import Snake2023_v5
                Snake2023_v5.main()
                

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
    
    screen.blit(inputinfo, (370, 215))
    screen.blit(START, (417, 372))
    screen.blit(QUIT, (466, 492))
    screen.blit(History, (30, 40))

    for i in range(MDS):
        screen.blit(score[i], (30, 75 + i*22))

    # screen.blit(BestScore, (30, 850))

    #  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 




    # update the frames of the game
    pygame.display.update()
