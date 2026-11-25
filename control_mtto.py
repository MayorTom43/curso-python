# PREPARAR LOS DATOS

flota = [
    {"codigo":"v-101", "km":320},
    {"codigo":"v-102", "km":780},
    {"codigo":"v-103", "km":1250},
    {"codigo":"v-104", "km":1680},
    {"codigo":"v-105", "km":450},
    {"codigo":"v-106", "km":920},
    {"codigo":"v-107", "km":1420},
    {"codigo":"v-108", "km":1850},
    {"codigo":"v-109", "km":610},
    {"codigo":"v-110", "km":1100},
    {"codigo":"v-111", "km":250},
    {"codigo":"v-112", "km":1550}
]

# CONTADORES
uso_reciente = 0
seguimiento = 0
prog_revision = 0
prioridad_alta = 0
fuera_rango = 0

# ACUMULADOR
km_total = 0

print("=" * 60)
print("REPORTE INDIVIDUAL DE MANTENIMIENTO PREVENTIVO")
print("=" * 60)

# RECORRER LOS REGISTROS, CLASIFICAR, CONTAR Y ACUMULAR
for vehiculos in flota:
    cod = vehiculos["codigo"]
    km = vehiculos["km"]
    
    # CALCULAR KM TOTAL
    km_total += km
    
    # CLASIFICAR
    if 0 <= km <= 499:
        categoria = "USO RECIENTE"
        uso_reciente +=1
    elif 500 <= km <= 999:
        categoria = "SEGUIMIENTO"
        seguimiento +=1
    elif 1000 <= km <= 1499:
        categoria = "PROGRAMAR REVISIÓN"
        prog_revision += 1
    elif 1500 <= km <= 1999:
        categoria = "PRIORIDAD ALTA"
        prioridad_alta +=1        
    else:
        categoria = "FUERA DE RANGO (2000+ KM)"
        fuera_rango +=1
        
# GUARDAR CATEGORIA
vehiculos["categoria"] = categoria
    
# MOSTRAR CLASIFICACION
print(f"Vehiculo: ", cod, "| Kilometraje: ", km, "km | Categoria: ", categoria)
    
# CALCULAR PROMEDIO CON len()
cant_vehiculos = len(flota)
km_promedio = km_total / cant_vehiculos if cant_vehiculos > 0 else 0
    
# RESUMEN FRECUENCIA E INDICADORES
print("\n" + "=" * 60)
print("RESUMEN DE FRECUENCIA E INDICADORES DE LA FLOTA")
print("=" * 60)
print(f"0 a 499 km (USO RECIENTE)          :{uso_reciente} vehiculos")
print(f"500 a 999 km (SEGUIMIENTO)         :{seguimiento} vehiculos")
print(f"1000 a 1499 km (PROGRARMAR REV.)   :{prog_revision} vehiculos")
print(f"1500 a 1999 km (PRIORIDAD ALTA)    :{prioridad_alta} vehiculos")
if fuera_rango > 0:
    print(f"2000 km o más (FUERA DE RANGO) :{fuera_rango} vehiculos")
print("-" * 60)
print(f"Total de vehiculos evaluados       :{cant_vehiculos}")
print(f"Kilometraje acumulado              :{km_total:,} km".replace(",","."))
print(f"Kilometraje promedio x Vehiculo    :{km_promedio:.2f} km")
    
# CONSULTAR CON WHILE
print("\n" + "=" * 60)
print("CONSULTA x CODIGO DE VEHICULO")
print("=" * 60)
    
continuar = "s"
    
while continuar.lower() == "s":
    cod_buscar = input("\nIngrese el codigo del vehiculo: ").strip().lower()
    encontrado = False
        
    for vehiculos in flota:
        if vehiculos["codigo"].lower() == cod_buscar:
            print(
                f"Resultado -> codigo: {vehiculos['codigo']} | "
                f"Kilometraje: {vehiculos['km']} | "
                f"Categoria: {vehiculos['categoria']}"
            )
            encontrado = True
            break
    if not encontrado:
        print(f"NO SE ENCUENTRA NINGUN VEHICULO {cod_buscar}")
        
    continuar = input("Desea realizar otra consulta? (s/n):").strip().lower()
        
print("\nConsulta finalizada")