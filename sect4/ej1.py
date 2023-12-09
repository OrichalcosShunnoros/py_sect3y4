"""
Programa que muestra su los ángulos corresponden a los de un triángulo
Autor: Christian Zambrano
Fecha: Diciembre 6 de 2023
"""
#Cree un programa que lea los tres ángulos internos de un triángulo y muestre si los ángulos corresponden a un triángulo o no.

a1 = float(input("Ingrese el primer ángulo: "))
a2 = float(input("Ingrese el segundo ángulo: "))
a3 = float(input("Ingrese el tercer ángulo: "))

if a1 + a2 + a3 == 180:
    print("La suma de los ángulos es correspondiente a un triángulo.")
else:
    print("La suma de los ángulos no es correspondiente a un triángulo.")
