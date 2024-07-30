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

#Classe do chão
class Chao(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
          self.game = game
          self._layer = GROUND_LAYER
          self.groups = self.game.all_sprites, self.game.ground
          pygame.sprite.Sprite.__init__(self, self.groups)
          self.x = x * TILESIZE
          self.y = y * TILESIZE
          self.width = TILESIZE
          self.height = TILESIZE

          self.image = pygame.Surface([self.width, self.height])
          self.image = pygame.image.load(join('img', f'piso.png')).convert_alpha()
          self.rect = self.image.get_rect()
          self.rect.x = self.x
          self.rect.y = self.y

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
