import pygame
import time
import random

#run game
pygame.init()

display_width = 1200
display_height = 1000

#rgb colors(0-255,255,255)
black = (0,0,0)
white = (255,255,255)
red = (255, 0,0)
block_color = (53, 115, 255)

#set screen size of game(input tuple)
gameDisplay = pygame.display.set_mode((display_width, display_height))

#display game name
pygame.display.set_caption("A bit Racey")

#set a clock for game
clock = pygame.time.Clock()

carImg = pygame.image.load("images/car_model.png")
car_width = carImg.get_width() // 4
car_height = carImg.get_height() // 4
carImg = pygame.transform.scale(carImg, (car_width, car_height))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

# Car position
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    
    time.sleep(2)
    game_loop()

def crash():
    message_display("You Crashed")

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    dodged = 0

    gameExit = False

    while not gameExit:
        # handles wheter user clicks keys or where the mouse on the screen(list of events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Key control
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change

        #Background color
        gameDisplay.fill(white)

        # Objects
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed

        # car position
        car(x,y)
        things_dodged(dodged)

        if x + car_width > display_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.5

        if y < thing_starty + thing_height:
            #y cross over
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()
        
        #updates surface(screen)
        pygame.display.update()
        #frames per second(if want fast and smooth, increase it)
        clock.tick(60)

# stop game from running
game_loop()
pygame.quit()
quit()