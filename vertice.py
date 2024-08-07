from config import *
import math
import random
from os.path import join
from os import walk

class Vertice(pygame.sprite.Sprite):
    def __init__(self, game, x, y, numero, direcoes_possiveis):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.vertices
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.direcoes_possiveis = direcoes_possiveis
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.numero = numero


        self.image = pygame.Surface([self.width, self.height])
        #self.image = pygame.image.load(join('pygame2', 'img', 'magicinho.png')).convert_alpha()
        self.image.fill('purple')

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

            