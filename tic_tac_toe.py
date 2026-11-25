# ====================================
#       JUEGO DE TRES EN RAYA
# ====================================

# crear el tablero incial de 3x3 lleno de guiones (espacios vacios)
tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def imprimir_tablero(t):
    print("\n     1   2   3")
    print("   -------------")
    for i in range(3):
        # imprime la fila con su numero al lado
        print(f"F{i+1} | ", end="")
        for j in range(3):
            print(t[i][j] + " | ", end="")
        print("\n   -------------")

def verificar_ganador(t, jugador):
    # revisar filas
    for i in range(3):
        if t[i][0] == jugador and  t[i][1] == jugador and t[i][2] == jugador:
            return True

    # revisar columnas
    for j in range(3):
        if t[0][j] == jugador and t[1][j] == jugador and t[2][j]:
            return True

    # revisar diagonal principal (arriba-izq a abajo-der)
    if t[0][0] == jugador and t[1][1] == jugador and t[2][2] == jugador:
        return True

    # revisar diagonal secundaria (de arriba-der a abajo-izq)
    if t[0][2] == jugador and t[1][1] == jugador and t[2][0] == jugador:
        return True

    return False

def tablero_lleno(t):
    # comprueba si quedan espacios vacios ('-') en el tablero
    for fila in t:
        if "-" in fila:
            return False
    return True   
 
# ====================================
#     BUCLE PRINCIPAL DEL JUEGO
# ====================================
turno_actual = "X" # empieza el jugador X
juego_activo = True

print("¡Bienvenido a TIC TAC TOE en Python!")

while juego_activo:
    imprimir_tablero(tablero)
    print(f"\nEs el turno del jugador: {turno_actual}")

    try:
        f = int(input("Elige la fila (1-3): ")) -1
        c = int(input("Elige la columna (1-3) "))-1

        # validar que las coordenadas esen dentro del rango permitido
        if not (0<= f < 3 and 0 <= c < 3):
            print("❌ Error: Las coordenadas deben estar entre 1 y 3.")
            continue

        # validar que la casilla este vacia
        if tablero[f][c] != "-":
            print("❌ Error: ¡Esa casilla ya está ocupada! Elige otra.")
            continue

        # colocar la ficha del jugador en la matriz
        tablero[f][c] = turno_actual

        # comprobar si el jugador actual ganó
        if verificar_ganador(tablero, turno_actual):
            imprimir_tablero(tablero)
            print(f"\n🎉 ¡Felicidades! El jugador {turno_actual} ha ganado la partida.")
            juego_activo = False
        elif tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("\n🤝 ¡Empate! El tablero está lleno.")
            juego_activo = False
        else:
            # cambiar de turno: si era 'X' pasa a 'O' y viceversa
            turno_actual = "O" if turno_actual == "X" else "X"
    except ValueError:
        print("❌ Entrada no válida. Por favor, introduce números enteros.")

