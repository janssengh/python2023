#veiculo.py

#classe mãe
class Veiculo:

    #construtor da classe
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.combustivel = 5
        self.__ligado = False  #boolean: True ou False


    def __str__(self):
        return f'Veiculo: marca: {self.marca} \tmodelo: {self.modelo} \tplaca: {self.placa} \tano: {self.ano}'

    def abastecer(self, litros):
        self.combustivel += litros
        print(f'Abastecendo veiculo...{litros} litros. Total do tanque: {self.combustivel}')

    def ligar(self):
        self.__ligado = True
        print('Veiculo ligado!')

    def desligar(self):
        self.__ligado = False
        print('Veiculo desligado!')

    #está ligado?
    @property
    def isligado(self):
        return self.__ligado
