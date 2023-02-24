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
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print('Chamou o construtor')

    def __str__(self):
        return f'Número: {self.numero}, \tTitular: {self.titular}, \tSaldo: {self.saldo}, \tLimite: {self.limite}'

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
       saldo_disponivel = self.__saldo + self.__limite
       return valor <= saldo_disponivel

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            return True
        else:
            return False

    def transferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        else:
            return False


    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    #define que o método é estático, ou seja, pertence à classe Conta e não aos objetos
    @staticmethod
    def codigo_banco():
        return{'BB: 001'}


