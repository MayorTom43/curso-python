# ======================================
#  REPRESENTACION DE UN SUDOKU EN PYTHON
# ======================================

tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# ==========================================
# FUNCIÓN PARA IMPRIMIR EL TABLERO BONITO
# ==========================================
def imprimir_sudoku(m):
    # Recorremos cada fila usando su índice 'i'
    for i in range(len(m)):
        # Cada 3 filas imprimimos una línea horizontal divisoria
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        # Recorremos cada columna usando su índice 'j'
        for j in range(len(m[i])):
            # Cada 3 columnas imprimimos una barra vertical divisoria
            if j % 3 == 0 and j != 0:
                print("|", end="")

            # Si el valor es 0, mostramos un punto '.' para que sea más legible
            if m[i][j] == 0:
                print(".  ", end="")
            else:
                print(str(m[i][j]) + " ", end="")

        # Salto de línea al terminar cada fila
        print()


# Ejecutamos la función
print("--- TABLERO DE SUDOKU INICIAL ---")
imprimir_sudoku(tablero)

# creamos una matriz de apoyo (Booleano) para identificar que celdas son fijas
# 'True' significa que la celda vino dada al inicio y no se puede modificar
fijas = [[celda != 0 for celda in fila] for fila in tablero]

# ================================================
# FUNCIÓN PARA IMPRIMIR EL TABLERO CON COORDENADAS
# ================================================

def imprimir_sudoku(m):
    print("\n     COLUMNAS")
    print("     1 2 3    4 5 6    7 8 9")
    print("  ---------------------------------")
    for i in range(len(m)):
        if i % 3 == 0 and i != 0:
            print("  ---------------------------------")

        # muestra el numero de la fila al inicio
        print(f"F{i+1} | ", end="")

        for j in range(len(m[i])):
            if j % 3 == 0 and j != 0:
                print("|  ", end="")
            
            if m[i][j] == 0:
                print(". ", end="")
            else:
                print(str(m[i][j]) + " ", end="")
        print("|")
    print("  ---------------------------------")

# ================================================
# FUNCIÓN DE VALIDACIÓN DE REGLAS
# ================================================
def es_valido(m, fila, col, num):

    # 1. validar si el numero ya esta en la fila
    if num in m[fila]:
        return False

    # 2. validar si el numero ya esta en la columna
    for i in range(9):
        if m[i][col] == num:
            return False

    # 3. validar si el numero ya está en el bloque de 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if m[inicio_fila + i][inicio_col + j] == num:
                return False

    return True # si pasa todas las pruebas, el movimiento es valido        

# ================================================
# BUCLE PRINCIPAL DEL JUEGO
# ================================================

print("¡Bienvenido al SUDOKU!")
print("Instrucciones: introduce la fila, columna y numero que desea poner.")
print("Escribe '0' en la fina en cualquier momento para salir del juego. \n")

while True:
    imprimir_sudoku(tablero)

    # usamos 'try-except' para evitar que el programa falle si el usuario escribe letras en vez de numeros
    try:
        print("\n--- NUEVO MOVIMIENTO ---")
        f = int(input("elige la fila (1-9) [0 para salir]: "))

        if f == 0:
            print("¡Gracias por jugar! Hasta pronto.")
            break

        c = int(input("elige la columna (1-9): "))
        n = int(input("elige el numero (1-9): "))

        # restamos 1 porque las listas en Python empiezan en el indice 0
        fila_idx = f - 1
        col_idx = c -1 

        # validar rangos correctos
        if not (0 <= fila_idx < 9 and 0 <= col_idx < 9 and 1 <= n <= 9):
            print(
                "❌ Error: Las coordenadas y el número deben estar estrictamente"
          " entre 1 y 9."
            )
            continue

        # verificar si el usuario intenta modificar una casilla original
        if fijas[fila_idx][col_idx]:
            print(
                "❌ Error: ¡Esa casilla es fija del tablero inicial y no se puede"
          " cambiar!"
            )
            continue

        # validar si el numero cumple las reglas del sudoku
        if es_valido(tablero, fila_idx, col_idx, n):
            tablero[fila_idx][col_idx] = n
            print("✅ ¡Movimiento colocado con éxito!")
        else:
            print("❌ Movimiento inválido: El número choca con otro igual en la misma"
          " fila, columna o bloque 3x3.")

    except ValueError:
        print("❌ Entrada no válida. Por favor, introduce únicamente números enteros"
        " del 1 al 9.")

