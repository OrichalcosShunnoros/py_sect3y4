"""
Programa que verifica si un número es par o no.
Autor: Christian Zambrano
Fecha: Diciembre 6 de 2023
"""

#Cree un programa que lea un número y muestre si éste es par o impar.

n = int(input("Ingrese un número: "))

if n % 2 == 0:
    print("El número que ingresaste, es par.")
else:
    print(f"El número que ingresaste, es impar.")
