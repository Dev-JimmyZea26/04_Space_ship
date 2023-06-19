import pygame as pg
from pygame import mixer
from game.utils.constants import SHIELD_TYPE, EXPLOSION_SOUND, SHOOT_SOUND, SHOOT_SOUND_ENEMY, SHIELD_IMPACT_SOUND

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets, game.stop_time)
            if bullet.rect.colliderect(game.player.rect.inflate(-5, -50)) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    mixer.Sound.play(EXPLOSION_SOUND)
                    game.player.life -= 1
                    pg.time.delay(1000)
                    if game.player.life == 0:
                        game.playing = False
                        game.game_over = True
                        game.death_count.update()
                    game.player.reset()
                    game.enemy_manager.reset()
                    self.reset()
                else:
                    mixer.Sound.play(SHIELD_IMPACT_SOUND)
                break
            
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.score.update()
                    break
        
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.owner == 'enemy':
            mixer.Sound.play(SHOOT_SOUND_ENEMY)
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.bullets) < 1:
            mixer.Sound.play(SHOOT_SOUND)
            self.bullets.append(bullet)
            
    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
        