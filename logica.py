#logica.py




temp = float(input('Entre com a temperatura:'))

"""
Previsão do tempo

Regras de Negócio:
quando a temperatura for menor que 0 = Congelando
quando a temperatura for maior oou igual a 0 e  menor ou iguaL A 20 = Frio
quando a temperatua maior ou igual a 21 e menor ou igual a 25 = Normal
quando a temperatua maior ou igual a 26 e menor ou igual a 35 = Quente
quando a temperatua maior que 35 = Muito Quente
"""

if temp < 0:
    print('Congelando...')
    
elif 0 <= temp <= 20: 
    print('Frio')

elif 21 <= temp <= 25:
    print('Normal')

elif 26 <= temp <= 35:
    print('Quente')

else:
    print('Muito Quente')



