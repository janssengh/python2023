#espiral_circulo.py

import turtle


#atalho de turtle
p = turtle.Pen() # é a caneta da tartaruga
p.pencolor('red')

for x in range(100):
    p.circle(x * 5)
    #gira 4 graus a cada volta
    p.left(91)
