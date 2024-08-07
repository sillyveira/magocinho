from config import *
import math
import random
from os.path import join
from os import walk

#Classe dos blocos de colisão, o jogador não pode passar por eles e eles são invisíveis. 
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
          self.game = game
          self._layer = GROUND_LAYER
          self.groups = self.game.all_sprites, self.game.blocks
          pygame.sprite.Sprite.__init__(self, self.groups)
          #Multiplico pelo TILESIZE para que cada um esteja disposto a cada 64 pixels (ou o tilesize definido) e assim, seja desenhado certinho com o uso do tilemap. 
          self.x = x * TILESIZE
          self.y = y * TILESIZE
          self.width = TILESIZE
          self.height = TILESIZE

          self.image = pygame.Surface([self.width, self.height])
          self.rect = self.image.get_rect()
          self.rect.x = self.x
          self.rect.y = self.y

class Moeda(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ITEM_LAYER
        self.groups = self.game.all_sprites, self.game.items
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.image.load(join('img', 'coin.png')).convert_alpha()

        self.image = pygame.transform.scale(self.image, (self.width // 1.2, self.height // 1.2))

        self.rect = self.image.get_rect()
        self.rect.x = self.x + (TILESIZE - self.image.get_width()) // 2
        self.rect.y = self.y + (TILESIZE - self.image.get_height()) // 2

        self.tipo = 'moeda'

#Classe do chão
class Chao(pygame.sprite.Sprite):
    def __init__(self, game, x, y, tem_moeda=False):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.ground
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.image.load(join('img', 'piso.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        if tem_moeda:   
          Moeda(game, x, y)

#Classe dos itens coletáveis
class Item(pygame.sprite.Sprite):
     def __init__(self, game, x, y, nome_item):
          self.game = game
          self._layer = PLAYER_LAYER
          self.groups = self.game.all_sprites, self.game.items
          pygame.sprite.Sprite.__init__(self,self.groups)
          self.x = (x * 64)+16
          self.y = (y * 64)+16
          self.width = 32
          self.height = 32
          self.image = pygame.image.load(join('img', f'{nome_item}.png')).convert_alpha()
          
          self.tipo = nome_item
          self.rect = self.image.get_rect()
          self.rect.x = self.x
          self.rect.y = self.y

#Classe da imagem das barras dispostas no mapa 
class Barra(pygame.sprite.Sprite):
     def __init__(self, game, x, y):
          self.game = game
          self._layer = GROUND_LAYER
          self.groups = self.game.all_sprites, self.game.ground

          pygame.sprite.Sprite.__init__(self,self.groups)

          self.image = pygame.image.load(join('img', f'background.png')).convert_alpha()

          self.rect = self.image.get_rect()
          self.rect.x = x
          self.rect.y = y
