# 12-4. Rocket: Make a game that begins with a rocket in the center of the screen. 
# Allow the player to move the rocket up, down, left, or right using the four arrow 
# keys. Make sure the rocket never moves beyond any edge of the screen.



import sys
import pygame


class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()

        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_bottom = False

    def blite(self):
         self.screen.blit(self.image,self.rect)

    def movement(self):
        """"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 10
        elif self.moving_left and self.rect.left > 0:
            self.x -= 10
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -=10
            print(self.y)
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += 10
        self.rect.x = self.x
        self.rect.y = self.y

class Rocket:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)


    def run_game(self):
        while True:
            self.check_events()
            self.ship.movement()
            self.screen.fill("purple")
            self.ship.blite()
            pygame.display.flip()
            
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self.check_keyup_events(event)
    
    def check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

ai = Rocket()
ai.run_game()