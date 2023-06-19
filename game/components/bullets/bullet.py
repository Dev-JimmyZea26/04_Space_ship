import pygame as pg
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT

class Bullet(Sprite):
    X_POS = 80
    Y_POS = 310
    BULLET_SIZE = pg.transform.scale(BULLET, (15, 40))
    BULLET_ENEMY_SIZE = pg.transform.scale(BULLET_ENEMY, (9, 32))
    BULLETS = {
        'player': BULLET_SIZE,
        'enemy': BULLET_ENEMY_SIZE
    }
    
    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type
        self.speed_bullet = spaceship.speed_bullet
        
    def events(self):
        pass
    
    def update(self, bullets, stop_time = False):
        if self.owner == 'enemy':
            self.rect.y += self.speed_bullet if not stop_time else 0
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
        else:
            self.rect.y -= self.speed_bullet
            if self.rect.y <= 0:
                bullets.remove(self)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        