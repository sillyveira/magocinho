import pygame
from config import *
from sprites import Block, Chao, Item
from player import Player
from inimigo import Inimigo
from ui import UI
import sys

class JOGO:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
        pygame.display.set_caption(TITULO_JOGO)
        self.clock = pygame.time.Clock()
       # self.fonteTexto = pygame.font.Font('Arial', 32)
        self.Executando = True


    def new(self):
        self.Jogando = True

        self.all_sprites    = pygame.sprite.LayeredUpdates()
        self.blocks         = pygame.sprite.LayeredUpdates()
        self.ground         = pygame.sprite.LayeredUpdates()
        self.enemies        = pygame.sprite.LayeredUpdates()
        self.items          = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 1.25, 2)
        for i in range(len(tilemap)):
            for j in range(len(tilemap[i])):
                if tilemap[i][j] == "B":
                    Block(self, j, i)
                if tilemap[i][j] == ".":
                    Chao(self, j, i)
                if tilemap[i][j] == "p":
                    Chao(self,j, i)
                    Item(self, j, i, 'pocao')
                if tilemap[i][j] == "c":
                    Chao(self,j, i)
                    Item(self, j, i, 'cogumelo')
        Inimigo(self, 4, 5)

        self.ui = UI(self)
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Jogando = False
                self.Executando = False
            if event.type == TIMER_COGUMELO:
                self.player.speed = VELOCIDADE_JOGADOR
                self.player.usingMush = False
                pygame.time.set_timer(TIMER_COGUMELO, 0) #desliga o timer
            if event.type == TIMER_POCAO:
                self.player.invisivel = True
                self.player.usingPotion = False
                pygame.time.set_timer(TIMER_POCAO, 0)
    def update(self):
        self.all_sprites.update()


    def draw(self):
        self.tela.fill('black')
        self.all_sprites.draw(self.tela)
        self.clock.tick(FPS)
        self.ui.display(self.player)
        pygame.display.update()

    def main(self):
        while self.Jogando:
            self.events()
            self.update()
            self.draw()
        self.Executando = False 

    def game_over(self):
        pass

    def intro_screen(self):
        pass

g = JOGO()
g.intro_screen()
g.new()
while g.Executando:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()