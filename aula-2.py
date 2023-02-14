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


5>4
True
4<5
True
5<4
False

5==5
True
if 5==5:
    print('igual')

    
igual


'a' == 'a'
True
'A' == 'a'
False


if 4 > 5:
    print('maior')
else:
    print('menor')

    
menor
if 6> 5:
    print('maior')
else:
    print('menor')

    
maior



letra = 'r'

if letra == 'r':
    print('l')
else:
    print(letra)

    
l

for x in frase:
    if x == 'r':
        print('l', end='')
    else:
        print(x, end='')

        
o lato loeu a loupa do lei de loma


frase
'o rato roeu a roupa do rei de roma'


5>4
True
5>4 or 6>3
True
if 5>4 or 6>3:
    print('todos maiores')

    
todos maiores
letra='R'
frase='o rato Roeu a roupa do Rei'


for letra in frase:
    if letra == 'r' or letra == 'R':
        print('l', end='')
    else:
        print(letra, end='')

        
o lato loeu a loupa do lei
o lato loeu a loupa do lei
SyntaxError: invalid syntax


frase
'o rato Roeu a roupa do Rei'

for letra in frase:
    if letra == ' ':
        print(letra)
    else:
        print(letra, end='')

        
o 
rato 
Roeu 
a 
roupa 
do 
Rei


frase.split()
['o', 'rato', 'Roeu', 'a', 'roupa', 'do', 'Rei']


for x in frase.split():
    print(x)

    
o
rato
Roeu
a
roupa
do
Rei

total = 0
for x in frase.split():
    total = total + 1

    
total
7

len(frase)
26
len(frase.split())
7
frase.split()
['o', 'rato', 'Roeu', 'a', 'roupa', 'do', 'Rei']
frase = input('Digite uma frase:')
Digite uma frase:aula 2 python

print('hello')
hello



def conta_letra():
    frase = input('Digite uma frase:')
    print('Quantidade de letras:'. len(frase))

    
def conta_letra():
    frase = input('Digite uma frase:')
    print('Quantidade de letras:', len(frase))

    
conta_letra
<function conta_letra at 0x000001CB87898040>
conta_letra()
Digite uma frase:aula 2 - curso python
Quantidade de letras: 21


frase
'aula 2 python'
frase = 'o rato roei a roupa'
frase.split('r')
['o ', 'ato ', 'oei a ', 'oupa']
frase
'o rato roei a roupa'


csv = 'CODIGO;PRODUTO;VALOR;QUANT'
csv.split(';')
['CODIGO', 'PRODUTO', 'VALOR', 'QUANT']


for col in csv.split(';'):
    print(col)

    
CODIGO
PRODUTO
VALOR
QUANT

for col in csv.split(';'):
    print(col, end' ')
    
SyntaxError: invalid syntax
for col in csv.split(';'):
    print(col, end('\n)
                   
SyntaxError: incomplete input
for col in csv.split(';'):
    print(col)

CODIGO
PRODUTO
VALOR
QUANT


for x in range(5,10):
    print(x)

                   
5
6
7
8
9
for x in range(100,200):
    print(x)

                   
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
for x in range(5,10):
    print(x, end=' ')

                   
5 6 7 8 9 
or x in range(100,200):
    print(x, end=' ')
                   
SyntaxError: invalid syntax
for x in range(100,200, 2):
    print(x,end=' ')

                   
100 102 104 106 108 110 112 114 116 118 120 122 124 126 128 130 132 134 136 138 140 142 144 146 148 150 152 154 156 158 160 162 164 166 168 170 172 174 176 178 180 182 184 186 188 190 192 194 196 198 

for x in range(100,0):
    print(x)

                   

for x in range(100,0,-5):
    print(x, end=' ')

                   
100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5 


for angulo in range(0, 360):
    print(angulo, end=' ')

                   
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 
>>> 
>>> for angulo in range(0, 360, 45):
...     print(angulo, end=' ')
... 
...                    
0 45 90 135 180 225 270 315 
>>> for angulo in range(0, 360, 30):
...     print(angulo, end=' ')
... 
...                    
0 30 60 90 120 150 180 210 240 270 300 330 
>>> for angulo in range(0, 360, 15):
...     print(angulo, end=' ')
... 
...                    
0 15 30 45 60 75 90 105 120 135 150 165 180 195 210 225 240 255 270 285 300 315 330 345 
>>> 
>>> 
>>> import turtle
>>> for comp in range(100):
...     turtle.forwad(x * 5)
...     turtle.left(45)
... 
...     
Traceback (most recent call last):
  File "<pyshell#246>", line 2, in <module>
    turtle.forwad(x * 5)
AttributeError: module 'turtle' has no attribute 'forwad'. Did you mean: 'forward'?
>>> for comp in range(100):
...     turtle.forward(x * 5)
...     turtle.left(45)
... 
...     

>>> for comp in range(100):
...     turtle.forward(comp * 5)
...     turtle.left(45)
... 
...     
