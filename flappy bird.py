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
pipegap = 200
pipefreq = 3000
lastpipe = pygame.time.get_ticks() - pipefreq
score = 0 
pastpipe = False

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
        global gameover 
        if self.rect.y + self.velocity < HEIGHT - 180 and gameover == False:  
            self.velocity += self.gravity
            self.rect.y += self.velocity

        else:
            self.rect.y = HEIGHT - 180  
            self.velocity = 0  
            gameover = True 
            self.index = 1  
            self.image = self.images[self.index]
        
        if self.flapping and gameover == False:
            self.counter += 1
            if self.counter >= 5:  
                self.index = (self.index + 1) % 3
                self.image = self.images[self.index]
                self.counter = 0

    def jump(self):
        self.velocity = self.lift 
        self.flapping = True  
        
        

class Pipes (pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        super().__init__()
        self.image = pillar
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x,y)
        else:
            self.rect.topleft = (x, y)
    def update(self):
        self.rect.x = self.rect.x - 5
        if self.rect.right < 0:
            self.kill()

            

      

    

#Objects
bird = Flappybird(80, 300)
#Group of sprites
bird_gs = pygame.sprite.Group()
bird_gs.add(bird)
pipe_gs = pygame.sprite.Group()



#While loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    timenow = pygame.time.get_ticks()
    if timenow - lastpipe >= pipefreq:
        tp = Pipes(864,275,1)  
        bp = Pipes(864,475,0)
        pipe_gs.add(tp)
        pipe_gs.add(bp)
        lastpipe = timenow
        


    #Check if spacebar is pressed, if so, make the bird jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird.jump()  #Make the bird jump on spacebar press

        
    #Drawing screen
    screen.blit(bg, (0, 0))
  
    
    
    if gameover == False:
        floorx -= 5
        if floorx <= -36:
            floorx = 0
            
    else:
        #Stop the floor when the bird hits the ground
        floorx = 0

    #drawing sprite
    bird_gs.draw(screen)
    pipe_gs.draw(screen)
    #calling the update function
    bird.update()
    pipe_gs.update()
    screen.blit(floor, (floorx, 750))
    #update the display
    pygame.display.update()
    #control the frame rate (60 frames per second)
    pygame.time.Clock().tick(60)
