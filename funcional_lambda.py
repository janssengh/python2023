#Programação funcional
#2. Usando lambda
#Salvar como: funcional_lambda.py

#def transformar(x, y):
#    return x * y

#lambda representa uma função anônima
transformar = lambda x, y: x * y

#lambda usando operador ternário (substitui if else)
iguais = lambda x, y: "Sim" if x == y else "Não"

if __name__ == '__main__':
    resultado = transformar(2,3)
    print(resultado)  #6
    print(iguais(5,6))  #Não
    print(iguais(7,7))  #Sim
    

    
