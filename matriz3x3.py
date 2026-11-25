#declarar matriz
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

#acceder a elementos de la matriz

primer_elemento = matriz[0][0] #fila 0, columna 0
elemento_central = matriz[1][1]

print("El primer elemento es:",primer_elemento,"\nElemento central es:",elemento_central)

#modificar un valor de la matriz
print("\n--- Modificando un valor de la matriz ---")
matriz[1][1] = 45
print("Fila 1 modificada:", matriz[1])

#recorrer la matriz
print("\n--- Imprimiendo la matriz ---")

for fila in matriz:
    for elemento in fila:
    # 'end=" " evita que se imprima un salto de linea y pone un espacio en blanco'
        print(elemento, end="\t") #tabulacion
    print()
