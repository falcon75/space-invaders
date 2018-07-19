import time
from game_objects import *
import random

class space_invaders(object):

    def __init__(self):
        self.score = 0
        self.start_time = time.time()
        self.user = player([325,425,50,50])
        self.objects = [self.user]
        self.generate_alien()

    def generate_alien(self):
        x = random.randint(1,700)
        a1 = alien(200,[x,10,20,20])
        self.objects.append(a1)

    def shoot(self):
        b1 = bullet([self.user.properties[0] + 25, self.user.properties[1] + 1])
        self.objects.append(b1)

def do_boxes_overlap(p1, p2):
    x = False
    y = False
    for i in range(p1[2]):
        i = i + p1[0]
        for j in range(p2[2]):
            j = j + p2[0]
            if i == j:
                x = True
    for i in range(p1[3]):
        i = i + p1[1]
        for j in range(p2[3]):
            j = j + p2[1]
            if i == j:
                y = True
    return (x and y)
