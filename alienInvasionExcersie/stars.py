from random import randint
import pygame
import sys
from pygame.sprite import Sprite

class StarImage(Sprite):
    def __init__(self,ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()

        # start each new alien newar the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position.
        self.x = float(self.rect.x)



class star:
    def __init__(self):
        pygame.init()
        self.screen_height = 720
        self.screen_width = 1280
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.star = pygame.sprite.Group()

        self._create_fleet()


    def _run(self):
        while True:
            self._checkEvents()
            self.screen.fill("yellow")
            self.star.draw(self.screen)
            pygame.display.flip()
            self.clock.tick()

    def _checkEvents(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

    def _create_fleet(self):
        star = StarImage(self)
        star_width, star_height = star.rect.size
        current_x,current_y = star_width,star_height
        while current_y < (self.screen_height - 3 * star_height):
            while current_x < (self.screen_width - 2 * star_width):
                self._create_star(current_x,current_y)
                current_x += 2 * star_width
        
            current_x = star_width
            current_y += 2* star_height
        

    def _create_star(self,x_position,y_position):
        """Create an alien and plave it in the fleet"""
        new_star = StarImage(self)
        new_star.x = x_position
        new_star.rect.x= randint(0,1280)
        new_star.rect.y = randint(0,720)
        self.star.add(new_star)
a= star()
a._run()
