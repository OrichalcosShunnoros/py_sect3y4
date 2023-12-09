"""
Programa que muestra si el usuario es mayor de edad o no.
Autor: CZ
Fecha: 20 octubre de 2023
"""

# Cree un programa que lea la edad de un usuario e imprima un mensaje que diga si el usuario es mayor de edad o no.

ed = int(input("Ingrese la edad del usuario: "))
if ed >= 18:
    print("El usuario es mayor de edad.")
else:
    print("El usuario no es mayor de edad.")
