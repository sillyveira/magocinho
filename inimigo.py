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

    def movimento_inimigo_1(self):
            self.ply_x, self.ply_y = self.game.ply_x, self.game.ply_y
            var_temp = 0
            if abs(self.ply_y - self.rect.y) > abs(self.ply_x - self.rect.x):
                #Se a distância em Y for maior, priorizá-la. o X está mais alinhado que o Y caso seja menor,
                #então a decisão lógica seria alcançar o jogador pelo Y.
                if self.ply_y > self.rect.y and BAIXO in self.direcoes and self.direcao_reversa != BAIXO:
                    self.direcao_reversa = CIMA
                    self.direcao = BAIXO
                    var_temp = 1
                elif self.ply_y < self.rect.y and CIMA in self.direcoes and self.direcao_reversa != CIMA:
                    self.direcao_reversa = BAIXO
                    self.direcao = CIMA
                    var_temp = 1
            else:
                if self.ply_x > self.rect.x and DIREITA in self.direcoes and self.direcao_reversa != DIREITA: 
                    #Se a distância em X for maior, priorizá-la. Mesma justificativa do comentário acima
                    self.direcao_reversa = ESQUERDA
                    self.direcao = DIREITA
                    var_temp = 1        
                elif self.ply_x < self.rect.x and ESQUERDA in self.direcoes and self.direcao_reversa != ESQUERDA:
                    
                    self.direcao_reversa = DIREITA
                    self.direcao = ESQUERDA
                    var_temp = 1

            if var_temp == 0: #Não pode seguir nenhuma direção até o jogador:
                #1. Pode seguir outra direção sem ser a reversa:
                if len(self.direcoes) > 1:
                    if self.direcao_reversa in self.direcoes:
                        self.direcoes.remove(self.direcao_reversa)  #Removendo a direção reversa dos caminhos possíveis
                        self.direcao = self.direcoes[0]
                        self.direcao_reversa = -self.direcao
                #2. No caso de só possuir a direção reversa possível, seguí-la:
                else:
                    self.direcao = self.direcoes[0]
                    self.direcao_reversa = -self.direcao

    def movimento_inimigo_2(self):
                # Verificar o tamanho da lista de direções possíveis
                if len(self.direcoes) > 1: 
                    if self.direcao_reversa in self.direcoes: # Remover a direção reversa
                        self.direcoes.remove(self.direcao_reversa) # Randomizar entre as direções restantes
                    direcao_escolhida = random.choice(self.direcoes)
                else:
                    direcao_escolhida = self.direcoes[0] # Seguir a única direção disponível, que é a reversa.

                self.direcao = direcao_escolhida # Atualizar a direção do inimigo
                self.direcao_reversa = -self.direcao # Atualizar a direção reversa