import pygame
import os
import sys

OGImage = pygame.image.load(os.path.join('Assets', 'stickmanpost2.png'))

class Character(object):  # represents the stickman
    def __init__(self):
        """ The constructor of the class """
        self.isJump = False
        self.jumpCount = 10
        self.image = pygame.transform.scale(OGImage, (70,200))
        # the bird's position
        self.x = 0
        self.y = 200

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left
        elif key[pygame.K_UP]:
            self.y -= dist
        

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))
    
    def jump(self):
        if self.isjump:
            self.y -= 1000

    def gravity(self):
        if self.y < 200:
            self.y += 0.2
        else:
            self.y = 200

pygame.init()
screen = pygame.display.set_mode((640, 400))

mainCharacter = Character() # create an instance
clock = pygame.time.Clock()

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            sys.exit(0)
            running = False

    mainCharacter.handle_keys() # handle the keys

    screen.fill((255,255,255)) # fill the screen with white
    mainCharacter.gravity()
    mainCharacter.draw(screen) # draw the bird to the screen
    pygame.display.update() # update the screen

    clock.tick(40)

