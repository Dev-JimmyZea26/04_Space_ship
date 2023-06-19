from game.components.enemies.enemy import Enemy
from game.utils.constants import EXPLOSION_SOUND
import pygame as pg
from pygame import mixer
import random

class EnemyManager:
    def __init__(self):
        self.enemies = []
        
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            
        self.enemy_collide_player(game, game.player)
            
    def add_enemy(self):
        enemy_type = random.randint(1, 4)
        if enemy_type == 1:
            enemy = Enemy()
        else:
            speed_bullet = 20 + (enemy_type - 1) * 5
            speed_x = 5 + enemy_type
            speed_y = 1
            mov_x_for = [50 + (enemy_type - 2) * 50, 100 + (enemy_type - 2) * 100]
            enemy = Enemy(enemy_type, speed_x, speed_y, mov_x_for, speed_bullet, enemy_type)
            
        if len(self.enemies) < 2:
            self.enemies.append(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def reset(self):
        self.enemies = []
        
    def enemy_collide_player(self, game, player):
        for enemy in self.enemies:
            if enemy.rect.colliderect(player.rect):
                mixer.Sound.play(EXPLOSION_SOUND)
                player.life -= 1
                pg.time.delay(1000)
                self.enemies.remove(enemy)
                if player.life == 0:
                    game.playing = False
                    game.game_over = True
                    game.death_count.update()
                game.player.reset()
                game.enemy_manager.reset()
                self.reset()