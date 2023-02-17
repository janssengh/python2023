#introducao_pygame

import pygame
import math

#Constantes
VERMELHO =255,0,0
VERDE = 0,255,0
AZUL = 0,0,255
AMARELO = 255,255,0
LARANJA = 255,165,0
PRETO = 0,0,0
BRANCO = 255,255,255
PI = math.pi

#inicializa o módulo pygame
pygame.init()

#cria a tela gráfica
tela = pygame.display.set_mode((640,480), 0)
pygame.display.set_caption('Titulo da Janela')


#pinta a tela de branco
tela.fill(BRANCO)

pygame.draw.circle(tela, VERMELHO, (50,50), 40, 0)


pygame.display.update()

#Eventos do pygame - executa um loop infinito
while True:
    #pega cada evento gerado pelo pygame
    for e in pygame.event.get():
        if e.type == pygame.QUIT: #evento fechar janela
            exit()

