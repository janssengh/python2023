#funções.py

#uma função deve ter um objetivo único e ser pequena
#você pode pensar em uma fumção como sendo um verbo!

#exemplo: funções de um carro
#o nome da função deve estar em formato camlCase, com parenteses
#rodarNaRodovia()
#precisamos incluir a palavra def (define função) antes do nome


#aqui apenas definimos as funções
def rodar():
    print('rodando...')



def acelerar():
    print('acelerando... vrummm')


#o parentêses serve para receber um parâmetro
def abastecer(litros):
    preco = 5.5 #preço litro gasolina
    total = litros * preco
    print('abastecendo...', litros, 'litros por R$', total)


#uma função basicamente é uma rotina específica
#(nada a ver com o carro)
def contador():
    for x in range(10):
        print(x)


#depois de definir, podemos chamar (ou não)
abastecer(50)
acelerar()
rodar()

contador()




