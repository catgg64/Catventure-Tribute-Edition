import pygame
import spritemanager

class Mel:
    def __init__(self, catventurete):
        self.catventurete = catventurete
        self.sprite_1 = pygame.image.load("Sprites/mel.png")
        self.sprite_1 = pygame.transform.scale(self.sprite_1, (100, 100))
        self.x = 0
        self.y = 0
        

    def update(self, screen, sprite_list, key):
        if key[pygame.K_RIGHT]:
            self.x += 5
        if key[pygame.K_UP]:
            self.y -= 5
        if key[pygame.K_DOWN]:
            self.y += 5
        if key[pygame.K_LEFT]:
            self.x -= 5

        sprite_list.append(spritemanager.SpriteData(self.sprite_1, self.x, self.y, 100, 100))
