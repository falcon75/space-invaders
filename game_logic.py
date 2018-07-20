import time
from game_objects import *
import random

class space_invaders(object):

    def __init__(self):
        self.score = 0
        self.level = 0
        self.start_time = time.time()
        self.user = player([325,400,50,50])
        self.objects = [self.user]
        self.generate_alien()
        self.alien_rates = {0:60,1:50,2:42,3:35,4:30,5:26,6:23,7:21,8:20}

    def generate_alien(self):
        x = random.randint(100,580)
        a1 = alien(200,[x,25,20,20])
        self.objects.append(a1)

    def shoot(self):
        b1 = bullet([self.user.properties[0] + 25, self.user.properties[1] + 1])
        self.objects.append(b1)

    def get_level(self):
        t1 = time.time() - self.start_time
        count = 0
        while t1 > 20:
            t1 -= 20
            count += 1
        self.level = count

def do_boxes_overlap(p1, p2):
    if overlapping(p1[0], p1[2], p2[0], p2[2]) and overlapping(p1[1], p1[3], p2[1], p2[3]):
        return True

def overlapping(a1, a2, b1, b2):
    
    axmin = a1
    axmax = a1 + a2
    bxmin = b1
    bxmax = b1 + b2

    if greater(abs(axmin - bxmax),abs(axmax - bxmin)) > (a2 + b2):
        return False
    else:
        return True

def greater(x,y):
    if x > y:
        return x
    else:
        return y
