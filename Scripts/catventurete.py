import pygame
import spritemanager
import mel
import button
import objects

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
        self.room = 0

        self.mel = mel.Mel(self)
        self.grass = pygame.image.load("Sprites/grass.png")
        self.grass = pygame.transform.scale(self.grass, (128, 128))
        self.coins = 0
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
            objects.SnakeX(700, 350),
            objects.SnakeY(400, 50)
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
            objects.SnakeX(550, 0),
            objects.SnakeY(400, 50),
        ]
        self.room_6 = [
            objects.Spike(525, 550),
            objects.Spike(150, 550),
            objects.Spike(350, 100),
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
        self.coin_room_list = [
            self.coin_room_1,
            self.coin_room_2,
            self.coin_room_3,
            self.coin_room_4,
            self.coin_room_5,
            self.coin_room_6,
        ]
        self.room_list = [
            self.room_1,
            self.room_2,
            self.room_3,
            self.room_4,
            self.room_5,
            self.room_6,
        ]
        self.mel_location_1 = (400, 400)
        self.mel_location_2 = (400, 400)
        self.mel_location_3 = (400, 400)
        self.mel_location_4 = (400, 400)
        self.mel_location_5 = (400, 400)
        self.mel_location_6 = (400, 400)
        self.mel_location_list = [
            self.mel_location_1,
            self.mel_location_2,
            self.mel_location_3,
            self.mel_location_4,
            self.mel_location_5,
            self.mel_location_6,
        ]
        
        self.pressing_right = False
        self.pressing_up = False
        self.pressing_down = False
        self.pressing_left = False

        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)

    def reset_room(self):
        self.mel.rect.x = self.current_mel_location_room[0]
        self.mel.rect.y = self.current_mel_location_room[1]
        self.mel.facing_right = False
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
        
        self.current_room = self.room_list[self.room - 1]
        self.current_mel_location_room = self.mel_location_list[self.room - 1]
        self.current_coin_room = self.coin_room_list[self.room - 1]
        self.coins = 0

        self.mel.rect.x = self.current_mel_location_room[0]
        self.mel.rect.y = self.current_mel_location_room[1]

        for coin in self.current_coin_room:
            self.current_room.append(coin)

    def update(self):
        self.event_handling()
        if self.room > 0:
            self.screen.fill("cadetblue1")
        else:
            self.screen.fill("black")

        self.sprites = []

        self.key = pygame.key.get_pressed()

        self.current_room = self.room_list[self.room - 1]
        self.current_mel_location_room = self.mel_location_list[self.room - 1]
        self.current_coin_room = self.coin_room_list[self.room - 1]


        if self.room > 0:
            for x in range(0, 30):
                for y in range(0, 30):
                    self.screen.blit(self.grass, (x * 128, y * 128))
            self.mel.update(self.screen, self.sprites, self.key, self.current_room)
            for _object in self.current_room:
                _object.update(self.sprites)
        else:
            self.button.update(pygame.mouse.get_pos(), self.screen, self.room, pygame.mouse.get_pressed(), catventure)

        spritemanager.update_sprite_list(self.sprites, self.offset_x, self.offset_y, 800, 800, self.screen)

        pygame.display.update()
        self.clock.tick(60)

catventure = Catventure()
while catventure.running:
    catventure.update()
