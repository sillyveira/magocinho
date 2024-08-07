from config import *
from sprites import Item
from os.path import join
from os import walk
import math
import random

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, game, x, y, z):
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

        if z == 1:
         self.MovimentoInimigo = 1
        else:
         self.MovimentoInimigo = 2

        self.speed = VELOCIDADE_INIMIGO

        self.x_c = 0
        self.y_c = 0
        self.ultimo_vertice = 0
        self.direcoes = []
        self.direcao = DIREITA
        self.direcao_reversa = ESQUERDA

        self.rect = pygame.Rect(self.image.get_rect().left, self.image.get_rect().top, 40, self.image.get_rect().height - 20)
        self.rect.x = self.x
        self.rect.y = self.y
        
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
          
    def collision(self):
        hits = pygame.sprite.spritecollide(self, self.game.vertices, False)
        if hits:
            if abs(hits[0].rect.x - self.rect.x) == 0 and abs(hits[0].rect.y - self.rect.y) == 0:
                if self.ultimo_vertice != hits[0].numero:
                    self.ultimo_vertice = hits[0].numero
                    self.direcoes = []
                    for dir in hits[0].direcoes_possiveis:
                        self.direcoes.append(dir)
                    
                    if self.MovimentoInimigo == 1:
                        self.movimento_inimigo_1()
                    else:
                        self.movimento_inimigo_2()

        def movimento_inimigo1(self):

            if self.direcao == 'direita':
                if self.alvo['coordenada_x'] > self.posicao_x and self.curvas['direita']:
                    self.posicao_x += self.velocidade
                elif not self.curvas['direita']:
                    if self.alvo['coordenada_y'] > self.posicao_y and self.curvas['baixo']:
                        self.direcao = 'virar para baixo'
                        self.posicao_y += self.velocidade
                    elif self.alvo['coordenada_y'] < self.posicao_y and self.curvas['direita']:
                        self.direcao = 'cima'
                        self.posicao_y -= self.velocidade
                    elif self.alvo['coordenada_x']  < self.posicao_x and self.curvas['esquerda']: # self.curvas['esquerda'] = pode ir pra esquerda
                        self.direcao = 'esquerda'
                        self.posicao_x -= self.velocidade
                    elif self.curvas['baixo']:
                        self.direcao = 'baixo'
                        self.posicao_y -= self.velocidade
                    elif self.curvas['cima']:
                        self.direcao = 'cima'
                        self.posicao_y += self.velocidade
                    elif self.curvas['esquerda']:
                        self.direcao = 'esquerda'
                        self.posicao_x -= self.velocidade
                elif self.curvas['direita']:
                    if self.alvo['coordenada_y'] > self.posicao_y and self.curvas['baixo']:
                        self.direcao = 'baixo'
                        self.posicao_y += self.velocidade
                    if self.alvo['coordenada_y'] < self.posicao_y and self.curvas['cima']:
                        self.direcao = 'cima'
                        self.posicao_y -= self.velocidade
                    else:
                        self.posicao_x += self.velocidade 

            elif self.direcao == 'esquerda':
                if self.alvo['coordenada_y'] > self.posicao_y and self.curvas['baixo']:
                    self.direcao = 'baixo'
                elif self.alvo['coordenada_x'] < self.posicao_x and self.curvas['direita']:
                    self.posicao_x += self.velocidade

                elif not self.curvas['esquerda']:
                    if self.alvo['coordenada_y'] > self.posicao_y and self.curvas['baixo']:
                        self.direcao = 'virar para baixo'
                        self.posicao_y += self.velocidade
                    elif self.alvo['coordenada_y'] < self.posicao_y and self.curvas['cima']:
                        self.direcao = 'cima'
                        self.posicao_y -= self.velocidade
                    elif self.alvo['coordenada_x'] > self.posicao_x and self.curvas['direita']: # self.curvas['esquerda'] = pode ir pra esquerda
                        self.direcao = 'direita'
                        self.posicao_x -= self.velocidade
                    elif self.curvas['baixo']:
                        self.direcao = 'baixo'
                        self.posicao_y -= self.velocidade
                    elif self.curvas['cima']:
                        self.direcao = 'cima'
                        self.posicao_y += self.velocidade
                    elif self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x -= self.velocidade
                elif self.curvas['esquerda']:
                    if self.alvo['coordenada_y'] > self.posicao_y and self.curvas['baixo']:
                        self.direcao = 'baixo'
                        self.posicao_y += self.velocidade
                    if self.alvo['coordenada_y'] < self.posicao_y and self.curvas['cima']:
                        self.direcao = 'cima'
                        self.posicao_y -= self.velocidade
                    else:
                        self.posicao_x -= self.velocidade 


            elif self.direcao == 'cima': 
                if self.alvo['coordenada_x'] < self.posicao_x and self.curvas['esquerda']:
                    self.direcao = 'esquerda'
                    self.posicao_x -= self.velocidade
                elif self.alvo['coordenada_y'] < self.posicao_y and self.curvas['cima']:
                    self.posicao_y -= self.velocidade

                elif not self.curvas['cima']:
                    if self.alvo['coordenada_x'] > self.posicao_x and self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x += self.velocidade
                    elif self.alvo['coordenada_x'] < self.posicao_x and self.curvas['esquerda']:
                        self.direcao = 'esquerda' 
                        self.posicao_x -= self.velocidade
                    elif self.alvo['coordenada_y'] > self.posicao_y and self.curvas['baixo']: # self.curvas['esquerda'] = pode ir pra esquerda
                        self.direcao = 'baixo'
                        self.posicao_x += self.velocidade
                    elif self.curvas['baixo']:
                        self.direcao = 'cima'
                        self.posicao_y -= self.velocidade
                    elif self.curvas['esquerda']:
                        self.direcao = 'esquerda'
                        self.posicao_x -= self.velocidade
                    elif self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x -= self.velocidade
                elif self.curvas['cima']:
                    if self.alvo['coordenada_x'] > self.posicao_x and self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x += self.velocidade
                    elif self.alvo['coordenada_x'] < self.posicao_x and self.curvas['esquerda']:
                        self.direcao = 'esquerda' 
                        self.posicao_x -= self.velocidade 
                    else:
                        self.posicao_y -= self.velocidade 
            
            elif self.direcao == 'baixo': 
                if self.alvo['coordenada_y'] > self.posicao_y and self.curvas['baixo']: #pode continuar para baixo
                    self.posicao_y += self.velocidade

                elif not self.curvas['baixo']:
                    if self.alvo['coordenada_x'] > self.posicao_x and self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x += self.velocidade
                    elif self.alvo['coordenada_x'] < self.posicao_x and self.curvas['esquerda']:
                        self.direcao = 'esquerda'
                        self.posicao_x -= self.velocidade
                    elif self.alvo['coordenada_y'] < self.posicao_y and self.curvas['cima']: #pode continuar para baixo
                        self.direcao = 'cima'
                        self.posicao_y -= self.velocidade
                    elif self.curvas['cima']:
                        self.direcao = 'cima'
                        self.posicao_y -= self.velocidade
                    elif self.curvas['esquerda']:
                        self.direcao = 'esquerda'
                        self.posicao_x -= self.velocidade
                    elif self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x += self.velocidade


                elif self.curvas['baixo']:
                    if self.alvo['coordenada_x'] > self.posicao_x and self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x += self.velocidade
                    elif self.alvo['coordenada_x'] < self.posicao_x and self.curvas['esquerda']:
                        self.direcao = 'esquerda' 
                        self.posicao_x -= self.velocidade 
                    else:
                        self.posicao_y += self.velocidade

        def movimento_inimigo2(self):


            if self.direcao == 'cima': 
                if self.alvo['coordenada_x'] > self.posicao_x and self.curvas['esquerda']:
                    self.direcao = 'esquerda'
                    self.posicao_x -= self.velocidade
                elif self.alvo['coordenada_y'] > self.posicao_y and self.curvas['cima']:
                    self.posicao_y += self.velocidade

                elif not self.curvas['cima']:
                    if self.alvo['coordenada_x'] > self.posicao_x and self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x += self.velocidade
                    elif self.alvo['coordenada_x'] < self.posicao_x and self.curvas['esquerda']:
                        self.direcao = 'esquerda' 
                        self.posicao_x -= self.velocidade
                    elif self.alvo['coordenada_y'] < self.posicao_y and self.curvas['baixo']: # self.curvas['esquerda'] = pode ir pra esquerda
                        self.direcao = 'baixo'
                        self.posicao_x += self.velocidade
                    elif self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x -= self.velocidade
                    elif self.curvas['baixo']:
                        self.direcao = 'baixo'
                        self.posicao_y -= self.velocidade
                    elif self.curvas['esquerda']:
                        self.direcao = 'esquerda'
                        self.posicao_x -= self.velocidade
                elif self.curvas['cima']:
                    self.posicao_y += self.velocidade

            elif self.direcao == 'esquerda':
                if self.alvo['coordenada_y'] < self.posicao_y and self.curvas['baixo']:
                    self.direcao = 'baixo'
                elif self.alvo['coordenada_x'] < self.posicao_x and self.curvas['direita']:
                    self.posicao_x += self.velocidade

                elif not self.curvas['esquerda']:
                    if self.alvo['coordenada_y'] > self.posicao_y and self.curvas['cima']:
                        self.direcao = 'cima'
                        self.posicao_y += self.velocidade
                    elif self.alvo['coordenada_y'] < self.posicao_y and self.curvas['baixo']:
                        self.direcao = 'virar para baixo'
                        self.posicao_y -= self.velocidade
                    elif self.alvo['coordenada_x'] > self.posicao_x and self.curvas['direita']: # self.curvas['esquerda'] = pode ir pra esquerda
                        self.direcao = 'direita'
                        self.posicao_x -= self.velocidade
                    elif self.curvas['cima']:
                        self.direcao = 'cima'
                        self.posicao_y += self.velocidade
                    elif self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x -= self.velocidade
                    elif self.curvas['baixo']:
                        self.direcao = 'baixo'
                        self.posicao_y -= self.velocidade
                elif self.curvas['esquerda']:
                    self.posicao_x -= self.velocidade

            elif self.direcao == 'direita':
                if self.alvo['coordenada_x'] > self.posicao_x and self.curvas['direita']:
                    self.posicao_x += self.velocidade
                elif not self.curvas['direita']:
                    if self.alvo['coordenada_y'] < self.posicao_y and self.curvas['baixo']:
                        self.direcao = 'virar para baixo'
                        self.posicao_y -= self.velocidade
                    elif self.alvo['coordenada_y'] > self.posicao_y and self.curvas['direita']:
                        self.direcao = 'cima'
                        self.posicao_y += self.velocidade
                    elif self.alvo['coordenada_x'] < self.posicao_x and self.curvas['esquerda']: # self.curvas['esquerda'] = pode ir pra esquerda
                        self.direcao = 'esquerda'
                        self.posicao_x -= self.velocidade
                    elif self.curvas['esquerda']:
                        self.direcao = 'esquerda'
                        self.posicao_x -= self.velocidade
                    elif self.curvas['baixo']:
                        self.direcao = 'baixo'
                        self.posicao_y -= self.velocidade
                    elif self.curvas['cima']:
                        self.direcao = 'cima'
                        self.posicao_y += self.velocidade
                    
                
                elif self.curvas['direita']:
                    self.posicao_x += self.velocidade 
            
            elif self.direcao == 'baixo': 
                if self.alvo['coordenada_y'] < self.posicao_y and self.curvas['baixo']: #pode continuar para baixo
                    self.posicao_y -= self.velocidade

                elif not self.curvas['baixo']:
                    if self.alvo['coordenada_x'] > self.posicao_x and self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x += self.velocidade
                    elif self.alvo['coordenada_x'] < self.posicao_x and self.curvas['esquerda']:
                        self.direcao = 'esquerda'
                        self.posicao_x -= self.velocidade
                    elif self.alvo['coordenada_y'] > self.posicao_y and self.curvas['cima']: #pode continuar para baixo
                        self.direcao = 'cima'
                        self.posicao_y += self.velocidade
                    elif self.curvas['esquerda']:
                        self.direcao = 'esquerda'
                        self.posicao_x -= self.velocidade
                    elif self.curvas['direita']:
                        self.direcao = 'direita'
                        self.posicao_x += self.velocidade
                    elif self.curvas['cima']:
                        self.direcao = 'cima'
                        self.posicao_y -= self.velocidade

                elif self.curvas['baixo']:
                        self.posicao_y -= self.velocidade