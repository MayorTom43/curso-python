# ========================================
# TRES EN RAYA CON MARDADOR (DICCIONARIOS)
# ========================================

# diccionario para almacer las estadisticas de las partidas
marcador = {"X": 0, "O": 0, "Empates": 0}

jugando_partidas = True

print("¡Bienvenido al Tres en raya con marcador global!")

while jugando_partidas:
    # tablero inicial
    tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    turno_actual = "X"
    ronda_activa = True

    def imprimir_tablero(t):
        print("\n     1   2   3")
        print("   -------------")
        for i in range(3):
            print(f"F{i+1} | ", end="")
            for j in range(3):
                print(t[i][j] + " | ", end="")
            print("\n   -------------")

    def verificar_ganador(t, jugador):
        # revidar filas, columnas y diagonales
        for i in range(3):
            if t[i][0] == jugador and t[i][1] == jugador and t[i][2] == jugador:
                return True 
            if t[0][i] == jugador and t[1][i] == jugador and t[2][i] == jugador:
                return True
        if t[0][0] == jugador and t[1][1] == jugador and t[2][2] == jugador:
            return True  
        if t[0][2] == jugador and t[1][1] == jugador and t[2][0] == jugador:
            return True 
        return False

    def tablero_lleno(t):
        for fila in t:
            if "-" in fila:
                return False
        return True

    # bucle de la ronda actual
    while ronda_activa:
        imprimir_tablero(tablero)
        print(f"\n--- TURNO DEL JUGADOR: {turno_actual} ---")

        try:
            f = int(input("Elige la fila (1-3): ")) - 1
            c = int(input("Elige la columna (1-3): ")) - 1

            if not (0 <= f < 3 and 0 <= c < 3):
                print("❌ Error: Las coordenadas deben estar entre 1 y 3.")
                continue
            if tablero[f][c] != "-":
                print("❌ Error: ¡Casilla ocupada!")
                continue

            tablero[f][c] = turno_actual

            if verificar_ganador(tablero, turno_actual):
                imprimir_tablero(tablero)
                print(f"\n🎉 ¡El jugador {turno_actual} gana esta ronda!")
                # usamos el diccionario para actualizar puntaje
                marcador[turno_actual] += 1
                ronda_activa = False

            elif tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print("\n🤝 ¡Empate en esta ronda!")
                marcador[turno_actual] += 1
                ronda_activa = False

            else:
                turno_actual = "O" if turno_actual == "X" else "X"

        except ValueError:
            print("❌ Por favor, introduce números válidos.") 

# ======================================
# MOSTRAR MARCADOR USANDO EL DICCIONARIO
# ======================================
    print("\n==============================") 
    print("      MARCADOR GLOBAL         ")
    print("==============================")   
    for clave, valor in marcador.items():
        print(f" {clave}: {valor} victorias/empates")
    print("==============================") 

# JUGAR OTRA RONDA?
    otra = input("\n¿Quieres jugar otra ronda? S/N: ").lower()
    if otra != "s":
        print("\n¡Gracias por jugar! Marcador final guardado.")
        break      