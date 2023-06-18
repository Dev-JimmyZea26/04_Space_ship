import pygame as pg
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    HALFT_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALFT_SCREEN_WIDTH = SCREEN_WIDTH // 2
    
    def __init__(self, screen):
        screen.fill((255, 255, 255))
        self.font = pg.font.Font(FONT_STYLE, 30)
        
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
    
    def draw(self, screen, message, x = HALFT_SCREEN_WIDTH, y = HALFT_SCREEN_HEIGHT, color = (0, 0, 0)):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)
        
    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))