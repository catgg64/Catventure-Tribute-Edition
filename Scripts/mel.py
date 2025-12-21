import pygame
import spritemanager
import time

class Mel:
    def __init__(self, catventurete):
        self.catventurete = catventurete
        self.sprite_1 = pygame.image.load("Sprites/mel.png")
        self.sprite_1 = pygame.transform.scale(self.sprite_1, (100, 100))
        self.sprite_2 = pygame.image.load("Sprites/mel frame 1.png")
        self.sprite_2 = pygame.transform.scale(self.sprite_2, (100, 100))
        self.inverted_sprite_1 = pygame.transform.flip(self.sprite_1, True, False)
        self.inverted_sprite_2 = pygame.transform.flip(self.sprite_2, True, False)
        self.walking_1 = pygame.image.load("Sprites/mel walking frame 1.png")
        self.walking_1 = pygame.transform.scale(self.walking_1, (100, 100))
        self.inverted_walking_1 = pygame.transform.flip(self.walking_1, True, False)
        self.walking_2 = pygame.image.load("Sprites/mel walking frame 2.png")
        self.walking_2 = pygame.transform.scale(self.walking_2, (100, 100))
        self.inverted_walking_2 = pygame.transform.flip(self.walking_2, True, False)
        self.walking_3 = pygame.image.load("Sprites/mel walking frame 3.png")
        self.walking_3 = pygame.transform.scale(self.walking_3, (100, 100))
        self.inverted_walking_3 = pygame.transform.flip(self.walking_3, True, False)
        
        self.facing_right = False
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.coliderect = pygame.Rect(0, 0, 80, 20)
        self.is_walking = False
        self.was_walking = False
        self.anim_frames = 0
        self.true_anim_frames = 0
        self.in_animation = False
        self.animation = "walking"
        self.mov_pauses = 1
        self.speed = 5

    def update(self, screen, sprite_list, key, current_room):
        self.coliderect.x = self.rect.x + 10
        self.coliderect.y = self.rect.y + 70

        if key[pygame.K_RIGHT]:
            if pygame.time.get_ticks() % self.mov_pauses == 0:
                self.rect.x += self.speed
            self.facing_right = True
        if key[pygame.K_UP]:
            if pygame.time.get_ticks() % self.mov_pauses == 0:
                self.rect.y -= self.speed
        if key[pygame.K_DOWN]:
            if pygame.time.get_ticks() % self.mov_pauses == 0:
                self.rect.y += self.speed
        if key[pygame.K_LEFT]:
            if pygame.time.get_ticks() % self.mov_pauses == 0:
                self.rect.x -= self.speed
            self.facing_right = False
        
        self.was_walking = bool(self.is_walking)

        if key[pygame.K_RIGHT] or key[pygame.K_UP] or key[pygame.K_DOWN] or key[pygame.K_LEFT]:
            self.is_walking = True
        else:
            self.is_walking = False

        if self.was_walking == False and self.is_walking == True:
            self.in_animation = True
            self.animation = "walking"

        if self.is_walking == False and self.animation == "walking":
            self.in_animation = False
            self.animation = ""

        if self.in_animation:
            self.anim_frames += 1
            self.true_anim_frames = self.anim_frames // 12 % 4

        frame = time.time() // 2 % 2

        for _object in current_room:
            if self.coliderect.colliderect(_object.rect):
                if _object.type == "spike":
                    self.catventurete.reset_room()
                elif _object.type == "coin":
                    self.catventurete.coins += 1
                    current_room.remove(_object)
                    if self.catventurete.coins >= 3:
                        self.catventurete.advance_room()
        if self.in_animation:
            if self.animation == "walking":
                if self.true_anim_frames == 0:
                    if self.facing_right:
                        sprite_list.append(spritemanager.SpriteData(self.inverted_walking_1, self.rect.x, self.rect.y, 100, 100))
                    else:
                        sprite_list.append(spritemanager.SpriteData(self.walking_1, self.rect.x, self.rect.y, 100, 100))
                if self.true_anim_frames == 1:
                    if self.facing_right:
                        sprite_list.append(spritemanager.SpriteData(self.inverted_walking_2, self.rect.x, self.rect.y, 100, 100))
                    else:
                        sprite_list.append(spritemanager.SpriteData(self.walking_2, self.rect.x, self.rect.y, 100, 100))
                if self.true_anim_frames == 2:
                    if self.facing_right:
                        sprite_list.append(spritemanager.SpriteData(self.inverted_walking_3, self.rect.x, self.rect.y, 100, 100))
                    else:
                        sprite_list.append(spritemanager.SpriteData(self.walking_3, self.rect.x, self.rect.y, 100, 100))
                if self.true_anim_frames == 3:
                    if self.facing_right:
                        sprite_list.append(spritemanager.SpriteData(self.inverted_sprite_2, self.rect.x, self.rect.y, 100, 100))
                    else:
                        sprite_list.append(spritemanager.SpriteData(self.sprite_2, self.rect.x, self.rect.y, 100, 100))
        else:
            if frame == 0:
                if self.facing_right:
                    sprite_list.append(spritemanager.SpriteData(self.inverted_sprite_1, self.rect.x, self.rect.y, 100, 100))
                else:
                    sprite_list.append(spritemanager.SpriteData(self.sprite_1, self.rect.x, self.rect.y, 100, 100))
            elif frame == 1:
                if self.facing_right:
                    sprite_list.append(spritemanager.SpriteData(self.inverted_sprite_2, self.rect.x, self.rect.y, 100, 100))
                else:
                    sprite_list.append(spritemanager.SpriteData(self.sprite_2, self.rect.x, self.rect.y, 100, 100))
        
