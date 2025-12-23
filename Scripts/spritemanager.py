class SpriteData():
    def __init__(self, surface, pos_x, pos_y, size_x, size_y):
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y

def update_sprite_list(list, offset_x, offset_y, window_size_x, window_size_y, surface):
    for sprite in list:
        if sprite.pos_x - offset_x < window_size_x and sprite.pos_y - offset_y < window_size_y and sprite.pos_x + sprite.size_x - offset_x > 0 and sprite.pos_y + sprite.size_y - offset_y > 0:
            surface.blit(sprite.surface, (sprite.pos_x - offset_x, sprite.pos_y - offset_y))

