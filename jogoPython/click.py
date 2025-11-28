# pip install pygame
# import pygame

import pygame
import random
import math

pygame.init()

PRETO = (0,0,0)
BRANCO = (255,255,255)
VERMELHO = (255,0,0)

largura_tela = 800
altura_tela = 500

tela = pygame.display.set_mode((largura_tela,altura_tela))

pygame.display.set_caption("Jogo de Clique!")

relogio = pygame.time.Clock() #FPS

alvo_raio = 30 #Tamanho do alvo

alvo_x = random.randint(alvo_raio, largura_tela-alvo_raio) #Para o alvo não aparecer fora da tela
alvo_y = random.randint(alvo_raio, altura_tela-alvo_raio) #Para o alvo não aparecer fora da tela

placar = 0 

fonte = pygame.font.Font(None, 70)

rodando = True

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
            print(pos_mouse)

            distancia = math.dist(pos_mouse,(alvo_x,alvo_y))

            if distancia <= alvo_raio:
                print("Acertou!")
                placar += 1
                alvo_x = random.randint(alvo_raio, largura_tela-alvo_raio)
                alvo_y = random.randint(alvo_raio, altura_tela-alvo_raio)
                alvo_raio = max(1,alvo_raio-2)
            else:
                print("Errou!")


    tela.fill(PRETO)
    pygame.draw.circle(tela, VERMELHO, (alvo_x,alvo_y), alvo_raio)
    texto_placar = fonte.render(f"Placar {placar}", True, BRANCO)
    tela.blit(texto_placar,(10,10)) #Camadas da tela
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()