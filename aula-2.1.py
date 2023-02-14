Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: C:/Curso Python Roeland/Aula2/espiral_escolha.py ==========

=========== RESTART: C:/Curso Python Roeland/Aula2/espiral_escolha.py ==========
chr(65)
'A'
chr(66)
'B'
chr(67)
'C'
chr(80)
'P'
chr(85)
'U'
chr(90)
'Z'
for x in range(65, 91):
    prfint(chr(x))

    
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    prfint(chr(x))
NameError: name 'prfint' is not defined. Did you mean: 'print'?
for x in range(65, 91):
    print(chr(x))

    
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
chr(97)
'a'
97+26
123
>>> chr(122)
'z'
>>> for x in range(97,123):
...     print(chr(x), end=' ')
... 
...     
a b c d e f g h i j k l m n o p q r s t u v w x y z 
>>> 
>>> ord('A')
65
>>> ord('B')
66
>>> palavra = 'banana'
>>> palavra[0]
'b'
>>> palavra[1]
'a'
>>> palavra[2]
'n'
>>> for c in palavra:
...     print(c, end='')
... 
...     
banana
>>> for c in palavra:
...     print(ord(c), end='')
... 
...     
98971109711097
>>> for letra in 'Roeland':
...     print(ord(letra), end='')
... 
...     
8211110110897110100
>>> 
>>> def gerador_senha():
...     palavra = inpút('Digite uma palavra:')
...     print('Senha =', end='')
...     for c in palavra:
...         print(ord(c), end='')
... 
>>> gerador_senha()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    gerador_senha()
  File "<pyshell#37>", line 2, in gerador_senha
    palavra = inpút('Digite uma palavra:')
NameError: name 'inpút' is not defined. Did you mean: 'input'?
>>> def gerador_senha():
...     palavra = input('Digite uma palavra:')
...     print('Senha =', end='')
...     for c in palavra:
...         print(ord(c), end='')
... 
>>> gerador_senha()
Digite uma palavra:ola como vai
Senha =1111089732991111091113211897105
