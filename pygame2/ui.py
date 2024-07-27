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
    def display(self, player):
        self.game.tela.blit(self.circuloQ, (0,0))
        self.game.tela.blit(self.circuloE, (LARGURA_TELA-128,0))

        if player.temMush == True:
            self.game.tela.blit(self.Mush, (LARGURA_TELA-128+16, 16))
        if player.temPotion == True:
            self.game.tela.blit(self.Potion, (16, 16))