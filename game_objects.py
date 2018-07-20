#Space Invaders Game objects - Samuel McHale - 19/7/18

class alien():
    
    def __init__(self, pointScore, shape):
        self.pointScore = pointScore
        self.properties = shape
        self.ob = 'alien'

    def drift(self):
        self.properties[1] += 1

class player():
    
    def __init__(self, shape):
        self.properties = shape
        self.ob = 'user'
    
    def move(self,key):
        if key == 275:
            if (self.properties[0] + 10) <= 650:
                self.properties[0] += 10
        elif key == 276:
            if (self.properties[0] - 10) >= 0:
                self.properties[0] -= 10

class bullet():

    def __init__(self, pos):
        self.properties = [pos[0] - 2,pos[1],5,10]
        self.ob = 'bullet'

    def drift(self):
        self.properties[1] -= 3


