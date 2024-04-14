import pygame
import sys
from pygame.sprite import Sprite





class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.rect = pygame.Rect(0,0,15,3)
        self.color = (60,60,60)
        self.rect.midtop = ai_game.ship.rect.midright
        
        self.x = float(self.rect.x)

    def update(self):
        self.x += 3
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
class ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.image = pygame.transform.rotate(pygame.image.load('images/ship.bmp'),-90)
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)
        self.moving_right  = False
        self.moving_left = False
        self.moving_up = False
        self.moving_bottom = False

    def blite(self):
        self.screen.blit(self.image,self.rect)

    def movement(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -=10
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += 10
        self.rect.y = self.y



class sideWayRocket:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()


    def run(self):
       while True:
            self.check_events()
            self.ship.movement()
            self._update_bullets()
            self.screen.fill("white")
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
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
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
    
    def check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False
    
    def _update_bullets(self):
        self.bullets.update()
        surface = pygame.display.get_surface()
        for bullet in self.bullets.copy():
            print(bullet.rect.right)
            if -bullet.rect.right < -surface.get_width():
                self.bullets.remove(bullet)
                print(len(self.bullets))
    
    def fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
ai = sideWayRocket()
ai.run()