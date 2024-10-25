import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("python piano program")#sets the window title
screen = pygame.display.set_mode((800, 400))#creates game screen
xpos = 0
ypos = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
press = False

class Pianokey:
    def __init__(self, x):
        self.x = x
    def pykeydraw(self):
        pygame.draw.rect(screen, (WHITE), (0 + self.x, 100, 100, 300))
        pygame.draw.rect(screen, (BLACK), (0 + self.x, 100, 100, 300), 2)
        if mousePos[0] > 0 and mousePos[0] < self.x and mousePos[1] >100:
            key = 1
        else: key = 0
        if key == 1:
            pygame.mixer.Sound.play(k1)
            pygame.draw.rect(screen, (150,150,150), (0 + self.x ,100,100,300))

#audio stuff!
pygame.mixer.init()
k1 = pygame.mixer.Sound("key01.mp3")
k2 = pygame.mixer.Sound("key02.mp3")
k3 = pygame.mixer.Sound("key03.mp3")
k4 = pygame.mixer.Sound("key04.mp3")
k5 = pygame.mixer.Sound("key05.mp3")
k6 = pygame.mixer.Sound("key06.mp3")
k7 = pygame.mixer.Sound("key07.mp3")
k8 = pygame.mixer.Sound("key08.mp3")
k9 = pygame.mixer.Sound("key09.mp3")
k10 = pygame.mixer.Sound("key10.mp3")
k11 = pygame.mixer.Sound("key11.mp3")
k12 = pygame.mixer.Sound("key12.mp3")



#this holds onto what key the user has pressed
key = 0

#gameloop###################################################
while True:
    print(mousePos) #this is just for testing so you can see the mouse coordinates on the screen!
    
    #event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
    
    #update/timer section---------------------------------------    
    if mousePos[0] > 0 and mousePos[0] < 100 and mousePos[1] >100:
        key = 1
    elif mousePos[0] > 100 and mousePos[0] < 200 and mousePos[1] >100:
        key = 3
    #add more keys here!
    else:
        key = 0
    
    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        press = True

    if event.type == pygame.MOUSEBUTTONUP:
        press = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos


    #render section---------------------------------------------

    #the keys 
    pygame.draw.rect(screen, (255, 255, 255), (0, 100, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 100, 300))
    #key outlines
    pygame.draw.rect(screen, (0, 0, 0), (0, 100, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (100, 100, 100, 300), 2)
    
    #if a key is pressed, highlight in grey and play the sound:
    if press == True:
        if key == 0:
            print("no key")
        elif key == 1:
            pygame.mixer.Sound.play(k1)
            pygame.draw.rect(screen, (150,150,150), (0,100,100,300))
        elif key == 3:
            pygame.mixer.Sound.play(k3)
            pygame.draw.rect(screen, (150,150,150), (100,100,100,300))
    
    pygame.display.flip() #always needed at the end of every game loop!
    

#end game loop##############################################

pygame.quit()