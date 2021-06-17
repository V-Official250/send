import pygame,sys

class Window (object):
    def __init__(self,width,height,title):
        self.width = width
        self.height = height
        self.title = title

        self.window = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.maxfps = 9999

        pygame.display.set_caption(self.title)

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
        self.clock.tick(self.maxfps)

    def clear(self,red=0, green=0, blue=0):
        self.window.fill((red,green,blue))

    def load(self,path):
        return pygame.image.load(path)

    def blit(self,img,x,y):
        self.window.blit(img,(x,y))