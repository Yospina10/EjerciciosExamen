#1. Construir un programa que permita ingresar 20 números enteros y cuenta cuantos números negativos fueron ingresados

print("Contar los números enteros y números negativos")

Enteros = 1
Neutros = 0
Negativos = 0
Positivos = 0

while (Enteros<=20):
    n = int(input(f'Digite el número {Enteros}: '))
    if(n==0):
        Neutros+=1
    elif(n<0):
        Negativos+=1
    else:
        Positivos+=1
        Enteros+=1

print(f'{Neutros}Son numeros neutros')
print(f'{Negativos}Son numeros negativos')
print(f'{Positivos}Son numeros positivos')