from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMIES
import time
import random

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy_index = 0  # Índice de la imagen actual en la lista ENEMIES
        self.enemy_quantity = random.randint(1, 3) # Cantidad de enemigos que se van a crear por cada elemento de la lista ENEMIES
        self.time_since_last_enemy = time.time()  # Tiempo transcurrido desde la creación del último enemigo

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def add_enemy(self):
        current_time = time.time()  # Obtener el tiempo actual en segundos
        if len(self.enemies) == 0: # Crear un enemigo antes de que pasen los primeros 5 segundos
            self.enemies.append(Enemy(ENEMIES[self.enemy_index]))
            self.enemy_quantity -= 1
            self.time_since_last_enemy = current_time
        
        if current_time - self.time_since_last_enemy >= 5.0:  # Pasaron 5 segundos desde la creación del último enemigo
            if self.enemy_index < len(ENEMIES) and self.enemy_quantity > 0:
                self.enemies.append(Enemy(ENEMIES[self.enemy_index]))
                self.enemy_quantity -= 1
                self.time_since_last_enemy = current_time
            elif self.enemy_quantity == 0:
                self.enemy_index += 1
                self.enemy_quantity = random.randint(1, 3)
            else:
                self.time_since_last_enemy = current_time
                self.enemy_quantity = random.randint(1, 3)
                self.enemy_index = 0

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)