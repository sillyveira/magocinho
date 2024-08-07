import pygame 
#configurações do jogo
LARGURA_TELA = 1280
ALTURA_TELA = 720
TITULO_JOGO = 'Magocinho'
TILESIZE = 64
TILESIZE_PLAYER = 60
FPS = 60
VELOCIDADE_JOGADOR = 3
VELOCIDADE_INIMIGO = 3
#CAMADAS

GROUND_LAYER    = 1
PLAYER_LAYER    = 2

ESQUERDA = 0
DIREITA = 1
BAIXO = 2
CIMA = -2

HORIZONTAL = 0
VERTICAL = 1

TIMER_DELAY_POCAO = 2000
TIMER_DELAY_COGUMELO = 2000

TIMER_POCAO = pygame.USEREVENT+1
TIMER_COGUMELO = pygame.USEREVENT+2

TILEMAP = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B...BB...BB........B',
    'B.B..B.B....BBB.BB.B',
    'B.BB.B.BBBB.BB..BB.B',
    'B...g.......BB.BBB.B',
    'BBB.B.BB.BB........B',
    'B...B.BB.BB.BBBBBBBB',
    'B.BBB.BB.BB.....BBBB',
    'B............BB....B',
    'B.BBBBB.B.BB.BBBBB.B',
    'B.......B..........B',
    'BBBBBBBBBBBBBBBBBBBB',
    'BBBBBBBBBBBBBBBBBBBB'
]