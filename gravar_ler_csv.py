#gravar_ler_csv.py

import csv


#Le um aqrquivo do Excel formato .CSV
def lerCsv():
    #abre o arquivo para leitura
    arquivo = open('dados.csv', encoding='UTF-8')
    #le o arquivo e armazena na memória
    dados = csv.reader(arquivo, delimiter=';')
   

    #para cada linha de dados, imprima
    for linha in dados:
        print(linha)


#Grava um arquivo do Excel no formato .CSV
def gravarCsv():
    dados = (
        ('PRODUTO','UNIDADE','PREÇO UNITÁRIO','QUANTIDADE ESTOQUE','VALOR TOTAL'),
        ('Açúcar','2Kg',3.59,10,35.9),
        ('Biscoito','200 Gr',1.19,10,11.9)
         )

    #drefine o destino dos dados
    arquivo = open('dados2.csv', 'w', newline='', encoding='UTF-8')
    destino = csv.writer(arquivo)
    #escreve as tuplas no arquivo de destino
    destino.writerows(dados)
    print('Gravou')


if (__name__ == '__main__'):
    #lerCsv()
    gravarCsv()

        
