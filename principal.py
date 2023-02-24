from conta import Conta

if __name__ == '__main__':
    #cria um objeto contaJoao a partir da classe Conta() e executa o construtor automaticamente
    contaJoao = Conta(123, 'João da Silva', 1000, 3000)
    print(Conta.codigo_banco())

    #contaJoao.sacar(300)

    contaMaria = Conta(456, 'Maria da Silva', 0, 3000)
    print(Conta.codigo_banco())

    if contaJoao.transferir(500, contaMaria):
        print('Transferiu com sucesso!')
    else:
        print('Não tem saldo suficiente para transferir')
    #print(contaJoao)
    #print(contaMaria)

    contaJoao.limite = 9000

    print(contaJoao.saldo)
    print(contaJoao.limite)
    print(contaJoao.titular)
    print(contaJoao.numero)

    # não pode usar para alterar por ser privado - contaJoao.numero = 999