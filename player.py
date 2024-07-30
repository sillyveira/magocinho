
from config import *
from sprites import Item
import math
import random
from os.path import join
from os import walk

#Classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.items = []

        #Variáveis relacionadas aos itens, se estão em uso e se possuem eles.
        self.usingPotion = False
        self.usingMush = False
        self.temPotion = False
        self.temMush = False

        self.x = x * TILESIZE_PLAYER
        self.y = y * TILESIZE_PLAYER
        self.width = TILESIZE_PLAYER
        self.height = TILESIZE_PLAYER

        self.image = pygame.Surface([self.width, self.height])
        #self.image = pygame.image.load(join('pygame2', 'img', 'magicinho.png')).convert_alpha()
        self.image.fill('red')

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = VELOCIDADE_JOGADOR
        self.x_c = 0
        self.y_c = 0
    def update(self): #função de atualização, recebe os inputs do jogador, o movimenta e faz a colisão.
            self.input_()
            self.rect.x += self.x_c  
            self.collision("x")           
            self.rect.y += self.y_c 
            self.collision("y")

            self.x_c = 0
            self.y_c = 0
    def input_(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]: 
                self.x_c += self.speed
                self.direcao = 'direita'              

            if keys[pygame.K_LEFT]:
                self.x_c -= self.speed
                self.direcao = 'esquerda'
            if keys[pygame.K_DOWN]:
                self.y_c += self.speed
                self.direcao = 'baixo'

            if keys[pygame.K_UP]:
                self.y_c -= self.speed
                self.direcao = 'cima'

            if keys[pygame.K_q]: #uso da poção
                
                if self.usingPotion == False:
                     self.temPotion = False
                     self.usingPotion = True
                     pygame.time.set_timer(TIMER_POCAO, TIMER_DELAY_POCAO)

            if keys[pygame.K_e]: #uso do cogumelo
                if self.usingMush == False and self.temMush == True:
                    self.temMush = False
                    self.speed = 15
                    self.usingMush = True
                    pygame.time.set_timer(TIMER_COGUMELO, TIMER_DELAY_COGUMELO)   

    def collision(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if direction == "x":
            if hits:
                 if self.x_c > 0: self.rect.x = hits[0].rect.left - self.rect.width #colidindo com a esquerda
                 if self.x_c < 0: self.rect.x = hits[0].rect.right #colidindo com a direita
        if direction == "y":
            if hits:
                 if self.y_c > 0: self.rect.y = hits[0].rect.top - self.rect.height #colidindo em cima
                 if self.y_c < 0: self.rect.y = hits[0].rect.bottom #colidindo embaixo
        hit_item = pygame.sprite.spritecollide(self, self.game.items, False)
        
        if hit_item: #ao colidir com o item, remove do mapa e adiciona ao jogador
            item = hit_item[0]
            if item.tipo == 'cogumelo' and self.temMush == False:
                hit_item[0].kill() #remove o item do mapa
                self.temMush = True

            if item.tipo == 'pocao' and self.temPotion == False:
                hit_item[0].kill() #remove o item do mapa
                self.temPotion = True
                
