import pygame
import spritemanager
import mel

pygame.init()

class Catventure:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Catventure: Tribute Edition")
        self.running = True  
        self.sprites = []
        self.offset_x = 0
        self.offset_y = 0

        self.mel = mel.Mel(self)

        self.pressing_right = False
        self.pressing_up = False
        self.pressing_down = False
        self.pressing_left = False

        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)


    def event_handling(self):
        self.pressing_right = False
        self.pressing_up = False
        self.pressing_down = False
        self.pressing_left = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.K_LEFT:
                self.pressing_left = True
            if event.type == pygame.K_DOWN:
                self.pressing_down = True
            if event.type == pygame.K_UP:
                self.pressing_up = True
            if event.type == pygame.K_RIGHT:
                self.pressing_right = True

    def update(self):
        self.event_handling()
        self.screen.fill("cadetblue1")

        self.sprites = []

        self.key = pygame.key.get_pressed()

        self.mel.update(self.screen, self.sprites, self.key)

        spritemanager.update_sprite_list(self.sprites, self.offset_x, self.offset_y, 800, 800, self.screen)

        pygame.display.update()
        self.clock.tick(60)

catventure = Catventure()
while catventure.running:
    catventure.update()
