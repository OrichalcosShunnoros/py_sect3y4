"""
Programa que dice un número del 1 al 15 es primo o no
Autor: Christian Zambrano
Fecha: Diciembre 6 de 2023
"""


#Cree un programa que lea un número entre 1 y 15 y muestre si éste es primo o no.

n = int(input("Ingrese un número entre 1 y 15: "))

if 1 < n <= 15:
    prim = True
    for i in range(2, n):
        if n % i == 0:
            prim = False
            break
    if prim:
        print(f"El {n} es un número primo.")
    else:
        print(f"El {n} no es un número primo.")
else:
    print("Ingrese un número válido entre 1 y 15.")
