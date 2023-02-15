#conjuntos.py
#Listas:   [1,2,3,4,5]

#Tuplas:   (1,2,3,4,5)

#Conjunto
#Um conjunto é uma coleçãi desordenada de elementos, sem repetição

frutas = {"uva", "laranja", "banana", "laranja", "uva", "banana"}
print(frutas)

a = set("abracadabra")
print(a)

b =  set("alacazam")
print(b)


palavra = "abracadabra"
for x in palavra:
    if x not in "abc":        
        print(x, end= ' ') #r d r 

#idem exemplo anterior com set comprehension = compreensão de conjunto)
print('\n')
c = {x for x in "abracadabra" if x not in "abc"}
print(c)    #{r,d}

#converte um conjunto em uma lista
print(list(frutas))

#converte um conjunto em uma tupla
print(tuple(frutas))



  
