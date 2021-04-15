'''
Trajon Brown
11/29/18
Dodging Life Game 
My game is a falling object dodging game. The player is to
avoid as many bills as possible. If a bill
is hit the game will say "You Crashed".
Then it will restart after a 3 second waiting period.
The game then keeps the highscore until
you play again.
'''
import pygame
import time
import random

pygame.init()
music = pygame.mixer.music.load('01.mp3')
#screen size
display_width = 800
display_height = 600
#colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
#man size 
man_width = 175
man_height = 175
img = 'bills.png'
img = pygame.image.load(img)

background_img = pygame.image.load('building.png')
fail_img = pygame.image.load('fail_img.png')
gamedisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Dodging Life!')
clock = pygame.time.Clock()
#load in man 
BmanImg = pygame.image.load('Bman3.png')
pygame.display.set_icon(BmanImg)

with open('highscore!', 'r+') as f: # opens text file with highscores
        contents = f.readlines()
       
def things_dodged(count): # counts the number of bills passed and shows it
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gamedisplay.blit(text,(0,20))
    
def Highscore(): # displays highscore 
    with open('highscore!', 'r+') as f: # reads from file to show highscore
        contents = f.read()
        contents = sorted(contents)
        
    font = pygame.font.SysFont(None, 25)
    text = font.render("Highscore: " + contents[-1] , True, black)
    gamedisplay.blit(text,(0,2))
    
def quit_screen(): # displays the options to pay again or quit
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
         
        gamedisplay.blit(background_img, [0,0])
        small = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = title_text('You are now in debt!', small)
        TextRect.center =((display_width/2),(display_height/2))
        gamedisplay.blit(TextSurf, TextRect)

        with open('highscore!', 'r+') as f: # reads from file to show highscore
            contents = f.read()
            contents = sorted(contents)
            
        font = pygame.font.SysFont(None, 50)
        text = font.render("Highscore: " + contents[-1] , True, black)
        gamedisplay.blit(text,(0,2))
            
            
        try_again_button('Try again',150,450,100,50,green,bright_green,game_loop)
        quit_button('quit',550,450,100,50,red,bright_red,'quit')                     
        pygame.display.update()
        clock.tick(15)
    
def things(thingx, thingy, thingw, thingh, color): # displays falling bills
    gamedisplay.blit(img,(thingx, thingy, thingw, thingh))
                           
def man(x,y): #displays business man 
    gamedisplay.blit(BmanImg,(x,y))
    
def other_text(text,font): #colors small text 
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def title_text(text,font): #colors larger text 
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message(text): #shows the "you crashed" and restarts game
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = title_text(text, largeText)
    TextRect.center =((display_width/2),(display_height/2))
    gamedisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(3)
    quit_screen()
    game_loop()

def crash(): 
    message('You Crashed')

def Button(msg,x,y,w,h,i,a,action=None): #makes so you can join game loop when clicking start in main menu
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplay,a,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gamedisplay,i,(x,y,w,h))
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = other_text('Start',smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gamedisplay.blit(textSurf,textRect)
    
def try_again_button(msg,x,y,w,h,i,a,action=None): # makes it possible to replay game in fail screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplay,a,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gamedisplay,i,(x,y,w,h))
        
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = other_text('Try again!',smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gamedisplay.blit(textSurf,textRect)
    
def quit_button(msg,x,y,w,h,i,a,action=None): # makes it possible to quit when in fail screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplay,a,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
                quit()

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gamedisplay,i,(x,y,w,h))
        
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = other_text('Quit!',smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gamedisplay.blit(textSurf,textRect)
    
def Main_menu(): #creates title and main menu screen
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gamedisplay.blit(background_img, [0,0])
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = title_text('Dodging Life', largeText)
        TextRect.center =((display_width/2),(display_height/2))
        gamedisplay.blit(TextSurf, TextRect)
        
        with open('highscore!', 'r+') as f:
            contents = f.read()
            contents = sorted(contents)
        
        font = pygame.font.SysFont(None, 50)
        text = font.render("Last Highscore: " + contents[-1], True, black)
        gamedisplay.blit(text,(0,2))
        
        Button('Start',350,450,100,50,green,bright_green,game_loop)
                          
        pygame.display.update()
        clock.tick(15)
    
def game_loop(): #makes the game run, object fall, and man move
    pygame.mixer.music.play(-1)
        
    x = (display_width * 0.35)
    y = (display_height * .7)
    
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 10
    thing_width = 75
    thing_height = 51

    thingCount = 1

    dodged = 0

    gameExit = False 
    
    crashed = False
    
    while not gameExit:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                
        x += x_change
        gamedisplay.blit(background_img, [0,0])
        
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        
        thing_starty += thing_speed
        man(x,y)
        things_dodged(dodged)
        Highscore()

        if x > display_width - man_width or x < 0:
                crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1

        if x in range(thing_startx-man_width,thing_startx+thing_width):
            if y in range(thing_starty-man_height,thing_starty+thing_height):
                with open('highscore!', 'a+') as f: #saves new highscore to file
                    f.write(str(dodged))
                crash()
        pygame.display.update()
        clock.tick(60)
Main_menu()
game_loop()
pygame.quit()
quit()






