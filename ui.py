from config import *
import math
import random
from os.path import join
from os import walk


class UI(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.display_surface = pygame.display.get_surface()
        self.circuloQ = pygame.image.load(join('img', 'circulo_Q.png')).convert_alpha()
        self.circuloE = pygame.image.load(join('img', 'circulo_E.png')).convert_alpha()
        self.Mush = pygame.image.load(join('img', f'cogumelo.png')).convert_alpha()
        self.Potion = pygame.image.load(join('img', f'pocao.png')).convert_alpha()
        self.Coracao = [pygame.image.load(join('img', 'coracao_vazio.png')).convert_alpha(), pygame.image.load(join('img', 'coracao_cheio.png')).convert_alpha()]
        
    
    
    def desenhar_coracao(self, coracoes):
        #Desenhar os 3 corações vazios:
        self.game.tela.blit(self.Coracao[0], (LARGURA_TELA/2-125, ALTURA_TELA-80))
        self.game.tela.blit(self.Coracao[0], (LARGURA_TELA/2-62.5, ALTURA_TELA-80))
        self.game.tela.blit(self.Coracao[0], (LARGURA_TELA/2, ALTURA_TELA-80))

        #Desenhar os corações cheios:
        for coracao in range(coracoes):
            self.game.tela.blit(self.Coracao[1], (LARGURA_TELA/2-coracao*62.5, ALTURA_TELA-80))

    def display(self, player):
        self.game.tela.blit(self.circuloQ, (0,ALTURA_TELA-80))
        self.game.tela.blit(self.circuloE, (LARGURA_TELA-128,ALTURA_TELA-80))
        
        if player.temMush == True:
            self.game.tela.blit(self.Mush, (LARGURA_TELA-128+16, ALTURA_TELA-80+16))
        if player.temPotion == True:
            self.game.tela.blit(self.Potion, (16, ALTURA_TELA-80+16))

        self.desenhar_coracao(player.coracoes)