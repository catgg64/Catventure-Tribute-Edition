import pygame
import spritemanager
import random

class Spike():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 150, 150)
        self.image = pygame.image.load("Sprites/spike.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.type = "spike"
        self.init_x = x
        self.init_y = y

    def update(self, sprites):
        sprites.append(spritemanager.SpriteData(self.image, self.rect.x, self.rect.y, 150, 150))

    def reset(self):
        self.rect.x = self.init_x
        self.rect.y = self.init_y
        
class MovingSpike():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 150, 150)
        self.image = pygame.image.load("Sprites/spike.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.type = "spike"
        self.direction_x = random.randint(-10, 10)
        self.direction_y = random.randint(-10, 10)
        self.init_x = x
        self.init_y = y
        

    def update(self, sprites):
        self.rect.x += self.direction_x
        self.rect.y += self.direction_y
        if self.rect.x + 150 > 800 or self.rect.x < 0:
            self.direction_x *= -1
        if self.rect.y + 150 > 800 or self.rect.y < 0:
            self.direction_y *= -1 

        sprites.append(spritemanager.SpriteData(self.image, self.rect.x, self.rect.y, 150, 150))

    def reset(self):
        self.rect.x = self.init_x
        self.rect.y = self.init_y
        self.direction_x = random.randint(-10, 10)
        self.direction_y = random.randint(-10, 10)

class Coin():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 100)
        self.image = pygame.image.load("Sprites/coin.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.type = "coin"
        self.init_x = x
        self.init_y = y


    def update(self, sprites):
        sprites.append(spritemanager.SpriteData(self.image, self.rect.x, self.rect.y, 100, 100))
    
    def reset(self):
        self.rect.x = self.init_x
        self.rect.y = self.init_y

class FakeCoin():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 100)
        self.image = pygame.image.load("Sprites/coin.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.type = "fake coin"
        self.init_x = x
        self.init_y = y


    def update(self, sprites):
        sprites.append(spritemanager.SpriteData(self.image, self.rect.x, self.rect.y, 100, 100))
    
    def reset(self):
        self.rect.x = self.init_x
        self.rect.y = self.init_y


class SnakeX():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = pygame.image.load("Sprites/snake.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.inverted_image = pygame.transform.flip(self.image, True, False)
        self.type = "spike"
        self.velocity = 5
        self.init_x = x
        self.init_y = y

    def update(self, sprites):
        self.rect.x += self.velocity
        
        if self.rect.x >= 800:
            self.velocity *= -1
        elif self.rect.x <= 0:
            self.velocity *= -1
        
        if self.velocity > 0:
            sprites.append(spritemanager.SpriteData(self.inverted_image, self.rect.x, self.rect.y, 50, 50))
        elif self.velocity < 0:
            sprites.append(spritemanager.SpriteData(self.image, self.rect.x, self.rect.y, 50, 50))
        
    def reset(self):
        self.rect.x = self.init_x
        self.rect.y = self.init_y
        
class SnakeY():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = pygame.image.load("Sprites/snake.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.inverted_image = pygame.transform.flip(self.image, True, False)
        self.type = "spike"
        self.velocity = 5
        self.init_x = x
        self.init_y = y

    def update(self, sprites):
        self.rect.y += self.velocity
        
        if self.rect.y >= 800:
            self.velocity *= -1
        elif self.rect.y <= 0:
            self.velocity *= -1
    
        sprites.append(spritemanager.SpriteData(self.image, self.rect.x, self.rect.y, 50, 50))
    
    def reset(self):
        self.rect.x = self.init_x
        self.rect.y = self.init_y
