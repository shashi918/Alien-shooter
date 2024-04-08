# 12-5. Keys: Make a Pygame file that creates an empty screen. In the event loop, 
# print the event.key attribute whenever a pygame.KEYDOWN event is detected. Run 
# the program and press various keys to see how Pygame responds.


import sys
import pygame

class EventLoop:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1250,720))
        self.clock = pygame.time.Clock()
        self.running = True

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                
            self.screen.fill("purple")

            pygame.display.flip()

            self.clock.tick(60)



ai = EventLoop()

ai.run_game()

