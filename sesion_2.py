producto = input("Ingresa producto: ")
cantidad = input("Ingresa la cantidad: ")
precio = input("Ingresa el precio del producto: ")

cantidad = int(cantidad)
precio_unitario = int(precio)

total = cantidad * precio_unitario

print("\n==== RESUMEN DE VENTA ====")
print("Su producto es:",producto,"\nLa cantidad es",cantidad,"\nEl precio x und es:",precio_unitario,"COP \nEl total es:",total)