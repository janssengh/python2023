#Programação funcional
#2. Usando map
#Salvar como: funcional_map.py

#o map é usado para percorrer uma lista automaticamente

#Problema: converter a lista de strings em inteiros
lista = ['1', '2', '5', '7', '9']

#Método 1: usando for
novaLista = []
for x in lista:
    novaLista.append(int(x))

print('Resultado conversão for:', novaLista)

#Método 2: usando compreensão de lista (list comprehension)
novaLista = [int(x) for x in lista]
print('Resultado conversão list comprehension:', novaLista)

#Método 3: usando map com função nomeada
def converter(x):
    return int(x)

#'1', '2', '5', '7', '9'
#map -> pegue cada valor da lista e aplique a função converter!
#e no final,me devolva uma lista
novaLista = list(map(converter, lista))
print('Resultado conversão com map e função nomeada:', novaLista)


#Método 4: usando map com função anônima (lambda)
novaLista = list(map(lambda x: int(x), lista))
print('Resultado conversão com map e lambda:', novaLista)

#Outro  exemplo com lambda
lista2 = ['1.0', '3.1', '4.8', '9.99', '55.5']
novaLista = list(map(lambda x, y: [int(x), float(y)], lista, lista2))
print('Resultado conversão de duas listas::', novaLista)
#[[1, 1.0], [2, 3.1], [5, 4.8], [7, 9.99], [9, 55.5]]

#Outro
numeros = (1,2,3)
resultado = tuple(map(lambda a: a + a, numeros))
print('Conversão de tupla de numeros:', resultado)
#(2, 4, 6)

#Mais um
numeros2 = [4,5,6]
resultado = list(map(lambda a, b: a + b, numeros, numeros2))
print('Último exemplo:', resultado)
#[5, 7, 9]

