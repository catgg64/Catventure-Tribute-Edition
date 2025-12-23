import pygame
import spritemanager
import time
import math

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
        self.stage_2_sprite_1 = pygame.image.load("Sprites/stage 2 mel.png")
        self.stage_2_sprite_1 = pygame.transform.scale(self.stage_2_sprite_1, (100, 100))
        self.stage_2_sprite_2 = pygame.image.load("Sprites/stage 2 mel frame 1.png")
        self.stage_2_sprite_2 = pygame.transform.scale(self.stage_2_sprite_2, (100, 100))
        self.stage_2_inverted_sprite_1 = pygame.transform.flip(self.stage_2_sprite_1, True, False)
        self.stage_2_inverted_sprite_2 = pygame.transform.flip(self.stage_2_sprite_2, True, False)
        self.stage_2_walking_1 = pygame.image.load("Sprites/stage 2 mel walking frame 1.png")
        self.stage_2_walking_1 = pygame.transform.scale(self.stage_2_walking_1, (100, 100))
        self.stage_2_inverted_walking_1 = pygame.transform.flip(self.stage_2_walking_1, True, False)
        self.stage_2_walking_2 = pygame.image.load("Sprites/stage 2 mel walking frame 2.png")
        self.stage_2_walking_2 = pygame.transform.scale(self.stage_2_walking_2, (100, 100))
        self.stage_2_inverted_walking_2 = pygame.transform.flip(self.stage_2_walking_2, True, False)
        self.stage_2_walking_3 = pygame.image.load("Sprites/stage 2 mel walking frame 3.png")
        self.stage_2_walking_3 = pygame.transform.scale(self.stage_2_walking_3, (100, 100))
        self.stage_2_inverted_walking_3 = pygame.transform.flip(self.stage_2_walking_3, True, False)
        self.stage_3_sprite_1 = pygame.image.load("Sprites/stage 3 mel.png")
        self.stage_3_sprite_1 = pygame.transform.scale(self.stage_3_sprite_1, (100, 100))
        self.stage_3_sprite_2 = pygame.image.load("Sprites/stage 3 mel frame 1.png")
        self.stage_3_sprite_2 = pygame.transform.scale(self.stage_3_sprite_2, (100, 100))
        self.stage_3_inverted_sprite_1 = pygame.transform.flip(self.stage_3_sprite_1, True, False)
        self.stage_3_inverted_sprite_2 = pygame.transform.flip(self.stage_3_sprite_2, True, False)
        self.stage_3_walking_1 = pygame.image.load("Sprites/stage 3 mel walking frame 1.png")
        self.stage_3_walking_1 = pygame.transform.scale(self.stage_3_walking_1, (100, 100))
        self.stage_3_inverted_walking_1 = pygame.transform.flip(self.stage_3_walking_1, True, False)
        self.stage_3_walking_2 = pygame.image.load("Sprites/stage 3 mel walking frame 2.png")
        self.stage_3_walking_2 = pygame.transform.scale(self.stage_3_walking_2, (100, 100))
        self.stage_3_inverted_walking_2 = pygame.transform.flip(self.stage_3_walking_2, True, False)
        self.stage_3_walking_3 = pygame.image.load("Sprites/stage 3 mel walking frame 3.png")
        self.stage_3_walking_3 = pygame.transform.scale(self.stage_3_walking_3, (100, 100))
        self.stage_3_inverted_walking_3 = pygame.transform.flip(self.stage_3_walking_3, True, False)
        self.stage_4_sprite_1 = pygame.image.load("Sprites/stage 4 mel.png")
        self.stage_4_sprite_1 = pygame.transform.scale(self.stage_4_sprite_1, (100, 100))
        self.stage_4_sprite_2 = pygame.image.load("Sprites/stage 4 mel frame 1.png")
        self.stage_4_sprite_2 = pygame.transform.scale(self.stage_4_sprite_2, (100, 100))
        self.stage_4_inverted_sprite_1 = pygame.transform.flip(self.stage_4_sprite_1, True, False)
        self.stage_4_inverted_sprite_2 = pygame.transform.flip(self.stage_4_sprite_2, True, False)
        self.stage_4_walking_1 = pygame.image.load("Sprites/stage 4 mel walking frame 1.png")
        self.stage_4_walking_1 = pygame.transform.scale(self.stage_4_walking_1, (100, 100))
        self.stage_4_inverted_walking_1 = pygame.transform.flip(self.stage_4_walking_1, True, False)
        self.stage_4_walking_2 = pygame.image.load("Sprites/stage 4 mel walking frame 2.png")
        self.stage_4_walking_2 = pygame.transform.scale(self.stage_4_walking_2, (100, 100))
        self.stage_4_inverted_walking_2 = pygame.transform.flip(self.stage_4_walking_2, True, False)
        self.stage_4_walking_4 = pygame.image.load("Sprites/stage 4 mel walking frame 4.png")
        self.stage_4_walking_4 = pygame.transform.scale(self.stage_4_walking_4, (100, 100))
        self.stage_4_inverted_walking_4 = pygame.transform.flip(self.stage_4_walking_4, True, False)
        self.dead_mel = pygame.image.load("Sprites/dead mel.png")
        self.dead_mel = pygame.transform.scale(self.dead_mel, (125, 78))
        self.dead_mel = pygame.transform.flip(self.dead_mel, True, False)
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
        self.stage = 1
        self.anim_speed = 12
        self.over = False
        self.darkness = 0
        self.true_darkness = 0
        
    def update(self, screen, sprite_list, key, current_room):
        self.coliderect.x = self.rect.x + 10
        self.coliderect.y = self.rect.y + 70

        if self.catventurete.room == 7:
            self.speed = 40
            self.mov_pauses = 100 
            self.anim_speed = 100

        if not self.over:
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
            self.true_anim_frames = self.anim_frames // self.anim_speed % 4

        frame = time.time() // 2 % 2

        for _object in current_room:
            if self.coliderect.colliderect(_object.rect):
                if _object.type == "spike":
                    self.catventurete.reset_room()
                    break
                elif _object.type == "coin":
                    self.catventurete.coins += 1
                    current_room.remove(_object)
                    if self.catventurete.coins >= 3:
                        self.catventurete.advance_room()
                elif _object.type == "fake coin":
                    self.catventurete.current_room.remove(_object)

        if self.catventurete.room == 7 and (abs(self.catventurete.current_coin_room[0].rect.x - self.rect.x) <= 350 or abs(self.catventurete.current_coin_room[0].rect.x - self.rect.x) <= 350):
            self.over = True
            self.darkness += 1
            self.true_darkness = self.darkness - 500
            if self.true_darkness < 0:
                self.true_darkness = 0
            elif self.true_darkness > 255:
                self.true_darkness = 255
            
        if not self.over:
            if self.stage == 1:
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
            elif self.stage == 2:
                if self.in_animation:
                    if self.animation == "walking":
                        if self.true_anim_frames == 0:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_2_inverted_walking_1, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_2_walking_1, self.rect.x, self.rect.y, 100, 100))
                        if self.true_anim_frames == 1:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_2_inverted_walking_2, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_2_walking_2, self.rect.x, self.rect.y, 100, 100))
                        if self.true_anim_frames == 2:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_2_inverted_walking_3, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_2_walking_3, self.rect.x, self.rect.y, 100, 100))
                        if self.true_anim_frames == 3:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_2_inverted_sprite_2, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_2_sprite_2, self.rect.x, self.rect.y, 100, 100))
                else:
                    if frame == 0:
                        if self.facing_right:
                            sprite_list.append(spritemanager.SpriteData(self.stage_2_inverted_sprite_1, self.rect.x, self.rect.y, 100, 100))
                        else:
                            sprite_list.append(spritemanager.SpriteData(self.stage_2_sprite_1, self.rect.x, self.rect.y, 100, 100))
                    elif frame == 1:
                        if self.facing_right:
                            sprite_list.append(spritemanager.SpriteData(self.stage_2_inverted_sprite_2, self.rect.x, self.rect.y, 100, 100))
                        else:
                            sprite_list.append(spritemanager.SpriteData(self.stage_2_sprite_2, self.rect.x, self.rect.y, 100, 100))
            elif self.stage == 3:
                if self.in_animation:
                    if self.animation == "walking":
                        if self.true_anim_frames == 0:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_3_inverted_walking_1, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_3_walking_1, self.rect.x, self.rect.y, 100, 100))
                        if self.true_anim_frames == 1:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_3_inverted_walking_2, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_3_walking_2, self.rect.x, self.rect.y, 100, 100))
                        if self.true_anim_frames == 2:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_3_inverted_walking_3, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_3_walking_3, self.rect.x, self.rect.y, 100, 100))
                        if self.true_anim_frames == 3:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_3_inverted_sprite_2, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_3_sprite_2, self.rect.x, self.rect.y, 100, 100))
                else:
                    if frame == 0:
                        if self.facing_right:
                            sprite_list.append(spritemanager.SpriteData(self.stage_3_inverted_sprite_1, self.rect.x, self.rect.y, 100, 100))
                        else:
                            sprite_list.append(spritemanager.SpriteData(self.stage_3_sprite_1, self.rect.x, self.rect.y, 100, 100))
                    elif frame == 1:
                        if self.facing_right:
                            sprite_list.append(spritemanager.SpriteData(self.stage_3_inverted_sprite_2, self.rect.x, self.rect.y, 100, 100))
                        else:
                            sprite_list.append(spritemanager.SpriteData(self.stage_3_sprite_2, self.rect.x, self.rect.y, 100, 100))
            elif self.stage == 4:
                if self.in_animation:
                    if self.animation == "walking":
                        if self.true_anim_frames == 0:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_4_inverted_walking_1, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_4_walking_1, self.rect.x, self.rect.y, 100, 100))
                        if self.true_anim_frames == 1:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_4_inverted_walking_2, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_4_walking_2, self.rect.x, self.rect.y, 100, 100))
                        if self.true_anim_frames == 2:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_4_inverted_walking_4, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_4_walking_4, self.rect.x, self.rect.y, 100, 100))
                        if self.true_anim_frames == 3:
                            if self.facing_right:
                                sprite_list.append(spritemanager.SpriteData(self.stage_4_inverted_sprite_2, self.rect.x, self.rect.y, 100, 100))
                            else:
                                sprite_list.append(spritemanager.SpriteData(self.stage_4_sprite_2, self.rect.x, self.rect.y, 100, 100))
                else:
                    if frame == 0:
                        if self.facing_right:
                            sprite_list.append(spritemanager.SpriteData(self.stage_4_inverted_sprite_1, self.rect.x, self.rect.y, 100, 100))
                        else:
                            sprite_list.append(spritemanager.SpriteData(self.stage_4_sprite_1, self.rect.x, self.rect.y, 100, 100))
                    elif frame == 1:
                        if self.facing_right:
                            sprite_list.append(spritemanager.SpriteData(self.stage_4_inverted_sprite_2, self.rect.x, self.rect.y, 100, 100))
                        else:
                            sprite_list.append(spritemanager.SpriteData(self.stage_4_sprite_2, self.rect.x, self.rect.y, 100, 100))
        else:
            sprite_list.append(spritemanager.SpriteData(self.dead_mel, self.rect.x, self.rect.y + 20, 100, 100))

