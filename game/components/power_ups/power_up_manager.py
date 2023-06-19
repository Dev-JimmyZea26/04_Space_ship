import pygame as pg
import random
from game.components.power_ups.shield import Shield
from game.components.power_ups.stop_time import StopTime
from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE, STOP_TIME_TYPE

class PowerUpManager:
    
    POWERS = {
        1: Shield,
        2: StopTime
    }
    
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3, 5)
        self.power_up_index = 0
    
    def generate_power_up(self):
        self.power_up_index = random.randint(1, 2)
        power_up = self.POWERS[self.power_up_index]()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)
        
    def update(self, game):
        current_time = pg.time.get_ticks()
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
            
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up.rect):
                self.power_up_action(game)
                power_up.start_time = pg.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)
                break
            
    def power_up_action(self, game):
        if self.power_up_index == 1:
            game.player.power_up_type = SHIELD_TYPE
            game.player.set_image((40, 80), SPACESHIP_SHIELD)
        elif self.power_up_index == 2:
            game.player.power_up_type = STOP_TIME_TYPE
            game.stop_time = True
        
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset(self):
        now = pg.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)