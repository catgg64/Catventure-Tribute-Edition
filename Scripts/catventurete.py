import pygame
import spritemanager
import mel
import button
import objects
import math
import time
pygame.init()

class Catventure:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800), pygame.DOUBLEBUF, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Catventure: Tribute Edition")
        self.running = True  
        self.sprites = []
        self.offset_x = 0
        self.offset_y = 0
        
        self.room = 0

        self.mel = mel.Mel(self)
        self.angel_mel = mel.AngelMel(self)

        self.grass = pygame.image.load("Sprites/grass.png")
        self.my_font = pygame.font.Font('HelvetiPixel.ttf', 30)
        self.sky_background = pygame.image.load("Sprites/sky background.png")
        self.grass = pygame.transform.scale(self.grass, (128, 128))
        self.coins = 0
        self.time_since_thing = 0
        self.just_finished_thing = False
        self.button = button.StartButton()
        self.room_1 = [
            objects.Spike(180, 580),
            objects.Spike(180, 430),
            objects.MovingSpike(300, 120),
            objects.MovingSpike(520, 110),
        ]
        self.room_2 = [
            objects.Spike(440, 280),
            objects.Spike(270, 280),
            objects.Spike(550, 160),
            objects.Spike(140, 160),
            objects.MovingSpike(650, 600),
            objects.MovingSpike(0, 600),
        ]
        self.room_3 = [
            objects.Spike(500, 600),
            objects.Spike(500, 450),
            objects.Spike(150, 450),
            objects.Spike(150, 600),
            objects.Spike(450, 150),
            objects.Spike(250, 150),
            objects.MovingSpike(450, 150),
            objects.MovingSpike(250, 150),
        ]
        self.room_4 = [
            objects.Spike(300, 620),
            objects.Spike(500, 450),
            objects.Spike(150, 450),
            objects.Spike(150, 600),
            objects.Spike(500, 600),
            objects.Spike(350, 250),
            objects.MovingSpike(650, 150),
            objects.MovingSpike(0, 150),
            objects.SnakeX(50, 350),
        ]
        self.room_5 = [
            objects.Spike(150, 50),
            objects.Spike(150, 200),
            objects.Spike(500, 200),
            objects.Spike(500, 50),
            objects.Spike(325, 250),
            objects.MovingSpike(650, 150),
            objects.MovingSpike(0, 150),
            objects.SnakeX(250, 0),
            objects.SnakeY(400, 50),
        ]
        self.room_6 = [
            objects.Spike(525, 550),
            objects.Spike(150, 550),
            objects.Spike(350, 100),
        ]
        self.room_7 = [    
        ]
        self.room_8 = [
            objects.Spike(450, 550),
            objects.Spike(150, 50),
            objects.Spike(450, 50),
            objects.Spike(150, 550),
            objects.Spike(300, 550),
            objects.Spike(300, 50),
        ]
        self.room_9 = [
            objects.Spike(650, 450),
            objects.Spike(300, 450),
            objects.Spike(0, 450),
            objects.Spike(650, 300),
            objects.Spike(300, 300),
            objects.Spike(0, 300),
        ]
        self.room_10 = [
            objects.Spike(650, 450),
            objects.Spike(325, 450),
            objects.Spike(0, 450),
            objects.Spike(450, 0),
            objects.Spike(325, 300),
            objects.Spike(300, 0)
        ]
        self.room_11 = [
            objects.Spike(525, 550),
            objects.Spike(150, 550),
            objects.Spike(350, 100),
        ]
        self.room_12 = [
        ]
        self.coin_room_1 = [
            objects.Coin(60, 520),
            objects.Coin(700, 20),
            objects.Coin(350, 50),
        ]
        self.coin_room_2 = [
            objects.Coin(50, 650),
            objects.Coin(400, 175),
            objects.Coin(650, 650),
        ]
        self.coin_room_3 = [
            objects.Coin(25, 450),
            objects.Coin(700, 450),
            objects.Coin(350, 50),
        ]
        self.coin_room_4 = [
            objects.Coin(50, 650),
            objects.Coin(400, 50),
            objects.Coin(700, 650),
        ]
        self.coin_room_5 = [
            objects.Coin(450, 100),
            objects.Coin(400, 50),
            objects.Coin(350, 100),
        ]
        self.coin_room_6 = [
            objects.Coin(0, 700),
            objects.Coin(700, 700),
            objects.Coin(375, 0)
        ]
        self.coin_room_7 = [
            objects.Coin(650, 350)
        ]
        self.coin_room_8 = [
            objects.Coin(500, 350),
            objects.Coin(350, 350),
            objects.Coin(200, 350),
        ]
        self.coin_room_9 = [
            objects.Coin(500, 350),
            objects.Coin(350, 200),
            objects.Coin(200, 350),
        ]
        self.coin_room_10 = [
            objects.Coin(500, 350),
            objects.Coin(375, 200),
            objects.Coin(225, 350)
        ]
        self.coin_room_11 = [
            objects.Coin(0, 700),
            objects.Coin(700, 700),
            objects.Coin(375, 0)    
        ]
        self.coin_room_12 = [
            objects.Coin(350, 50),
            objects.Coin(350, -5000),
            objects.FakeCoin(350, -7000),
            objects.FakeCoin(350, -9000),
            objects.FakeCoin(350, -11000),
            objects.FakeCoin(350, -13000),
            objects.FakeCoin(350, -15000),
        ]
        self.coin_room_list = [
            self.coin_room_1,
            self.coin_room_2,
            self.coin_room_3,
            self.coin_room_4,
            self.coin_room_5,
            self.coin_room_6,
            self.coin_room_7,
            self.coin_room_8,
            self.coin_room_9,
            self.coin_room_10,
            self.coin_room_11,
            self.coin_room_12,
        ]
        self.room_list = [
            self.room_1,
            self.room_2,
            self.room_3,
            self.room_4,
            self.room_5,
            self.room_6,
            self.room_7,
            self.room_8,
            self.room_9,
            self.room_10,
            self.room_11,
            self.room_12,
        ]
        self.mel_location_1 = (400, 400)
        self.mel_location_2 = (400, 400)
        self.mel_location_3 = (400, 400)
        self.mel_location_4 = (400, 400)
        self.mel_location_5 = (400, 400)
        self.mel_location_6 = (400, 400)
        self.mel_location_7 = (50, 350)
        self.mel_location_8 = (0, 0)
        self.mel_location_9 = (375, 0)
        self.mel_location_10 = (375, 750)
        self.mel_location_11 = (400, 400)
        self.mel_location_12 = (375, 750)
        self.mel_location_list = [
            self.mel_location_1,
            self.mel_location_2,
            self.mel_location_3,
            self.mel_location_4,
            self.mel_location_5,
            self.mel_location_6,
            self.mel_location_7,
            self.mel_location_8,
            self.mel_location_9,
            self.mel_location_10,
            self.mel_location_11,
            self.mel_location_12,
        ]
        
        self.pressing_right = False
        self.pressing_up = False
        self.pressing_down = False
        self.pressing_left = False
        self.fade_surface = pygame.Surface((800, 800), pygame.SRCALPHA)
        self.doing_the_fadeout = False
        self.text_appearing = False
        self.text_fade = 0

        self.distance = self.angel_mel.rect.y * -1 + 800

        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)

    def reset_room(self):
        if self.room < 8:
            self.mel.rect.x = self.current_mel_location_room[0]
            self.mel.rect.y = self.current_mel_location_room[1]
            self.mel.facing_right = False
        else:
            self.angel_mel.rect.x = self.current_mel_location_room[0]
            self.angel_mel.rect.y = self.current_mel_location_room[1]
            self.angel_mel.facing_right = False
        self.coins = 0

        for _object in self.current_room:
            _object.reset()
        
        for coin in self.current_coin_room:
            if not coin in self.current_room:
                self.current_room.append(coin)

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

    def advance_room(self):
        self.room += 1
        
        if self.room < 14:
            self.current_room = self.room_list[self.room - 1]
            self.current_mel_location_room = self.mel_location_list[self.room - 1]
            self.current_coin_room = self.coin_room_list[self.room - 1]
        self.coins = 0

        if self.room < 8:
            self.mel.rect.x = self.current_mel_location_room[0]
            self.mel.rect.y = self.current_mel_location_room[1]
        else:
            self.angel_mel.rect.x = self.current_mel_location_room[0]
            self.angel_mel.rect.y = self.current_mel_location_room[1]

        for coin in self.current_coin_room:
            self.current_room.append(coin)

        if self.room == 4:
            self.mel.stage = 2
            self.mel.speed = 12
            self.mel.mov_pauses = 3
            self.anim_speed = 16
        if self.room == 5:
            self.mel.stage = 3 
            self.mel.speed = 20 
            self.mel.mov_pauses = 5
            self.anim_speed = 20
        if self.room == 6:
            self.mel.stage = 4 
            self.mel.speed = 50 
            self.mel.mov_pauses = 50
            self.anim_speed = 60

    def update(self):
        self.event_handling()
        if self.room > 0 and self.room < 8:
            self.screen.fill("cadetblue1")
        elif self.room == 0:
            self.screen.fill("black")
        elif self.room >= 8 and self.room < 12:
            self.screen.fill((94, 157, 228))
        else:
            self.screen.fill((max(min(94 - self.distance / 100, 255), 0), max(min(157 - self.distance / 100, 255), 0), max(min(228 - self.distance / 100, 255), 0)))

        self.sprites = []

        self.key = pygame.key.get_pressed()

        if self.room < 13:
            self.current_room = self.room_list[self.room - 1]
            self.current_mel_location_room = self.mel_location_list[self.room - 1]
            self.current_coin_room = self.coin_room_list[self.room - 1]


        if self.room > 0 and self.room < 8:
            for x in range(0, 30):
                for y in range(0, 30):
                    self.screen.blit(self.grass, (x * 128, y * 128))
            self.mel.update(self.screen, self.sprites, self.key, self.current_room)
            for _object in self.current_room:
                _object.update(self.sprites)
        elif self.room < 8:
            self.button.update(pygame.mouse.get_pos(), self.screen, self.room, pygame.mouse.get_pressed(), catventure)
        elif self.room >= 8:
            if self.room == 12:
                true_offset = self.angel_mel.rect.y - 375 
                if true_offset > 0:
                    true_offset = 0
                true_offset /= 1
                self.offset_y = true_offset
                self.distance = self.angel_mel.rect.y * -1 + 800
                self.doing_thing = False

                self.finished_doing_the_fadeout = False
                if self.distance >= 2000:
                    self.doing_thing = True
                    self.angel_mel.facing_right = True
                if self.doing_thing:
                    self.angel_mel.can_move = False
                    self.angel_mel.vy -= 2
                    if self.angel_mel.rect.x > 350:
                        self.angel_mel.rect.x -= 1
                    if self.angel_mel.rect.x < 350:
                        self.angel_mel.rect.x += 1
                        
                if self.distance >= 10000 and self.distance <= 10100:
                    self.doing_the_fadeout = True
                    self.time_since_fadeout = 0
                    self.finished_doing_the_fadeout = False
                    self.time_since_fadeout_ended = 0
                if self.doing_the_fadeout:
                    self.time_since_fadeout += 1
                    if self.time_since_fadeout == 255:
                        self.finished_doing_the_fadeout = True
                        self.time_since_fadeout_ended += 1 
                if self.distance >= 16000 and not self.text_appearing:
                    self.fade_surface = pygame.Surface((800, 800), pygame.SRCALPHA)
                    self.text_surface = self.my_font.render('Wherever you are, Rest in Peace, Mel.', False, (255, 255, 255))
                    self.text_rect = self.text_surface.get_rect(center=(400, 400))
                    self.text_appearing = True
            
            self.screen.blit(self.sky_background, (0, 150 - self.offset_y / 2))
            for _object in self.current_room:
                _object.update(self.sprites)
            self.angel_mel.update()
        

        spritemanager.update_sprite_list(self.sprites, self.offset_x, self.offset_y, 800, 800, self.screen)
        
        if self.room == 12:
            if self.doing_the_fadeout:
                self.fade_surface.fill((0, 0, 0, min(self.time_since_fadeout / 2, 255)))
                self.screen.blit(self.fade_surface, (0, 0))
        if self.text_appearing:
            self.text_fade = min(self.text_fade + 1, 255)

            float_y = 400 + math.sin(pygame.time.get_ticks() / 400) * 3
            self.text_rect.center = (400, float_y)

            self.text_surface.set_alpha(self.text_fade)
            self.screen.blit(self.text_surface, self.text_rect)

        if self.mel.over:
            self.fade_surface.fill((0, 0, 0, self.mel.true_darkness))
            self.screen.blit(self.fade_surface, (0, 0))
            
            if self.mel.darkness == 1000:
                self.mel.over = False
                self.just_finished_thing = True
                self.mel.darkness = 0
                self.advance_room()
                
        if self.just_finished_thing:
            self.time_since_thing += 1
            self.fade_surface.fill((0, 0, 0, max(255 - self.time_since_thing, 0)))
            self.screen.blit(self.fade_surface, (0, 0))
            if self.time_since_thing == 255:
                self.just_finished_thing = False


        pygame.display.update()
        self.clock.tick(60)

catventure = Catventure()
while catventure.running:
    catventure.update()
