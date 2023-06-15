from game.components.enemies.enemy import Enemy
import random

class EnemyManager:
    def __init__(self):
        self.enemies = []
        
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            
    def add_enemy(self):
        enemy_type = random.randint(1, 4)
        if enemy_type == 1:
            enemy = Enemy()
        else:
            speed_x = 5 + enemy_type
            speed_y = 1 + (enemy_type - 1)
            mov_x_for = [50 + (enemy_type - 2) * 50, 100 + (enemy_type - 2) * 100]
            enemy = Enemy(enemy_type, speed_x, speed_y, mov_x_for)
            
        if len(self.enemies) < 1:
            self.enemies.append(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)