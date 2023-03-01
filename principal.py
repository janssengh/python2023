from carro import Carro
from motociicleta import Motocicleta
from veiculo import Veiculo

if __name__ == '__main__':
    gol = Veiculo('VW', 'Gol', 'GOL-1234', 2016)
    fusca = Carro('VW', 'Fusca', 'FUS-1234', 1963)
    moto = Motocicleta('Honda', 'Titan', 'MMM-4567', 2020, 6)
    print(gol)
    gol.abastecer(30)
    gol.ligar()
    print(gol.isligado)

    gol.desligar()
    print(gol.isligado)

    fusca.ligar()
    print(fusca)

    print(moto)
    moto.abastecer(10)

