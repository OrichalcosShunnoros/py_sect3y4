"""
Programa que muestra si un número es divisible entre cinco.
Autor: Christian Zambrano
Fecha: Diciembre 6 de 2023
"""


#Cree un programa que lea un número y muestre si éste es divisible entre cinco o no.


numero = int(input("Ingrese un número: "))

if numero % 5 == 0:
    print(f"El número {numero} es divisible por cinco.")
else:
    print(f"El número {numero} no es divisible por cinco.")
