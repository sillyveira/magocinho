from config import *
from sprites import Item
from os.path import join
from os import walk
import math

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill('green')

        self.ply_x = 0
        self.ply_y = 0

        self.contagem = 0 
        self.imagens_esquerda = ['esq_1.png', 'esq_2.png']
        self.imagens_direita = ['dir_1.png', 'dir_2.png']
        self.imagens_cima = ['up_1.png', 'up_2.png']
        self.imagens_baixo = ['down_1.png', 'down_2.png']


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.speed = VELOCIDADE_INIMIGO

        self.x_c = 0
        self.y_c = 0
        self.ultimo_vertice = 0
        self.direcoes = []
        self.direcao = DIREITA
        self.direcao_reversa = ESQUERDA

    def update(self):
        self.collision()
        if self.direcao == DIREITA:
            self.rect.x += self.speed
            self.contagem = self.contagem + 0.1
            self.image = pygame.image.load(join('img', 'guarda', self.imagens_direita[math.ceil(self.contagem) % len(self.imagens_direita)])).convert_alpha()
        elif self.direcao == ESQUERDA:
            self.rect.x -= self.speed
            self.contagem = self.contagem + 0.1
            self.image = pygame.image.load(join('img', 'guarda', self.imagens_esquerda[math.ceil(self.contagem) % len(self.imagens_esquerda)])).convert_alpha()
        elif self.direcao == CIMA:
            self.rect.y -= self.speed
            self.contagem = self.contagem + 0.1
            self.image = pygame.image.load(join('img', 'guarda', self.imagens_cima[math.ceil(self.contagem) % len(self.imagens_cima)])).convert_alpha()
        elif self.direcao == BAIXO:
            self.rect.y += self.speed
            self.contagem = self.contagem + 0.1
            self.image = pygame.image.load(join('img', 'guarda', self.imagens_baixo[math.ceil(self.contagem) % len(self.imagens_baixo)])).convert_alpha()
          