class AngelMel():
    def __init__(self, catventurete):
        self.catventurete = catventurete
        self.wing_1 = pygame.image.load("Sprites/mels wings.png")
        self.wing_1 = pygame.transform.scale(self.wing_1, (172, 68))
        self.wing_2 = pygame.transform.flip(self.wing_1, True, False)
        self.aurora = pygame.image.load("Sprites/aurora.png")
        self.aurora = pygame.transform.scale(self.aurora, (75, 50))
        self.mel = pygame.image.load("Sprites/mel.png")
        self.mel = pygame.transform.scale(self.mel, (100, 100))
        self.flipped_mel = pygame.transform.flip(self.mel, True, False)
        self.angel_mel_animation_1_frame_1 = pygame.image.load("Sprites/angel mel animation 1 frame 1.png")
        self.angel_mel_animation_1_frame_1 = pygame.transform.scale(self.angel_mel_animation_1_frame_1, (100, 100))
        self.flipped_angel_mel_animation_1_frame_1 = pygame.transform.flip(self.angel_mel_animation_1_frame_1, True, False)
        self.angel_mel_animation_1_frame_2 = pygame.image.load("Sprites/angel mel animation 1 frame 2.png")
        self.angel_mel_animation_1_frame_2 = pygame.transform.scale(self.angel_mel_animation_1_frame_2, (100, 100))
        self.flipped_angel_mel_animation_1_frame_2 = pygame.transform.flip(self.angel_mel_animation_1_frame_2, True, False)
        self.angel_mel_animation_1_frame_3 = pygame.image.load("Sprites/angel mel animation 1 frame 3.png")
        self.angel_mel_animation_1_frame_3 = pygame.transform.scale(self.angel_mel_animation_1_frame_3, (100, 100))
        self.flipped_angel_mel_animation_1_frame_3 = pygame.transform.flip(self.angel_mel_animation_1_frame_3, True, False)       
        self.mel_looking_down = pygame.image.load("Sprites/mel looking down.png")
        self.mel_looking_down = pygame.transform.scale(self.mel_looking_down, (100, 100))       
        self.flipped_mel_looking_down = pygame.transform.flip(self.mel_looking_down, True, False)       
        self.mel_looking_up = pygame.image.load("Sprites/mel looking up.png")
        self.mel_looking_up = pygame.transform.scale(self.mel_looking_up, (100, 100))       
        self.flipped_mel_looking_up = pygame.transform.flip(self.mel_looking_up, True, False)
        self.mel_wings_frame_1 = pygame.image.load("Sprites/mels wings frame 1.png")
        self.mel_wings_frame_1 = pygame.transform.scale(self.mel_wings_frame_1, (172, 68))
        self.flipped_mel_wings_frame_1 = pygame.transform.flip(self.mel_wings_frame_1, True, False)
        self.mel_wings_frame_2 = pygame.image.load("Sprites/mels wings frame 2.png")
        self.mel_wings_frame_2 = pygame.transform.scale(self.mel_wings_frame_2, (172, 68))
        self.flipped_mel_wings_frame_2 = pygame.transform.flip(self.mel_wings_frame_2, True, False)
        self.mel_wings_frame_3 = pygame.image.load("Sprites/mels wings frame 3.png")
        self.mel_wings_frame_3 = pygame.transform.scale(self.mel_wings_frame_3, (172, 68))
        self.flipped_mel_wings_frame_3 = pygame.transform.flip(self.mel_wings_frame_3, True, False)
        self.mel_wings_frame_4 = pygame.image.load("Sprites/mels wings frame 4.png")
        self.mel_wings_frame_4 = pygame.transform.scale(self.mel_wings_frame_4, (172, 68))
        self.flipped_mel_wings_frame_4 = pygame.transform.flip(self.mel_wings_frame_4, True, False)
        self.mel_wings_expended = pygame.image.load("Sprites/mels wings expanded.png")
        self.mel_wings_expended = pygame.transform.scale(self.mel_wings_expended, (172, 68))
        self.flipped_mel_wings_expended = pygame.transform.flip(self.mel_wings_expended, True, False)
        self.mel_wings_unexpended = pygame.image.load("Sprites/mels wings unexpanded.png")
        self.mel_wings_unexpended = pygame.transform.scale(self.mel_wings_unexpended, (172, 68))
        self.flipped_mel_wings_unexpended = pygame.transform.flip(self.mel_wings_unexpended, True, False)
        
        self.wing_frames = [
            self.angel_mel_animation_1_frame_1,
            self.angel_mel_animation_1_frame_2,
            self.angel_mel_animation_1_frame_3,
        ]

        self.flipped_wing_frames = [
            self.flipped_angel_mel_animation_1_frame_1,
            self.flipped_angel_mel_animation_1_frame_2,
            self.flipped_angel_mel_animation_1_frame_3,
        ]

        
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.coliderect = pygame.Rect(0, 0, 80, 20)
        self.gravity = 0
        self.speed = 5
        self.facing_right = False
        self.seconds_pressing_jump = 0
        self.last_key = pygame.key.get_pressed()
        self.fall_speed = 1
        self.fall_cap = 3
        self.looking_up = False
        self.looking_down = False
        self.halo_time = 0
        self.halo_base_y = -45
        self.halo_float_strength = 6
        self.halo_pulse_strength = 6
        self.wing_anim_time = 0
        self.gravity = 0.35   # NEVER touch this again
        self.vy = 0.0
        self.max_fall = 6
        self.can_move = True
        self.past_can_move = self.can_move
        
    def update(self):
        self.key = self.catventurete.key
        self.coliderect.x = self.rect.x + 10 
        self.coliderect.y = self.rect.y + 70

        for _object in self.catventurete.current_room:
            if self.coliderect.colliderect(_object.rect):
                if _object.type == "spike":
                    self.catventurete.reset_room()
                    break
                elif _object.type == "coin":
                    self.catventurete.coins += 1
                    self.catventurete.current_room.remove(_object)
                    if self.catventurete.coins >= 3:
                        self.catventurete.advance_room()
                elif _object.type == "fake coin":
                    self.catventurete.current_room.remove(_object)

        #if self.gravity > 70:
        #    self.gravity = 10
        #if self.gravity < -10:
        #    self.gravity = -10
        #if -1 < self.vy < 1:
        #    self.vy *= 0.92

        if self.can_move:
            # choose gravity
            if self.key[pygame.K_DOWN]:
                g = self.gravity * 3
                max_fall = self.max_fall * 2
            else:
                g = self.gravity
                max_fall = self.max_fall
        else:
            g = self.gravity
            max_fall = self.max_fall
        

        # apply gravity
        self.vy += g

        # terminal velocity
        self.vy = max(min(self.vy, max_fall), -12)

        # wing glide (only when NOT diving)
        if not self.key[pygame.K_DOWN] and self.vy > 0:
            self.vy *= 0.97

        # move
        self.rect.y += self.vy

        if self.can_move:
            
            if self.vy > 4:
                self.looking_down = True
                self.looking_up = False
            elif self.vy < -2:
                self.looking_up = True
                self.looking_down = False
            else:
                self.looking_up = False
                self.looking_down = False

            if self.key[pygame.K_UP] or self.key[pygame.K_SPACE]:
                self.seconds_pressing_jump += 1
                self.vy -= 0.38   # gentle lift while holding
            else:
                self.wing_anim_time = max(self.wing_anim_time - 2, 0)
            if (self.last_key[pygame.K_UP] and not self.key[pygame.K_UP]) or (self.last_key[pygame.K_SPACE] and not self.key[pygame.K_SPACE]):
                jump_power = min(self.seconds_pressing_jump / 1.2, 40)
                self.vy = -jump_power
                self.seconds_pressing_jump = 0
        if (not self.can_move and self.past_can_move):
            jump_power = min(self.seconds_pressing_jump / 1.2, 40)
            self.vy = -jump_power
            self.seconds_pressing_jump = 0
        if self.can_move:
            
            if self.catventurete.key[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.facing_right = True
            if self.catventurete.key[pygame.K_LEFT]:
                self.rect.x -= self.speed
                self.facing_right = False


    
        self.halo_time += 0.08

        halo_y_offset = self.halo_base_y + math.sin(self.halo_time) * self.halo_float_strength
        halo_pulse = 1 + math.sin(self.halo_time * 1.5) * 0.05

        halo_size = int(50 * halo_pulse)

        halo = pygame.transform.scale(self.aurora, (halo_size, halo_size - 15))

        if self.facing_right:
            halo_x = self.rect.x + 35
        else:
            halo_x = self.rect.x + 20

        self.catventurete.sprites.append(
            spritemanager.SpriteData(
                halo,
                halo_x,
                self.rect.y + halo_y_offset,
                halo_size,
                halo_size
            )
        )
        if self.seconds_pressing_jump == 0:
            if self.vy > -4 and self.vy < 4:
                self.catventurete.sprites.append(spritemanager.SpriteData(self.wing_1, self.rect.x - 150, self.rect.y + 20, 172, 68))
                self.catventurete.sprites.append(spritemanager.SpriteData(self.wing_2, self.rect.x + 50, self.rect.y + 20, 172, 68))
            elif self.vy < -4 and self.vy < 4:
                self.catventurete.sprites.append(spritemanager.SpriteData(self.mel_wings_expended, self.rect.x - 150, self.rect.y + 20, 172, 68))
                self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_mel_wings_expended, self.rect.x + 50, self.rect.y + 20, 172, 68))
            elif self.vy > 4:
                self.catventurete.sprites.append(spritemanager.SpriteData(self.mel_wings_unexpended, self.rect.x - 150, self.rect.y + 20, 172, 68))
                self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_mel_wings_unexpended, self.rect.x + 50, self.rect.y + 20, 172, 68))
            if not self.looking_down and not self.looking_up:
                if self.facing_right:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_mel, self.rect.x, self.rect.y, 100, 100))
                else:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.mel, self.rect.x, self.rect.y, 100, 100))
            elif self.looking_down:
                if self.facing_right:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_mel_looking_down, self.rect.x, self.rect.y, 100, 100))
                else:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.mel_looking_down, self.rect.x, self.rect.y, 100, 100))
            elif self.looking_up:
                if self.facing_right:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_mel_looking_up, self.rect.x, self.rect.y, 100, 100))
                else:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.mel_looking_up, self.rect.x, self.rect.y, 100, 100))
        else:
            if self.seconds_pressing_jump // 30 == 0:
                self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_mel_wings_frame_1, self.rect.x + 50, self.rect.y + 20, 172, 68))
                self.catventurete.sprites.append(spritemanager.SpriteData(self.mel_wings_frame_1, self.rect.x - 150, self.rect.y + 20, 172, 68))
                if self.facing_right:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_angel_mel_animation_1_frame_1, self.rect.x, self.rect.y, 100, 100))
                else:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.angel_mel_animation_1_frame_1, self.rect.x, self.rect.y, 100, 100))
            elif self.seconds_pressing_jump // 30 == 1:
                self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_mel_wings_frame_2, self.rect.x + 50, self.rect.y + 20, 172, 68))
                self.catventurete.sprites.append(spritemanager.SpriteData(self.mel_wings_frame_2, self.rect.x - 150, self.rect.y + 20, 172, 68))
                if self.facing_right:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_angel_mel_animation_1_frame_2, self.rect.x, self.rect.y, 100, 100))
                else:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.angel_mel_animation_1_frame_2, self.rect.x, self.rect.y, 100, 100))
            elif self.seconds_pressing_jump // 30 >= 2:
                self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_mel_wings_frame_3, self.rect.x + 50, self.rect.y + 20, 172, 68))
                self.catventurete.sprites.append(spritemanager.SpriteData(self.mel_wings_frame_3, self.rect.x - 150, self.rect.y + 20, 172, 68))
                if self.facing_right:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.flipped_angel_mel_animation_1_frame_3, self.rect.x, self.rect.y, 100, 100))
                else:
                    self.catventurete.sprites.append(spritemanager.SpriteData(self.angel_mel_animation_1_frame_3, self.rect.x, self.rect.y, 100, 100))
            
#            frame_index = min(self.wing_anim_time // 15, 2)

#            if self.facing_right:
#                wing_sprite = self.flipped_wing_frames[frame_index]
#            else:
#                wing_sprite = self.wing_frames[frame_index]

            #self.catventurete.sprites.append(
            #    spritemanager.SpriteData(
            #        wing_sprite,
            #        self.rect.x,
            #        self.rect.y,
            #        100,
            #        100
            #    )
            #)


        
        
        self.last_key = self.key
        self.past_can_move = self.can_move
