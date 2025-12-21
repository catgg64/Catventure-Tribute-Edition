import pygame
import spritemanager

class StartButton():
    def __init__(self):
        self.rect = pygame.Rect(325, 325, 150, 150)
        self.image = pygame.image.load("Sprites/beta button.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
    
    def update(self, mouse_pos, surface, rooms, mouse_pressed, catventure):
        catventure.sprites.append(spritemanager.SpriteData(self.image, self.rect.x, self.rect.y, 150, 150))
        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            catventure.advance_room()
        
