import pygame
import sys
import os
import constantes
import constantesgame_over

from config import *
from sprites import Block, Chao, Item, Barra, Hitbox, HitboxInimigo
from player import Player
from inimigo import Inimigo
from vertice import Vertice
from ui import UI

class TelaInicial:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()

    def novo_jogo(self):
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        self.tela.fill(constantes.AZUL)
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()

    def carregar_arquivos(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'img')
        self.diretorio_audios = os.path.join(os.getcwd(), 'audios')
        self.start_logo = os.path.join(diretorio_imagens, constantes.IMAGEM)
        self.start_logo = pygame.image.load(self.start_logo).convert_alpha()

    def mostrar_texto(self, texto, tamanho, cor, x, y):
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)

    def mostrar_start_logo(self, x, y):
        self.tela.fill(constantes.AZUL)
        start_logo_rect = self.start_logo.get_rect()
        start_logo_rect.midtop = (x, y)
        self.tela.blit(self.start_logo, start_logo_rect)

    def mostrar_tela_start(self):
        pygame.mixer.music.load(os.path.join(self.diretorio_audios, constantes.MUSICA_START))
        pygame.mixer.music.play()

        self.mostrar_start_logo(constantes.LARGURA / 2, 0)
        self.mostrar_texto( 
            '- PRESSIONE UMA TECLA PARA COMEÇAR -',
            32,
            constantes.ESCURO,
            constantes.LARGURA / 2,
            570
        )   

        pygame.display.flip()
        self.fade_in(2)  # Adicionando fade in
        self.esperar_por_jogador()

    def esperar_por_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(constantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYUP:
                    esperando = False    
                    pygame.mixer.music.stop()         
                    pygame.mixer.Sound(os.path.join(self.diretorio_audios, constantes.TECLA_START)).play()  

    def fade_in(self, duracao):
        fade_img = pygame.Surface((constantes.LARGURA, constantes.ALTURA)).convert_alpha()
        fade_img.fill((0, 0, 0))
        fade_alpha = 255
        fade_speed = fade_alpha / (duracao * constantes.FPS)

        while fade_alpha > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            fade_alpha -= fade_speed
            if fade_alpha < 0:
                fade_alpha = 0

            self.tela.fill(constantes.AZUL)  # Redesenhando o fundo
            self.mostrar_start_logo(constantes.LARGURA / 2, 0)  # Redesenhando o logo
            self.mostrar_texto( 
                '- PRESSIONE UMA TECLA PARA COMEÇAR -',
                32,
                constantes.ESCURO,
                constantes.LARGURA / 2,
                570
            )  # Redesenhando o texto
            fade_img.set_alpha(fade_alpha)
            self.tela.blit(fade_img, (0, 0))
            pygame.display.flip()
            self.relogio.tick(constantes.FPS)


class JOGO:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
        pygame.display.set_caption(TITULO_JOGO)
        self.clock = pygame.time.Clock()

        self.Executando = True
        self.ply_x = 0
        self.ply_y = 0
    def new(self):
        self.Jogando = True

        self.all_sprites    = pygame.sprite.LayeredUpdates()
        self.blocks         = pygame.sprite.LayeredUpdates()
        self.ground         = pygame.sprite.LayeredUpdates()
        self.vertices         = pygame.sprite.LayeredUpdates()
        self.enemies        = pygame.sprite.LayeredUpdates()
        self.items          = pygame.sprite.LayeredUpdates()
        self.playerg          = pygame.sprite.LayeredUpdates()
        self.player = Player(self, 512, 256)
        x = 0
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

        #Hitbox(self, 10, 10)
        #self.inimigo = Inimigo(self, 5, 10)
        #HitboxInimigo(self,90,90)
      #  for item in range(len(self.vertices)):
      #      print(f"{item}: {self.vertices[item].rect.x}, {self.vertices[item].rect.y}, {[self.vertices[item].direcoes_possiveis]}")
        Barra(self, 0, 0)

        #Vertices:

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

    def mostrar_tela_gameover(self):
        self.Jogando = False
        self.Executando = False

    def main(self):
        while self.Jogando:
            self.events()
            self.update()
            self.draw()
        self.Executando = False  

class GameoverTela:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantesgame_over.LARGURA, constantesgame_over.ALTURA))
        pygame.display.set_caption(constantesgame_over.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantesgame_over.FONTE)
        self.carregar_arquivos()

    def novo_jogo(self):
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantesgame_over.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        self.tela.fill(constantesgame_over.CINZA)
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()

    def carregar_arquivos(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'img')
        self.diretorio_audios = os.path.join(os.getcwd(), 'audios')
        self.start_logo = os.path.join(diretorio_imagens, constantesgame_over.IMAGEM)
        self.start_logo = pygame.image.load(self.start_logo).convert_alpha()

    def mostrar_texto(self, texto, tamanho, cor, x, y):
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)

    def mostrar_start_logo(self, x, y):
        self.tela.fill(constantesgame_over.CINZA)
        start_logo_rect = self.start_logo.get_rect()
        start_logo_rect.midtop = (x, y)
        self.tela.blit(self.start_logo, start_logo_rect)

    def mostrar_tela_gameover(self):
        pygame.mixer.music.load(os.path.join(self.diretorio_audios, constantesgame_over.MUSICA_START))
        pygame.mixer.music.play()
        
        self.mostrar_start_logo(constantesgame_over.LARGURA / 2, 0)

        self.mostrar_texto( 
            '- PRESSIONE UMA TECLA PARA COMEÇAR -',
            32,
            constantesgame_over.ESCURO,
            constantesgame_over.LARGURA / 2,
            570
        )   

        pygame.display.flip()
        self.fade_in(2)  # Adicionando fade in
        self.esperar_por_jogador()

    def esperar_por_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(constantesgame_over.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYUP:
                    esperando = False    
                    pygame.mixer.music.stop()         
                    pygame.mixer.Sound(os.path.join(self.diretorio_audios, constantesgame_over.TECLA_START)).play()  

    def fade_in(self, duracao):
        fade_img = pygame.Surface((constantesgame_over.LARGURA, constantesgame_over.ALTURA)).convert_alpha()
        fade_img.fill((0, 0, 0))
        fade_alpha = 255
        fade_speed = fade_alpha / (duracao * constantesgame_over.FPS)

        while fade_alpha > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            fade_alpha -= fade_speed
            if fade_alpha < 0:
                fade_alpha = 0

            self.tela.fill(constantesgame_over.CINZA)  # Redesenhando o fundo
            self.mostrar_start_logo(constantesgame_over.LARGURA / 2, 0)  # Redesenhando o logo
            self.mostrar_texto( 
                '- PRESSIONE UMA TECLA PARA COMEÇAR -',
                32,
                constantesgame_over.ESCURO,
                constantesgame_over.LARGURA / 2,
                570
            )  # Redesenhando o texto
            fade_img.set_alpha(fade_alpha)
            self.tela.blit(fade_img, (0, 0))
            pygame.display.flip()
            self.relogio.tick(constantesgame_over.FPS)
     

# Gerenciador de estados
class GerenciadorDeEstados:
    def __init__(self):
        self.estado = 'menu'

    def novo(self):
        if self.estado == 'menu':
            self.menu = TelaInicial()
            self.menu.mostrar_tela_start()
            self.estado = 'jogando'
            self.jogo = JOGO()
            self.jogo.new()
        if self.estado == 'jogando':
            self.jogo.main()
            self.estado = 'game over'
        if self.estado == 'game over':
            self.gameover = GameoverTela()
            self.gameover.mostrar_tela_gameover()
            self.estado = 'menu'

g = GerenciadorDeEstados()
while True:
    g.novo()
    pygame.quit()
    sys.exit()