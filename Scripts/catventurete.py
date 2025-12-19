import pygame

pygame.init()

class Catventure:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Catventure: Tribute Edition")
        self.running = True  

        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)


    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.event_handling()
        
        pygame.display.update()
        #self.clock.tick(60)

catventure = Catventure()
while catventure.running:
    catventure.update()
