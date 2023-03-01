#motocicleta.py
from veiculo import Veiculo


class Motocicleta(Veiculo):

    def __init__(self, marca, modelo, placa, ano, cilindrada):
        super().__init__(marca, modelo, placa, ano)
        self.__cilindrada = cilindrada

    def __str__(self):
        return f'Motocicleta: marca: {self.marca} \tmodelo: {self.modelo} ' \
                f'\tplaca: {self.placa} \tano: {self.ano} \tCilindrada: {self.__cilindrada}'

