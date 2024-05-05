import pygame
import sys
import os
from pygame.sprite import Sprite

class RainDrop(Sprite):
    def __init__(self,ai_game):
        """Initialize the alien and set its starting fleet"""
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('rain.png')
        self.image = pygame.transform.scale(self.image,(76,76))
        self.rect = self.image.get_rect()
        self.rect.x - self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)



class Rain:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.rains = pygame.sprite.Group()
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self._create_rain_fleet()

    def _run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill("Purple")
            self.fleet_direction()
            self._update_drops()
            self.rains.draw(self.screen)
            pygame.display.flip()

            self.clock.tick(60)

    def _create_rain_fleet(self):
        """Create the fleet of rain."""
        drop = RainDrop(self)
        drop_width,drop_height = drop.rect.size
        current_x, current_y = drop_width,drop_height
        
        while current_y < (self.screen_height - 2 * drop_height):
            while current_x < (self.screen_width - 1 * drop_width):
                self._create_drop(current_x,current_y)
                current_x += 2 * drop_width
            
            current_x = drop_width
            current_y += 2 * drop_height
    
    def _create_drop(self,x_position,y_position):
        """Create an drop and place it in the fleet"""
        new_drop = RainDrop(self)
        new_drop.x = x_position
        new_drop.rect.x = x_position
        new_drop.rect.y = y_position
        self.rains.add(new_drop)
    
    def fleet_direction(self):
        for drop in self.rains.sprites():
            drop.rect.y += 10

    def _update_drops(self):
        for drop in self.rains.copy():
            if drop.rect.top > self.screen_height:
                self.rains.remove(drop)
                print(len(self.rains))
        if len(self.rains) == 0:
            self._create_rain_fleet()
rain = Rain()
rain._run()