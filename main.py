import pygame
import game_logic
import time
import random

pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
pygame.key.set_repeat(10,10)

def refresh():
    screen.fill((0xFF, 0xFF, 0xFF))
    for item in game.objects:
        pygame.draw.rect(screen, (0,0,0),item.properties)
    pygame.display.flip()

game = game_logic.space_invaders()
refresh()
t = 0
fail = False

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
            if item.properties[1] > 480:
                game.objects.remove(item)
                fail = True

    if random.randint(1,75) == 1:
        game.generate_alien()

    for alien in game.objects:
        if alien.ob == 'alien':
            a = alien.properties
            for bullet in game.objects:
                if bullet.ob == 'bullet':
                    b = bullet.properties
                    if game_logic.do_boxes_overlap(a,b) == True:
                        game.objects.remove(alien)
                        game.objects.remove(bullet)
                        game.score += 20
    
    refresh()
    clock.tick(15)

