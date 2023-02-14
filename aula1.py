Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=1
a
1
b=2
c=a+b
c
3
a
1
b
2
c
3
print(c)
3
print(c)
3
print(1+2*3/4-1)
1.5
a=1
b=2
c=3
d=4
print(a+b/c*d-a)
2.6666666666666665
print((a+b) / c * (d - a))
3.0
print("(a+b/c")
(a+b/c
print ('a+b/c')
 
a+b/c
print('a+b"c"')
 
a+b"c"
a
 
1
print('Valor de a', a)
 
Valor de a 1
 print('a')
 
SyntaxError: unexpected indent
print('Soma = ', 1+2)
 
Soma =  3
print('Subtração = ', 2 - 1)
 
Subtração =  1
print('Multiplicação = ', 4 * 3)
 
Multiplicação =  12
print('Divisao = '. 4 / 3)
 
SyntaxError: invalid syntax
print('Divisao = ', 4/3)
 
Divisao =  1.3333333333333333
4//3
 
1
4/3
 
1.3333333333333333
5/2
 
2.5
print('Divião interira', 5//2)
 
Divião interira 2
a
 
1

================================ RESTART: Shell ================================
a
 
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a
NameError: name 'a' is not defined
9%2
 
1
55%4
 
3
3*3
 
9
2*2*2
 
8
2 ** 3
 
8
9 ** 3
 
729
print('Potência:', 2 ** 3)
 
Potência: 8
#sqaure root = raiz quadrada
 
#isto é um comentário
 
print('hello') #comentario
 
hello
#módulo do python
 
#math
 
import math
math.sqrt(9)
3.0
math.sqrt(81)
9.0
2 ** 3
8
math.pow(2,3)
8.0
2 ** 3
8
math.pi
3.141592653589793


#operadores relacionais
4<5
True
10<2
False
5<5
False
5<=5
True
5>=5
True
5>5
False
5 = 5
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
5 == 5
True
5 == 4
False
a=1
b=1
a == b
True
c=2
a == c
False
2 != 5
True
5 != 5
False
5 ! = 5
SyntaxError: invalid syntax
5 != 5
False
5 == 5.0
True
'uva' == 'banana'
False
'5' == '5.0'
False
'uva' > 'banana'
True
'uva' != 'banana'
True
not True
False
not False
True
5 == 4
False
(5 == 4)
False
not (5 == 4)
True
not (5 != 4)
False
not (not (5 !=4))
True
not (not (not false))
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    not (not (not false))
NameError: name 'false' is not defined. Did you mean: 'False'?
not (not (not False))
True
true and true
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    true and true
NameError: name 'true' is not defined. Did you mean: 'True'?
True and True
True
True and False
False
True and True and True and True and False
False
True or True
True
True or False
True
True or True or False or False or True or True
True
False or False
False
preco = 1.99
quantidade = 5
print(preco, quantidade)
1.99 5
print ('Preço da banana', preco, 'quantidade', quantidade)
Preço da banana 1.99 quantidade 5
print ('Preço da banana R$', preco, 'quantidade', quantidade, 'kg')
Preço da banana R$ 1.99 quantidade 5 kg
print('%s', 'banana')
%s banana
 quantidade 5 kg

SyntaxError: unexpected indent
print('%s', % 'banana')
SyntaxError: invalid syntax
print('%s' % 'banana')
banana
type(5)
<class 'int'>
type(5.0)
<class 'float'>
type(3,14)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    type(3,14)
TypeError: type() takes 1 or 3 arguments
>>> type(3.14)
<class 'float'>
>>> print('%d' % 123)
123
>>> print('%f' % 123)
123.000000
>>> print('%.2f' % 123)
123.00
>>> print('%.1f' % 123)
123.0
>>> print('%.2f' % math.pi)
3.14
>>> print('%s = %.2f' % ('Preço da banana', preco))
Preço da banana = 1.99
>>> print('%s = R$%.2f' % ('Preço da banana', preco))
Preço da banana = R$1.99
>>> print('%s = R$ %.2f' % ('Preço da banana', preco))
Preço da banana = R$ 1.99
>>> print('n\n\nFIM')
n

FIM
>>> print('\n\n\nFIM')



FIM
>>> print('*\t*\t*\tFIM')
*	*	*	FIM
>>> print('hello','world')
hello world
>>> print('hello', end='*')
hello*
>>> print('hello', end='*')
hello*
>>> print('hello', end='')
hello
>>> print('hello', end='')
hello
