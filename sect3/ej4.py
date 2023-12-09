"""
Programa que muestra el mayor o igual entre 3 números.
Autor: Christian Zambrano
Fecha: Octubre 6 de 2023
"""

#Cree un programa que reciba tres números y muestre el mayor. En caso de que los números sean iguales
#también se debe mostrar al usuario.

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 == n2 and n2 == n3:
    print("Los números son iguales.")
else:
    ma = max(n1, n2, n3)
    print(f"El número mayor es: {ma}")
