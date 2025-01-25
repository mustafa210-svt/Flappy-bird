import pygame


#screen 
HEIGHT = 900
WIDTH = 864
TITLE = "Flappy bird"

#Setting up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

#variables
floorx = 0
gameover = False
flying = False
run = True

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
        self.images = [bird_up, bird, bird_down] 
        self.index = 1  
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.velocity = 0
        self.gravity = 0.25  
        self.lift = -8  
        self.flapping = True  
        
    def update(self):
        if self.rect.y + self.velocity < HEIGHT - 100:  
            self.velocity += self.gravity
            self.rect.y += self.velocity
        else:
            self.rect.y = HEIGHT - 100  
            self.velocity = 0  
            self.flapping = False  
            self.index = 1  
            self.image = self.images[self.index]
        
        if self.flapping:
            self.counter += 1
            if self.counter >= 5:  
                self.index = (self.index + 1) % 3
                self.image = self.images[self.index]
                self.counter = 0

    def jump(self):
        self.velocity = self.lift 
        self.flapping = True  
        


  
    

#Objects
bird = Flappybird(80, 300)
#Group of sprites
bird_gs = pygame.sprite.Group()
bird_gs.add(bird)

#While loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
  

    #Check if spacebar is pressed, if so, make the bird jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird.jump()  #Make the bird jump on spacebar press

    #Drawing screen
    screen.blit(bg, (0, 0))
    screen.blit(floor, (floorx, 750))

    if bird.rect.y < HEIGHT - 100:
        floorx -= 5
        if floorx <= -36:
            floorx = 0
    else:
        #Stop the floor when the bird hits the ground
        floorx = 0

    #drawing sprite
    bird_gs.draw(screen)
    #calling the update function
    bird.update()
    #update the display
    pygame.display.update()
    #control the frame rate (60 frames per second)
    pygame.time.Clock().tick(60)
