"""
Programa que muestra el número mayor o igual entre dos números.
Autor: Christian Zambrano
Fecha: Octubre 6 de 2023
"""

#Cree un programa que reciba dos números y muestre el mayor. En caso de que los números sean iguales
#también se debe mostrar al usuario.

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

if n1 > n2:
    print(f"El número mayor es: {n1}")
elif n2 > n1:
    print(f"El número mayor es: {n2}")
else:
    print("Los números son iguales.")
