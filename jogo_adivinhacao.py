#jogo_adivinhacao.py

import random

def jogar():


    print("==================================")
    print("Bem vindo ao jogo de Adivinhação #")
    print("==================================")

    #gera um número aleatório entre 1 e 100
    numero_secreto = random.randrange(1,101)
    pontuacao = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Fácil   (2) Médio  (3) Difícil')
    nivel = int(input('Defina o nível:'))


    if (nivel == 1):    
        total_tentativas = 20 #Fácil
    elif (nivel == 2):
        total_tentativas = 10 #Médio
    elif (nivel == 3):
        total_tentativas = 5  #Difícil
    else:
        print('Nível inválido!')
        total_tentativas = 0
           

    for tentativa in range(total_tentativas):
        print(f'Tentativa {tentativa + 1} de {total_tentativas}')

        #le uma string e converte em inteiro
        chute = int(input('Digite um número entre 1 e 100:'))


        if (chute < 1 or chute > 100):
            print('Chute deve estar entre 1 e 100')
            continue

        #acertei
        if (chute == numero_secreto):
            print('Acertou')
            break #interrompe o loop
        #errei
        else:
           pontos_perdidos = abs(numero_secreto - chute)
           pontuacao -= pontos_perdidos
            
           if (chute > numero_secreto):
                print('Errou! seu chute foi menor que o número secreto')        

           else: 
                print('Errou! seu chute foi menor que o número secreto')


    print('Fim do jogo')
    print(f'O número secreto é {numero_secreto}. Voce fez {pontuacao}')


#jogar()

#print(__name__) #executa o main (próprio arquivo)


#só executa o jogo quando eu rodo DIRETAMENTE (sem importar)
if (__name__) == '__main__':
    jogar()



