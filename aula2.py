Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
range(5)
range(0, 5)
list(range(5))
[0, 1, 2, 3, 4]

for x in range(5):
    print(x)

    
0
1
2
3
4
for x in range(10):
    print(x)

    
0
1
2
3
4
5
6
7
8
9
for var in range(7)
SyntaxError: incomplete input
for var in range(7)
SyntaxError: incomplete input
for var in range(7):
    print(var)

    
0
1
2
3
4
5
6
for minha_variavel in range(5):
    print(minha_variavel)

    
0
1
2
3
4
for a in range(5):
    print(a)

    
0
1
2
3
4
for a in range(5):
    print(A)

    
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    print(A)
NameError: name 'A' is not defined. Did you mean: 'a'?
for _ in range(5):
    print(_)

    
0
1
2
3
4
for b in range(5):
    print(b)

    
0
1
2
3
4
print(a)
0
print(5)
5
print('\n\n\n\n)
      
SyntaxError: incomplete input
print ('\n\n\n\n')
      





for x in range(10):
      print(x, end='')

      
0123456789
for x in range(10):
      print(x, end='*')

      
0*1*2*3*4*5*6*7*8*9*
for x in range(10):
      print(x, end='  ')

      
0  1  2  3  4  5  6  7  8  9  
import time
time.sleep(1)
time.sleep(5)



import time

for x in range(10):
    print(x, end=' ')
    time.sleep(1)

    
0 1 2 3 4 5 6 7 8 9 



lista = [0,1,2,3,4,5]
for x in lista:
    print(x)

    
0
1
2
3
4
5
lista = ['B', 'e', 'm', ' ', 'v', 'i', 'n', 'd', 'o']
lista
['B', 'e', 'm', ' ', 'v', 'i', 'n', 'd', 'o']
for x in lista:
    print(x)

    
B
e
m
 
v
i
n
d
o
for x in lista:
    print(x, end='')

    
Bem vindo

for x in lista:
    print(x, end=' ')
    time.sleep(1)

    
B e m   v i n d o 
for x in lista:
    print(x, end='\n')
    time.sleep(1)

    
B
e
m
 
v
i
n
d
o
frase = 'o rato roeu a roupa do rei de roma'


for x in frase:
    print(x)

    
o
 
r
a
t
o
 
r
o
e
u
 
a
 
r
o
u
p
a
 
d
o
 
r
e
i
 
d
e
 
r
o
m
a
or x in frase:
    print(x end=' ')
    
SyntaxError: invalid syntax
for x in frase:
    print(x)

    
o
 
r
a
t
o
 
r
o
e
u
 
a
 
r
o
u
p
a
 
d
o
 
r
e
i
 
d
e
 
r
o
m
a
for x in frase:
    print(x, end=' ')

    
o   r a t o   r o e u   a   r o u p a   d o   r e i   d e   r o m a 
for x in frase:
    print(x, end=' ')
    time.sleep(0.5)

    
o   r a t o   r o e u   a   r o u p a   d o   r e i   d e   r o m a 
for x in frase:
    print(x, end='')

    
o rato roeu a roupa do rei de roma
>>> 
>>> 
>>> 5>4
True
>>> 4<5
True
>>> 5<4
False
>>> 
>>> 5==5
True
>>> if 5==5:
...     print('igual')
... 
...     
igual
>>> 
>>> 
>>> 'a' == 'a'
True
>>> 'A' == 'a'
False
>>> 
>>> 
>>> if 4 > 5:
...     print('maior')
... else:
...     print('menor')
... 
...     
menor
>>> if 6> 5:
...     print('maior')
... else:
...     print('menor')
... 
...     
maior
