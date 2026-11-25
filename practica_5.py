# crear dos diccionarios de productos
auto_1 = {
    "marca": "KIA",
    "modelo": "sportage 2026",
    "color": "gris",
    "precio": "125M"
}
auto_2 = {
    "marca": "MAZDA",
    "modelo": "CX30 2024",
    "color": "rojo",
    "precio": "87M"
}

# guardar productos en una lista
concesionario = [auto_1, auto_2]
print(concesionario)

# consultar el nombre del primer producto
print("marca del 1er vehiculo: ", concesionario[0]["marca"])

# modificar el precio de un producto
concesionario[1]["precio"] = "110M"
print("Nuevo precio del", concesionario[1]["marca"], "es", concesionario[1]["precio"])

# crear categoria
