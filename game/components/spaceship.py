import pygame as pg
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = SCREEN_HEIGHT - 100
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pg.transform.scale(self.image, (30, 70))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.speed_bullet = 35
        self.has_power_up = False
        self.power_up_time = 0
        self.power_up_type = DEFAULT_TYPE
        self.life = 3
        
    # Events   
    def move_left(self):
        self.rect.x -= 10
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - 40

    def move_right(self):
        self.rect.x += 10
        if self.rect.right >= SCREEN_WIDTH - 60:
            self.rect.x = 0
    
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += 10

    def update(self, user_input, game):
        if user_input[pg.K_LEFT]:
            self.move_left()
        if user_input[pg.K_RIGHT]:
            self.move_right()
        if user_input[pg.K_UP]:
            self.move_up()
        if user_input[pg.K_DOWN]:
            self.move_down()
        if user_input[pg.K_SPACE]:
            self.shoot(game.bullet_manager)
            
    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.set_image()
        if self.life == 0:
            self.life = 3
        
    def set_image(self, size=(30, 70), image=SPACESHIP):
        self.image = image
        self.image = pg.transform.scale(self.image, size)
