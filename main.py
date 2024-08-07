import pygame
from config import *
from sprites import Block, Chao, Item, Barra, Hitbox, HitboxInimigo
from player import Player
from inimigo import Inimigo
from vertice import Vertice
from ui import UI
import sys

class JOGO:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption(TITULO_JOGO)
        self.clock = pygame.time.Clock()

        self.Executando = True
        self.ply_x = 0
        self.ply_y = 0

    def new(self):
        self.Jogando = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.ground = pygame.sprite.LayeredUpdates()
        self.vertices = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.items = pygame.sprite.LayeredUpdates()
        self.playerg = pygame.sprite.LayeredUpdates()
        self.player = Player(self, 512, 256)

        for i in range(len(tilemap)):
            for j in range(len(tilemap[i])):
                if tilemap[i][j] == "B":
                    Block(self, j, i)
                if tilemap[i][j] == ".":
                    Chao(self, j, i)
                if tilemap[i][j] == "g":
                    Chao(self, j, i)
                if tilemap[i][j] == "p":
                    Chao(self, j, i)
                    Item(self, j, i, 'pocao')
                if tilemap[i][j] == "c":
                    Chao(self, j, i)
                    Item(self, j, i, 'cogumelo')
                if tilemap[i][j] == "i":
                    Chao(self, j, i)
                    Inimigo(self, j, i)

        Vertice(self, 1, 1, 1, [BAIXO, DIREITA])
        Vertice(self, 3, 1, 2, [ESQUERDA, BAIXO])
        Vertice(self, 6, 1, 3, [BAIXO, DIREITA])
        Vertice(self, 8, 1, 4, [ESQUERDA, BAIXO])
        Vertice(self, 11, 1, 5, [BAIXO, DIREITA])
        Vertice(self, 15, 1, 6, [BAIXO, ESQUERDA, DIREITA])
        Vertice(self, 18, 1, 7, [ESQUERDA, BAIXO])

        Vertice(self, 3, 2, 8, [CIMA, DIREITA])
        Vertice(self, 4, 2, 9, [ESQUERDA, BAIXO])
        Vertice(self, 8, 2, 10, [CIMA, DIREITA])
        Vertice(self, 11, 2, 11, [CIMA, BAIXO, ESQUERDA])

        Vertice(self, 14, 3, 12, [BAIXO, DIREITA])
        Vertice(self, 15, 3, 13, [CIMA, ESQUERDA])

        Vertice(self, 1, 4, 14, [CIMA, DIREITA])
        Vertice(self, 3, 4, 15, [BAIXO, ESQUERDA, DIREITA])
        Vertice(self, 4, 4, 16, [CIMA, ESQUERDA, DIREITA])
        Vertice(self, 5, 4, 17, [BAIXO, ESQUERDA, DIREITA])
        Vertice(self, 6, 4, 18, [CIMA, ESQUERDA, DIREITA])
        Vertice(self, 8, 4, 19, [BAIXO, ESQUERDA, DIREITA])
        Vertice(self, 11, 4, 20, [ESQUERDA, CIMA, BAIXO])

        Vertice(self, 11, 5, 21, [CIMA, BAIXO, DIREITA])
        Vertice(self, 14, 5, 22, [ESQUERDA, DIREITA, CIMA])
        Vertice(self, 18, 5, 23, [ESQUERDA, CIMA])

        Vertice(self, 1, 6, 24, [BAIXO, DIREITA])
        Vertice(self, 3, 6, 25, [CIMA, ESQUERDA])

        Vertice(self, 11, 7, 26, [BAIXO, CIMA, DIREITA])
        Vertice(self, 12, 7, 27, [BAIXO, ESQUERDA, DIREITA])
        Vertice(self, 15, 7, 28, [BAIXO, ESQUERDA])

        Vertice(self, 1, 8, 29, [CIMA, DIREITA, BAIXO])
        Vertice(self, 5, 8, 30, [ESQUERDA, CIMA, DIREITA])
        Vertice(self, 7, 8, 31, [ESQUERDA, BAIXO, DIREITA])
        Vertice(self, 8, 8, 32, [CIMA, ESQUERDA, DIREITA])
        Vertice(self, 9, 8, 99, [BAIXO, ESQUERDA, DIREITA])
        Vertice(self, 11, 8, 33, [ESQUERDA, CIMA, DIREITA])
        Vertice(self, 12, 8, 34, [ESQUERDA, BAIXO, CIMA])
        Vertice(self, 15, 8, 35, [CIMA, DIREITA])
        Vertice(self, 18, 8, 36, [ESQUERDA, BAIXO])

        Vertice(self, 1, 10, 37, [CIMA, DIREITA])
        Vertice(self, 7, 10, 38, [ESQUERDA, CIMA])
        Vertice(self, 9, 10, 39, [CIMA, DIREITA])
        Vertice(self, 12, 10, 40, [CIMA, ESQUERDA, DIREITA])
        Vertice(self, 18, 10, 41, [ESQUERDA, CIMA])

        Barra(self, 0, 0)

        self.ui = UI(self)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Jogando = False
                self.Executando = False
            if event.type == TIMER_COGUMELO:
                self.player.speed = VELOCIDADE_JOGADOR
                self.player.usingMush = False
                pygame.time.set_timer(TIMER_COGUMELO, 0)
            if event.type == TIMER_POCAO:
                self.player.intangivel = False
                self.player.usingPotion = False
                pygame.time.set_timer(TIMER_POCAO, 0)
            if event.type == TIMER_INTANGIVEL:
                self.player.intangivel = False
                pygame.time.set_timer(TIMER_INTANGIVEL, 0)

    def update(self):
        self.all_sprites.update()
        self.playerg.update()

    def draw(self):
        self.tela.fill('black')
        self.all_sprites.draw(self.tela)
        self.tela.blit(self.player.image, (self.player.rect.x - 5, self.player.rect.y - 10))
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
