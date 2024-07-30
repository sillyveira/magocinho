import pygame
from config import *
from sprites import Block, Chao, Item, Barra
from player import Player
from inimigo import Inimigo
from grafo import Vertice
from ui import UI
import sys
#Importação da biblioteca do pygame, dos sprites, do jogador, do inimigo e do vértice

#Classe principal
class JOGO:
    def __init__(self):
        #Inicialização do pygame, configurações da tela e instanciando o clock e variável de execução
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
        pygame.display.set_caption(TITULO_JOGO)
        self.clock = pygame.time.Clock()
        self.Executando = True


    def new(self):
        self.Jogando = True
        #definindo os grupos de sprite
        self.all_sprites    = pygame.sprite.LayeredUpdates()
        self.blocks         = pygame.sprite.LayeredUpdates()
        self.ground         = pygame.sprite.LayeredUpdates()
        self.grafos         = pygame.sprite.LayeredUpdates()
        self.enemies        = pygame.sprite.LayeredUpdates()
        self.items          = pygame.sprite.LayeredUpdates()
        #instanciando o jogador
        self.player = Player(self, 1.1, 1.1)
        #lendo o mapa feito nas configurações (config.py)
        for i in range(len(tilemap)):
            for j in range(len(tilemap[i])):
                if tilemap[i][j] == "B":
                    Block(self, j, i)
                if tilemap[i][j] == ".":
                    Chao(self, j, i)
                if tilemap[i][j] == "g":
                    Chao(self,j, i)
                if tilemap[i][j] == "p":
                    Chao(self,j, i)
                    Item(self, j, i, 'pocao')
                if tilemap[i][j] == "c":
                    Chao(self,j, i)
                    Item(self, j, i, 'cogumelo')
        #sprite das barras no mapa
        Barra(self, 0, 0)

        #inicializando a interface
        self.ui = UI(self)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.Jogando = False
                self.Executando = False
            if event.type == TIMER_COGUMELO: #caso o jogador use o item de cogumelo
                self.player.speed = VELOCIDADE_JOGADOR
                self.player.usingMush = False
                pygame.time.set_timer(TIMER_COGUMELO, 0) #desliga o timer
            if event.type == TIMER_POCAO: #caso o jogador use o item de poção
                self.player.intangivel = True
                self.player.usingPotion = False
                pygame.time.set_timer(TIMER_POCAO, 0)
    def update(self):
        self.all_sprites.update() #atualizando todos os sprites


    def draw(self):#desenhando os sprites na tela
        self.tela.fill('black')
        self.all_sprites.draw(self.tela)
        self.clock.tick(FPS)
        self.ui.display(self.player) #sprites da interface
        pygame.display.update()

    def main(self):
        while self.Jogando: #rodando as funções enquanto o jogo está em execução
            self.events()
            self.update()
            self.draw()
        self.Executando = False 

    def game_over(self):
        pass

    def intro_screen(self):
        pass

#iniciando o jogo:
g = JOGO()
g.intro_screen()
g.new()
while g.Executando:
    g.main()
    g.game_over()

#fechando o jogo:
pygame.quit()
sys.exit()