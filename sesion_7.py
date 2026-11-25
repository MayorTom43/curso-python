# # CICLO FOR
# guias = ["G001", "G002", "G003", "G004", "G005", "G006"]

# for memoria in guias:
#     print("Revisando envio:", memoria)

# # FOR + RANGE
# for numero in range(2):
#     print("revisando envio:",guias[numero])
    
# for numero in range(2,5):
#     print("revisando envio:",guias[numero])

# # CONTADORES
# cont = 0

# for memoria in guias:
#     cont += 1
#     print("Revisando", memoria)

# print("Total:", cont)

# # ACUMULADOR
# distancias = [15, 22 , 10, 18]

# distancia_total = 0

# for distancia in distancias:
#     distancia_total += distancia
    
# print("distancia total:", distancia_total)

# # WHILE
# intento = 1
# while intento <= 3:
#     print("intento de envio:", intento)
#     intento += 1
    
# # EJERCICIO
# envios = [
#     {"estado": "ENTREGADO"},
#     {"estado": "EN RUTA"},
#     {"estado": "DEVUELTO"},
#     {"estado": "ENTREGADO"},
#     {"estado": "DEVUELTO"},
#     {"estado": "ENTREGADO"}
# ]
# entregados = 0
# en_ruta = 0
# devueltos = 0

# for envio in envios:
#     if envio["estado"] == "ENTREGADO":
#         entregados += 1
#     elif envio["estado"] == "EN RUTA":
#         en_ruta += 1
#     else:
#         devueltos += 1
        
# print("RESUMEN DE ENVIOS")
# print("ENTREGADOS:", entregados, "\nEN RUTA:", en_ruta, "\nDEVUELTOS:", devueltos)

# WHILE 
# INTENTOS DE ENTREGAS

guia = "G001"
intentos = 0
entregados = False

while intentos < 3 and entregados == False:
    intentos += 1
    
    print("guia", guia)
    print("intentos de entrega:", intentos)

resultado = input("se entregó el paquete? (S/N):  ").lower()

if resultado == "s":
    entregados = True
else:
    entregados = False
if entregados:
    print("Envio entregado")
else:
    print("envio devuelto")