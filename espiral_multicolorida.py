#espiral_multicolorida

import turtle

turtle.bgcolor('black') #cor de fundo
p = turtle.Pen()

cores = ['red', 'yellow', 'blue', 'green']

for x in range(100): #0,99...
    p.pencolor(cores[x % 4]) #0,1,2,3
    p.circle(x * 5)
    p.left(91)
