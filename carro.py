#carro.py
from veiculo import Veiculo


class Carro(Veiculo):

    def __str__(self):
        return f'Carro: marca: {self.marca} \tmodelo: {self.modelo} \tplaca: {self.placa} \tano: {self.ano}'
