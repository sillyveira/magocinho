from config import *
from sprites import Item
import math
import random
from os.path import join


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.playerg
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.coletaveis = 106 #106

        self.usingPotion = False
        self.usingMush = False
        self.temPotion = False
        self.temMush = False

        self.contagem = 0 
        self.pontos = 0
        self.x = x
        self.y = y
        self.width = TILESIZE_PLAYER
        self.height = TILESIZE_PLAYER

        self.image = pygame.Surface([self.width, self.height])
        self.imagex = pygame.Surface([self.width, self.height])
        self.imagex = pygame.image.load(join('img', 'magocinho', 'baixo_1.png')).convert_alpha()
        
        self.imagens_esquerda = ['esquerda_1.png', 'esquerda_2.png']
        self.imagens_direita = ['direita_1.png', 'direita_2.png']
        self.imagens_cima = ['cima_1.png', 'cima_2.png']
        self.imagens_baixo = ['baixo_1.png', 'baixo_2.png']

        self.game.barulho_perde_vida = pygame.mixer.Sound('lost_life_sound.wav')
        self.game.barulho_pega_item = pygame.mixer.Sound('pick_itens_sound.wav')
        self.game.barulho_usa_item = pygame.mixer.Sound('use_itens_sound.wav')

        self.speed = VELOCIDADE_JOGADOR
        self.x_c = 0
        self.y_c = 0

        self.direcao = ''
        self.coracoes = 3
        self.intangivel = False

        self.rect = pygame.Rect(self.image.get_rect().left, self.image.get_rect().top, 40, self.image.get_rect().height - 20)
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.input_()

        if self.direcao == DIREITA:
            self.x_c += self.speed
            self.contagem = self.contagem + 0.1
            self.imagex = pygame.image.load(join('img', 'magocinho', self.imagens_direita[math.ceil(self.contagem) % len(self.imagens_direita)])).convert_alpha()
        elif self.direcao == ESQUERDA:
            self.x_c -= self.speed
            self.contagem = self.contagem + 0.1
            self.imagex = pygame.image.load(join('img', 'magocinho', self.imagens_esquerda[math.ceil(self.contagem) % len(self.imagens_esquerda)])).convert_alpha()
        elif self.direcao == BAIXO:
            self.y_c += self.speed
            self.contagem = self.contagem + 0.1
            self.imagex = pygame.image.load(join('img', 'magocinho', self.imagens_baixo[math.ceil(self.contagem) % len(self.imagens_baixo)])).convert_alpha()
        elif self.direcao == CIMA:
            self.y_c -= self.speed
            self.contagem = self.contagem + 0.1
            self.imagex = pygame.image.load(join('img', 'magocinho', self.imagens_cima[math.ceil(self.contagem) % len(self.imagens_cima)])).convert_alpha()

        self.rect.x += self.x_c  
        self.collision("x")           
        self.rect.y += self.y_c 
        self.collision("y")

        self.x_c = 0
        self.y_c = 0
        self.game.ply_x = self.rect.x
        self.game.ply_y = self.rect.y

    def input_(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: 
            self.direcao = DIREITA              
        if keys[pygame.K_LEFT]:
            self.direcao = ESQUERDA
        if keys[pygame.K_DOWN]:
            self.direcao = BAIXO
        if keys[pygame.K_UP]:
            self.direcao = CIMA
        if keys[pygame.K_q] and self.temPotion:  # Usar poção
            self.game.barulho_usa_item.play()
            self.temPotion = False
            self.usingPotion = True
            self.intangivel = True
            pygame.time.set_timer(TIMER_INTANGIVEL, TIMER_DELAY_POCAO)
        if keys[pygame.K_e] and self.temMush:  # Usar cogumelo
            self.game.barulho_usa_item.play()
            self.temMush = False
            self.speed = VELOCIDADE_COGUMELO
            self.usingMush = True
            pygame.time.set_timer(TIMER_COGUMELO, TIMER_DELAY_COGUMELO)
            


    def collision(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if direction == "x":
            if hits:
                if self.x_c > 0: self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_c < 0: self.rect.x = hits[0].rect.right
        if direction == "y":
            if hits:
                if self.y_c > 0: self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_c < 0: self.rect.y = hits[0].rect.bottom

        hit_item = pygame.sprite.spritecollide(self, self.game.items, False)
        if hit_item:
            item = hit_item[0]
            if item.tipo == 'cogumelo' and not self.temMush:
                hit_item[0].kill()
                self.temMush = True
                self.game.barulho_pega_item.play()
                self.coletaveis -= 1
            if item.tipo == 'pocao' and not self.temPotion:
                hit_item[0].kill()
                self.temPotion = True
                self.game.barulho_pega_item.play()
                self.coletaveis -= 1
            if item.tipo == 'moeda':
                hit_item[0].kill() #remove o item do mapa
                self.pontos += 1
                self.coletaveis -= 1
            if self.coletaveis == 0:
                self.game.atualizar_itens()
                self.coletaveis = 106    
            
        hit_inimigo = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hit_inimigo and not self.intangivel:
            self.game.barulho_perde_vida.play() # Chamar isso quando perder uma vida
            self.intangivel = True
            self.coracoes -= 1
            if self.coracoes == 0:
                self.game.mostrar_tela_gameover()
            else:
                pygame.time.set_timer(TIMER_INTANGIVEL, TIMER_DELAY_INTANGIVEL)
