import pygame,random

class Level:
    def __init__(self):
        self.walls = []
        self.gencount = 0

    def update(self,dt,player,window):
        if player.died == False:
            for rect in self.walls:
                if player.rect.colliderect(rect):
                    player.died = True

            if self.gencount > 25:
                self.walls.append(random.choice([pygame.Rect(400,0,60,200),pygame.Rect(400,300,60,200)]))
                self.gencount = 0;
            else:
                self.gencount -= 0.25 * dt

        for rect in self.walls:
            pygame.draw.rect(window,(255,0,0),rect)

        print("working")