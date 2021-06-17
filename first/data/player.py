import pygame

class Player:
    def __init__(self,x=120,y=300,width=32,height=32):
        self.rect = pygame.Rect(x,y,width,height)
        self.texture = pygame.transform.scale(pygame.image.load("./data/img/player.png"),(width,height))
        self.texture.set_colorkey((255,255,255))
        self.gravity = 4
        self.died = False
        
        self.jumpForce = 0
        self.jumpCount = 0
        self.isJump = False

    def update(self,windowf,dt):
        if not self.died:
            windowf.blit(self.texture,self.rect.x,self.rect.y)
            self.Keys(dt)

    def Keys(self,dt):
        self.rect.y += self.gravity * dt

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and self.isJump == False:
            self.isJump = True

        if self.isJump == True:
            self.jumpForce = 25
            self.isJump = False

        if self.jumpForce >= 0:
            self.rect.y -= self.jumpForce
            self.jumpForce -= 2 * dt