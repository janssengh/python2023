#espiral_escolha.py

import turtle

p = turtle.Pen()

turtle.bgcolor('black')
p.speed(0)

# voce pode escolher entre 2 e 6 lados para obter formas diferentes
lados = int(turtle.numinput('Escolha entre 2 e 6', 'Número de lados'))
cores = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

for x in range(300):
    p.pencolor(cores[x%lados])
    #tamanho da linha   
    p.forward(x * 3 / lados + x)
    #calcula o ângulo de acordo com o número de lados
    p.left(360 / lados + 1)
    #espessura da linha
    p.width(x * lados / 200)
