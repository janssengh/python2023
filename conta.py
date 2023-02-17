#Orientação à Objetos em Python
#
#métodos principais de uma classe
# -método construtor ou inicializador: __init__
# -propriedades: são métodos anotados com @property
# -setters: são métodos para modificação do objeto anotados com @xxxxx.setter (só escrita)
# -métodos estáticos: anotados com @staicmethod

#atributos ou variáveis de uma classe:
# -atributos públicos. Exemplo: self.variavel  (pode ler e alterar)
# -atributos privados. Exemplo: self.__variavel (não pode ler, nem alterar)
# -as variáveis são criadas dentro do construtor

#sintaxes:
# - nome do arquivo em minúsculas. Exemplo: conta.py
# - nome da classe em maiúsculas. Ecemplo: class Conta

#Métodos builtin (métodos prontos):
# - são métodos herdados da classe mãe Objetct, no formato: __xxxxx__
# - um métodos bultin pode ser reescrito!

class Conta:
    #método construtor ou inicializador: é o primeito método chamado quando criamos um objeto
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        print('Chamou o construtor')

    def __str__(self):
        return f'Número: {self.numero}, \tTitular: {self.titular}, \tSaldo: {self.saldo}, \tLimite: {self.limite}'


if __name__ == '__main__':
    #cria um objeto contaJoao a partir da classe Conta() e executa o construtor automaticamente
    contaJoao = Conta(123, 'João da Silva', 1000, 3000)
    print(contaJoao)

    #segundo objeto
    contaMaria = Conta(456, 'Maria da Silva', 1500, 5000)
    print(contaMaria)
