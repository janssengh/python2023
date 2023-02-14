#carro.py

#Programação Orientada à Objetos = POO
#(Oriented Object Programming = OOP)
#define a classe Carro
class Carro:

    #função de inicialização ou função construtora
    def __init__ (self, marca, modelo, placa, ano): #self = gol
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def ligar(self):
        print(f'{self.modelo} ligado')

    def desligar(self):
        print(f'{self.modelo} desligado')

    def abastecer(self):
        print(f'{self.modelo} abastecendo...')

    #funções builtin do python (funções prontas)
    def __str__(self):
        return f'Marca:{self.marca} \tModelo:{self.modelo} \tPlaca:{self.placa} \tAno:{self.ano}'





#cria um objeto de carro gol
gol = Carro('VW', 'Gol', 'GOL-1234', 2010)

#chama as funções do objeto gol
gol.ligar()
gol.desligar()
gol.abastecer()

#chama automaticamente a função __str__
print(gol)





#cria um palio
#cria um objeto de carro palio
palio = Carro('FIAT', 'Palio', 'PALIO-3456', 2011)

#chama as funções do objeto gol
palio.ligar()
palio.desligar()
palio.abastecer()

#chama automaticamente a função __str__
print(palio)


