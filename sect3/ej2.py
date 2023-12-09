"""
Programa que muestra sí el producto paga IVA.
Autor: Christian Zambrano
Fecha: Octubre 6 de 2023
"""

#En un supermercado se tiene los siguientes productos: lentejas, crema, arroz y vino. Las lentejas y el arroz no
#pagan IVA, el vino y la crema si. Cree un programa que reciba el nombre de alguno de los productos
#mencionados y muestre si el producto paga IVA o no.

prods = ["lentejas", "crema", "arroz", "vino"]

prod = input("Ingrese el nombre del producto: ")

if prod in prods:
    if prod == "lentejas" or prod == "arroz":
        print("El producto no paga IVA.")
    else:
        print("El producto paga IVA.")
else:
    print("Producto no encontrado en la lista.")
