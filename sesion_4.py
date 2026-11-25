# sesion 4 - consultar cadenas de texto

producto = "computador"
print(producto[0]) 
print(producto[1])
print(producto[2])
print(producto[3])
print(producto[4])
print(producto[5])
print(producto[6])
print(producto[7])
print(producto[8])
print(producto[9])

# ejemplo f-string
nombre = "Laura"
edad = 30
print(f"Hola, me llamo {nombre} y tengo {edad} años.")

# posiciones positivas y negativas
print(producto[-3]) #d
print(producto[0]) #c
print(producto[-7]) #p

# extraer parte de una cadena de texto
print(producto[0:5]) #compu
print(producto[5:10])
print(producto[6:])
print(producto[:-3])
print(producto[2:-6])

# longitud de una cadena de texto
texto = "El café de la mañana"
longitud = len(texto)
print("La longitud de la cadena de texto es:", longitud)
print(texto.upper()) # pasar cadena a MAYUSCULA
print(texto.lower()) # pasar cadena a minuscula
print(texto.capitalize()) # primera letra en Mayuscula
print(texto.replace("a","i")) # reemplazar letra
print(texto + " s ") # agregar letra al inicio y final de la cadena
print(texto.strip()) # eliminar espacios sobrantes

# limpiar base de datos
nombre = "  JUAN CARLOS LOPEZ GONZALEZ   "
print(f"el nombre del usuario es: {nombre.strip().title()}")

# ejercicio
nombres = [
    "    MARIA GOMEZ   ",
    " juan perez",
    " ANA LOPEZ    "
]

print("El primer nombre es:", nombres[0])
print("Limpiamos el primer nombre:", nombres[0].strip())
print("Convertimos a formato titulo:",nombres[0].strip().title())
