import pygame as pg
from pygame import mixer
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, LOBBY_SOUND
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.counter import Counter
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.display.set_icon(ICON)
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.running = False
        self.menu = Menu(self.screen)
        self.power_up_manager = PowerUpManager()
        self.stop_time = False
        
    def execute(self):
        mixer.Sound.play(LOBBY_SOUND)
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pg.display.quit()
        pg.quit()
        
    def run(self):
        self.reset()
        self.playing = True
        while self.playing:
            mixer.Sound.stop(LOBBY_SOUND)
            self.events()
            self.update()
            self.draw()
        else:
            mixer.Sound.play(LOBBY_SOUND)
        
    def reset(self):
        self.enemy_manager.reset()
        self.score.reset()
        self.player.reset()
        self.bullet_manager.reset()
        self.power_up_manager.reset()
        
    # Events
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                
    # Update
    def update(self):
        user_input = pg.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
    
    # Draw
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pg.display.update()
        pg.display.flip()
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pg.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.menu.draw(self.screen, f'{self.player.power_up_type.capitalize()} is enabled for: {time_to_show} in seconds', 500, 50, size=23)
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.stop_time = False
                self.player.set_image()
        
    def draw_background(self):
        image = pg.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
        
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count.count == 0:
            self.menu.draw(self.screen, 'Welcome to the Space Invaders', half_screen_width, 50)
            self.menu.draw(self.screen, 'Press any key to start...', half_screen_width, half_screen_height + 30, True)
        else:
            self.update_highes_score()
            color = (255, 255, 255)
            self.menu.draw(self.screen, f'Game Over. Press any key to restart.', y=50 ,palpitating=True)
            self.menu.draw(self.screen, f'Your score: {self.score.count}', half_screen_width, 330, color=color)
            self.menu.draw(self.screen, f'Highest score: {self.highest_score.count}', half_screen_width, 365, color=color)
            self.menu.draw(self.screen, f'Total deaths: {self.death_count.count}', half_screen_width, 395, color=color)

        self.menu.update(self)
        
    def update_highes_score(self):
        self.highest_score.set_count(self.score.count if self.score.count > self.highest_score.count else self.highest_score.count)