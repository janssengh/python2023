#lista.py

#Lista é um tipo de estrutura de dados muitoi usada na área
#de ciência de computação, sendo talvez a mais importante,
#e com certeza a mais importante no python

#cria uma lista de strings
ListaFrutas = ['banana', 'laranja', 'uva', 'abacate', 'kiwi']

#cria uma lista de números
ListaNumeros = [5,10,20,30,40,222,1001]

#cria uma lista mista
ListaMista = ['texto', 3.14, 1, 2, 3, 'mil', 'Brasil', 999]

#imprime o primeiro item da lista
print(ListaFrutas[0])

#imprime o segundo item da lista
print(ListaFrutas[1])

#imprime o terceiro item da lista
#F5 para rodar!
print(ListaFrutas[2])

#IndexError: list index out of range
# não existe o índice 3
#print(ListaFrutas[3])

#imprime o último item
print(ListaFrutas[-1])

#imprime lista mista
print(ListaMista[0])
print(ListaMista[1])
print(ListaMista[2])
print(ListaMista[-1]) # último item da lista:999

print('\nimprimindo a lista completa com for')
for item in ListaMista:
    print(item)

#imprimindo a lista completa: imprime a estrutura de dados
print(ListaMista)

#remove um item da lista
ListaMista.remove('Brasil')
print(ListaMista)

#remove o último da lista
ultimo = ListaMista.pop()
print('Removeu com pop:', ultimo)
print(ListaMista)

print('\nlista de frutas:', ListaFrutas)
#junta(anexa) um item nmo final da lista
ListaFrutas.append('morango')
ListaFrutas.append('melancia')
print('\nlista de frutas:', ListaFrutas)

ListaFrutas.sort()
print('\nordena em ordem alfabética:', ListaFrutas)

#inverte a ordemn
ListaFrutas.reverse()
print('\nordem reversa:', ListaFrutas)

ListaCategorias = ['vw', 'ford', 'fiat', 'gm', 'bmw']
ListaMarcasCarros = ['vw', 'fiat', 'ferrari', 'mercedes', 'audi']

#quero imprimir somente as marcas de carro que fazem parte da minha
#ListaCategorias
for marca in ListaMarcasCarros:
    #verifica se marca está dentro da ListaCategorias: 
    if marca in ListaCategorias:
        print(marca) #vw fiat

print('\nLista composta por sublistas')
#lista composta por sublistas
ListaValores = [1,2,[3,4,5],6,[7,8,9]]
print(ListaValores)
print(ListaValores[0])
print(ListaValores[1])
print(ListaValores[2])
print(ListaValores[3])
print(ListaValores[4])

print('\nImprimindo a lista com for')
for item in ListaValores: print(item)

#imprimindo o valor 4 e 9 da lista de valores
print(ListaValores[2][1]) #4
print(ListaValores[4][2]) #9

#0   1  2  3  4  5   6
#[5,10,20,30,40,222,1001]
print('\nLista de números:', ListaNumeros)

#fazendo uma seleção na lista de números (intervalo de posições => :)
#imoprime da posição 0 até a 3, pois 4 é exclusivo (exclui)
print(ListaNumeros[0:4])

#imprime entre 1 e 5
print(ListaNumeros[1:6])

#imprime da posição 2 até o penúltimo, pois -1 é o último (exclui)
print(ListaNumeros[2:-1])

#imprime da posição 2 até o final!
print(ListaNumeros[2:])

#imprime do inicio até a posição 3
print(ListaNumeros[:4])

#imprime a lista toda
print(ListaNumeros[:])
#ou
print(ListaNumeros)

#Copiando variáveia
#não faz uma cópia, pois cria uma referencia
a = ListaNumeros

#Copiando variáveia
#faz uma cópia, pois copia itens
a = ListaNumeros[:]

#também copia - Identico ListaNumeros[:]
a = ListaNumeros.copy()

#para contar o número de itens da lista
print('Tamanho da lista:', len(ListaNumeros)) #7 = 0..6

#apaga todos os itens da lista
ListaFrutas.clear()
print(ListaFrutas) #[]

#juntar listas
lista1 = [0,1,2]
lista2 = [3,4,5]
todas = lista1 + lista2
print(todas)  #[0,1,2,3,4,5]

#copia conteudo da lista, dentro da propria lista
print(todas * 2)
#ou
print(3 * todas)

#lista de notas
notas = [7.2,5.4,3.3,8.1,9.0,9.0]

#contando as notas
print('Quantidade de notas:', len(notas))

#contando quanto notas 9 existem na lista
print('Quantiade de 9.0:', notas.count(9.0))

#calculando a nota mínima
print('Nota mínima:', min(notas))

#calculando a nota maxima
print('Nota máxima:', max(notas))

#calculando a média das notas
print('Media das notas:', sum(notas) / len(notas))

#lista de compras
ListaCompras = ['leite', 'ovos', 'manteiga', 'pão', 'queijo', 'mortadela']
print('pão' in ListaCompras) #True

#não existe 'carne' na lista de compras
print ('carne' not in ListaCompras) #True

#em qual posição da lista está o pão?
print("Posição de 'pão' na lista:", ListaCompras.index('pão'))

#troca 'pão' por 'pão francês'
posicao = ListaCompras.index('pão')
ListaCompras[posicao] = 'pão francês'
print(ListaCompras)

print('\npercorrendo a lista de compras com for')
for x in ListaCompras:
    print(x)
for x in ListaCompras:
    print(x)

print('\npercorrendo a lista com list comprehension')
print([x for x in ListaCompras])

#que é o mesmo de
print(ListaCompras)

#imprime as notas x vezes 2
print([x * 2 for x in notas])

#similar , porém menos eficiente
for x in notas:
    print(x * 2)


#===== tupla ======

#uso parenteses para definir uma tupla
tuplaNumeros = (10,20,30,700,1001)

#ou não usa nada!
tuplaFrutas = 'banana', 'laranja', 'uva'
print(tuplaFrutas[0])
print(tuplaFrutas[1])

#não permite acrescentar
#tuplaFrutas.append('kiwi')

#não permite remover
#tuplaFrutas.remove('uva')

#não permite alterar
#tuplaFrutas[0] = 'kiwi'

#=====> uma tupla é similar a uma lista, porém IMUTÁVEL

#além de lista e tupla temos:
#conjunto e dicionário
















