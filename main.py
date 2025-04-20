import pygame
import time
import random
import sys

# Inicializando o Pygame
pygame.init()

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Tamanho da tela
largura = 600
altura = 400

# Tamanho do bloco da cobra
tamanho_bloco = 20

# Velocidade do jogo
velocidade = 15

# Fonte
fonte = pygame.font.SysFont("arial", 25)

# Criar tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("🐍 Snake Game com Python")

# Relógio
relogio = pygame.time.Clock()

def mostrar_pontuacao(pontuacao):
    valor = fonte.render(f"Pontuação: {pontuacao}", True, preto)
    tela.blit(valor, [10, 10])

def desenhar_cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, azul, [x[0], x[1], tamanho_bloco, tamanho_bloco])

def mensagem_fim(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura // 6, altura // 3])

def jogo():
    game_over = False
    sair = False

    x1 = largura // 2
    y1 = altura // 2

    x1_mudanca = 0
    y1_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    while not sair:

        while game_over:
            tela.fill(branco)
            mensagem_fim("Você perdeu! Pressione Q para sair ou R para reiniciar", vermelho)
            mostrar_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        sair = True
                        game_over = False
                    if evento.key == pygame.K_r:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x1_mudanca == 0:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT and x1_mudanca == 0:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP and y1_mudanca == 0:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN and y1_mudanca == 0:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            game_over = True

        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(branco)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Colisão com o próprio corpo
        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                game_over = True

        desenhar_cobra(tamanho_bloco, lista_cobra)
        mostrar_pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        relogio.tick(velocidade)

    pygame.quit()
    sys.exit()

# Inicia o jogo
jogo()
