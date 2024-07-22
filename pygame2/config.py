import pygame 

LARGURA_TELA = 1280
ALTURA_TELA = 720
TITULO_JOGO = 'Magocinho'
TILESIZE = 64
TILESIZE_PLAYER = 60
FPS = 60
VELOCIDADE_JOGADOR = 5
#CAMADAS

GROUND_LAYER    = 1
PLAYER_LAYER    = 2

TIMER_DELAY_POCAO = 2000
TIMER_DELAY_COGUMELO = 2000

TIMER_POCAO = pygame.USEREVENT+1
TIMER_COGUMELO = pygame.USEREVENT+2

tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B.............c....B',
    'B..................B',
    'B...c.........p....B',
    'B..................B',
    'B..................B',
    'B..BBBB.....B.B.B..B',
    'B.....B.....B.B.B..B',
    'B.....BBBBB.BBB.B..B',
    'B......p...........B',
    'BBBBBBBBBBBBBBBBBBBB'
]