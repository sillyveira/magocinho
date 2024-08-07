import pygame
import constantes
import sys
import os

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

    def mostrar_tela_game_over(self):
        pass

g = TelaInicial()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()