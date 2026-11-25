# sesion 5
# diccionarios

televisores = {
    "marca": "Samsung",
    "precio": 5400000,
    "pulgadas": 50,
    "color": "negro",
    "resolucion": "4k"
}

# print(televisores["marca"])
# print(televisores["precio"])
# print(televisores["pulgadas"])
# print(televisores["resolucion"])

# consultar informacion get
#corchetes
#print(televisores["precio"])

#llaves
# print(televisores.get("disponible"))
# print(televisores.get("precio"))
# print(televisores.get("resolucion"))

# # agregar informacion

# televisores["disponible"] = True
# print(televisores)

# #modificar informacion

# televisores["precio"] = 6000000
# print(televisores)

# # eliminar informacion

# del televisores["disponible"]
# print(televisores)

# consultar conjuntos de datos

# print(televisores.keys()) 
# print(televisores.values())
# print(televisores.items())

# coleccion de registros
electrodomesticos_cocina = [
    {
    "producto": "nevera",
    "marca": "LG",
    "litros": 220,
    "color": "plateado",
    "disponible": True
    },
    {
    "producto": "sanduchera",
    "marca": "hoster",
    "color": "negra",
    "disponible": True
    }
]

print(electrodomesticos_cocina[0]["marca"])
print(electrodomesticos_cocina[1]["marca"])

# ejercicio
evento_1 = {"codigo": "UTCCV-01", "tipo": "AUXILIO VIAL", "unidad": "CARRO TALLER"}
evento_2 = {"codigo": "UTCCV-02", "tipo": "ATENCION DERRAME", "unidad": "CONTRAINCEDIOS"}

reporte = [evento_1, evento_2]

print("Primer evento:", reporte[0]["tipo"])
print("Unidad que atendió segundo evento:", reporte[1]["unidad"])

reporte[1]["tipo"] = "INCENDIO FORESTAL"
print("Cambio tipo de evento 2:", reporte[1]["tipo"])

# conjuntos

unidades = {"carro taller", "ambulancia", "grua"}
print(unidades)

# agregar un canal
unidades.add("contraincendios")
print(unidades)

# comprobar si un elemento esta en el conjunto
print("moto" in unidades)
print("ambulancia" in unidades)

# unir conjuntos
campania_a = {"instagram", "facebook", "tiktok"}
campania_b = {"youtube","tiktok","pinterest"}

campania_c = campania_a | campania_b # union
print(campania_c)

campania_d = campania_a & campania_b # interseccion
print(campania_d)

campania_e = campania_a - campania_b # diferencia
print(campania_e)
