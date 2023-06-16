import pygame as pg
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    HALFT_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALFT_SCREEN_WIDTH = SCREEN_WIDTH // 2
    
    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pg.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALFT_SCREEN_WIDTH, self.HALFT_SCREEN_HEIGHT)
        
    def handle_events_on_menu(self, game):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game.running = False
                game.playing = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game.running = False
                else:
                    game.run()
        
    def update(self, game):
        pg.display.update() # actualizar componentes de la pantalla
        self.handle_events_on_menu(game)
    
    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        
    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALFT_SCREEN_WIDTH, self.HALFT_SCREEN_HEIGHT)
        
    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))