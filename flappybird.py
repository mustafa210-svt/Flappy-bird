import pygame

#setting up screen
#screen 
HEIGHT = 600
WIDTH = 600
TITLE = "RECYCLABALE GAME"
run = True
#Setting up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

#loading the images
bird_up = pygame.image.load("flappy bird.png")
bird_down = pygame.image.load("flappy bird down.png")
bird = pygame.image.load("flappy bird nuetral.png")
bg = pygame.image.load("fb bg.png")
pillar = pygame.image.load("pillar.png")
floor = pygame.image.load("floor.png")

class Flappybird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images = [bird_up,bird,bird_down] 
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
#objects
bird = Flappybird(80,300)
#group of sprites
bird_gs = pygame.sprite.Group()
bird_gs.add(bird)


#while loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #drawing screen
    screen.blit(bg, (0, 0))
    #drawing sprite
    bird_gs.draw(screen)

    #update the display
    pygame.display.update()
    #control the frame rate (60 frames per second)
    pygame.time.Clock().tick(60)