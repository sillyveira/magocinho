from config import *
from sprites import Item
import math
import random
from os.path import join
from os import walk

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE_PLAYER
        self.y = y * TILESIZE_PLAYER
        self.width = TILESIZE_PLAYER
        self.height = TILESIZE_PLAYER

        self.image = pygame.Surface([self.width, self.height])
        #self.image = pygame.image.load(join('pygame2', 'img', 'magicinho.png')).convert_alpha()
        self.image.fill('green')

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = VELOCIDADE_JOGADOR
        self.x_c = 0
        self.y_c = 0
