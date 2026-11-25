# # Sesion 3 TIPOS DE DATOS

# # --- ENTEROS ---
# edad = 25
# cantidad = 10
# temperatura = -50

# # --- FLOTANTES ---
# precio = 10.5
# pi = 3.1416
# peso = 25.2

# print(edad, cantidad, temperatura, precio, pi, peso)

# # --- BOOLEANOS ---
# disponible = True
# pagado = False

# print(disponible, pagado)

# # --- type() ---
# print(type(temperatura))
# print(type(pi))
# print(type(disponible))

# # que pasa si no convierto el tipo de dato
# print(edad + disponible)


# registro de ventas
producto = input("Ingresa nombre de producto: ")
cantidad = int(input("Ingrese la cantidad vendida: "))
precio = float(input("Ingrese el precio unitario: "))

total = cantidad * precio
print("\nProducto:", producto, "\nTotal:", total)

