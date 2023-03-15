#criar pasta: aula11
#Programação funcional
#1. Usando funções normais (comuns)
#Salvar como: funcional_funcoes.py


#definie uma função com 2 parâmetros
#e retorna a multplicação
def transformar(x, y):
    return x * y

#define função para comparação
def iguais(x, y):
    if x == y:
        return "Sim"
    else:
        return "Não"

if __name__ == '__main__':
    resultado = transformar(2,3)
    print(resultado)  #6
    print(iguais(5,6))  #Não
    print(iguais(7,7))  #Sim
