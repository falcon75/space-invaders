import pygame
import game_logic
import time
import random

#Game Setup
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
pygame.key.set_repeat(10,10)

#Loading Images
ship = pygame.image.load('ship.jpg')
alien1 = pygame.image.load('alien.png')
alien2 = pygame.image.load('alien2.png')
background = pygame.image.load('background.jpg')

#Setting Fonts
font1 = pygame.font.SysFont(None, 25)
font2 = pygame.font.SysFont(None, 40)

#Function for drawing all objects onto the window
def refresh():
    screen.fill((0xFF, 0xFF, 0xFF))
    screen.blit(background,(0,0))
    text = font1.render('Score: ' + str(game.score) + '  Level: ' + str(game.level), True, (0,0,0))
    screen.blit(text, (275,5))
    for item in game.objects:
        if item.ob == 'user':
            screen.blit(ship, (item.properties[0],item.properties[1]))
        elif item.ob == 'alien':
            if item.alienType == 'n':
                screen.blit(alien1, (item.properties[0],item.properties[1]))
            elif item.alienType == 's':
                screen.blit(alien2, (item.properties[0], item.properties[1]))
        else:
            pygame.draw.rect(screen, (0,0,0),item.properties)
    pygame.display.flip()

#Initialisation of game
game = game_logic.space_invaders()
refresh()
t = 0
fail = False

#Main Loop
while not fail:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 276 or event.key == 275:
                game.user.move(event.key)
            elif (event.key == 32) and ((time.time() - t) > 0.5):
                game.shoot()
                t = time.time()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

    for item in game.objects:
        if item.ob == 'bullet':
            item.drift()
            if item.properties[1] < 0:
                game.objects.remove(item)

    for item in game.objects:
        if item.ob == 'alien':
            item.drift()
            if (item.properties[1] > 480) or (item.properties[0] > 700):
                game.objects.remove(item)
                fail = True

    if game.level > 8:
        rate = game.alien_rates[8]
    else:
        rate = game.alien_rates[game.level]
        
    if random.randint(1,rate) == 1:
        game.generate_alien()


    for alien in game.objects:
        if alien.ob == 'alien':
            for bullet in game.objects:
                if bullet.ob == 'bullet':
                    if game_logic.do_boxes_overlap(alien.properties,bullet.properties) == True:
                        game.objects.remove(alien)
                        game.objects.remove(bullet)
                        game.score += alien.pointScore

    game.get_level()
    refresh()
    clock.tick(30)

#Game Over Screen
screen.fill((0xFF, 0xFF, 0xFF))
text = font2.render('Game Over', True, (0,0,0))
screen.blit(text, (250,200))
text = font1.render('Score: ' + str(game.score) + '  Level: ' + str(game.level), True, (0,0,0))
screen.blit(text, (250,250))
pygame.display.flip()
input()

