#matriz.py
#matriz usando python puro (usando a lista)



#lista de números
numeros = [10,50,70,90]
soma = 0

for x in numeros:
    soma += x
    print(soma)
    
print(soma)

print(sum(numeros))

matriz = [
            [3, 0],
            [2, -1],
            [5, 7]
        ]

print('matriz:',matriz)
print('matriz[0]:', matriz[0])
print('matriz[1]:',matriz[1])
print('matriz[2]:',matriz[2])

print('\nmatriz[0][0]:', matriz[0][0])
print('matriz[0][1]:',matriz[0][1])

print('\nmatriz[1][0]:', matriz[1][0])
print('matriz[1][1]:',matriz[1][1])

print('imprimindo com for')
for linha in matriz:
    print(linha)

print('imprimindo com for * 2')
for linha in matriz:
    for col in linha:
        print(col * 2, end=' ')
    print() #pula linha
