import pygame
from pygame import mixer
import os

pygame.mixer.init()
# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

STOP_TIME = pygame.image.load(os.path.join(IMG_DIR, 'Other/stop_time.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/back.jpg'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
STOP_TIME_TYPE = 'stop time'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))

ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))

FONT_STYLE = 'freesansbold.ttf'

EXPLOSION_SOUND = mixer.Sound(os.path.join(IMG_DIR, 'Sounds/explosion.wav'))
SHOOT_SOUND = mixer.Sound(os.path.join(IMG_DIR, 'Sounds/shoot.wav'))
SHOOT_SOUND_ENEMY = mixer.Sound(os.path.join(IMG_DIR, 'Sounds/shoot_enemy.wav'))
LOBBY_SOUND = mixer.Sound(os.path.join(IMG_DIR, 'Sounds/lobby.wav'))
GAME_OVER_SOUND = mixer.Sound(os.path.join(IMG_DIR, 'Sounds/game_over.wav'))
SHIELD_IMPACT_SOUND = mixer.Sound(os.path.join(IMG_DIR, 'Sounds/shield_impact.wav'))

KEBOARD_ARROWS = pygame.image.load(os.path.join(IMG_DIR, 'Other/keyboard_arrows.png'))
SPACE_BAR = pygame.image.load(os.path.join(IMG_DIR, 'Other/spacebar.png'))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/game_over.jpg'))