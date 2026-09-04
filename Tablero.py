import Jugador
from Reglas import Reglas
from Agente import Agente 


class Tablero:
    """Controla el flujo de la partida y el tablero de juego."""

    def __init__(self, valor="-"):
        self.dimension = self.ingresar_dimension()
        self.grilla = [
            [valor for _ in range(self.dimension)]
            for _ in range(self.dimension)
        ]

    def mostrar(self):
        """Imprime el tablero por consola con sus coordenadas."""
        print("\n  " + " ".join(str(i + 1) for i in range(self.dimension)))
        for i, fila in enumerate(self.grilla):
            print(i + 1, " ".join(str(celda) for celda in fila))

    def ingresar_dimension(self):
        """Solicita y valida la dimensión del tablero (par y >= 4)."""
        mensaje = "Ingrese la dimensión (números pares >= 4): "
        m = input(mensaje)
        while not m.isdigit() or int(m) < 4 or int(m) % 2 != 0:
            print("Error: Entrada inválida.")
            m = input(mensaje)
        return int(m)

    def iniciar_tablero(self):
        """Coloca las cuatro fichas iniciales en el centro del tablero."""
        medio = self.dimension // 2
        self.grilla[medio - 1][medio - 1] = "B"
        self.grilla[medio][medio] = "B"
        self.grilla[medio - 1][medio] = "N"
        self.grilla[medio][medio - 1] = "N"

    def crear_jugador(self, color):
        """Instancia y retorna un jugador del color especificado."""
        return Jugador.Jugador(color)

    def limpiar_x(self):
        """Elimina las 'X' que marcan los movimientos válidos."""
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.grilla[i][j] == "X":
                    self.grilla[i][j] = "-"

    def iniciar_partida(self, jugador1, jugador2):
        """Maneja el bucle de la partida, los turnos y el fin de juego."""
        turno = 0
        switch = True
        pasos = 0

        while switch:
            valido = True
            self.limpiar_x()

            if turno % 2 == 0:
                jug_actual = jugador1
                nombre_turno = "Blanco (B)"
            else:
                jug_actual = jugador2
                nombre_turno = "Negro (N)"

            movimientos = Reglas.obtener_movimientos_validos(
                self, jug_actual.color
            )

            if not movimientos:
                print(
                    f"\nEl jugador {nombre_turno} no tiene "
                    "movimientos. Pasa."
                )
                pasos += 1
                turno += 1
                if pasos >= 2:
                    print("\nDos pases seguidos. Fin del juego.")
                    self.finalizar_partida()
                    break
                continue

            pasos = 0

            for f, c in movimientos:
                self.grilla[f][c] = "X"

            self.mostrar()

            while valido:
                print(f"\nTurno del jugador {nombre_turno}.")

                if isinstance(jug_actual, Agente):
                    print("La CPU esta calculando su jugada...")
                    movimiento = jug_actual.seleccionar_mejor_movimiento(self)
                    if movimiento:
                        f, c = movimiento
                        jug_actual.poner_ficha(self, f + 1, c + 1)
                    valido = False

                else:

                    entrada_fila = input("Ingrese la fila: ")
                    entrada_columna = input("Ingrese la columna: ")

                    if (not entrada_fila.isdigit() or
                            not entrada_columna.isdigit()):
                        print("Por favor, ingrese números válidos.")
                        continue

                    fila = int(entrada_fila)
                    columna = int(entrada_columna)

                    if not jug_actual.poner_ficha(self, fila, columna):
                        self.mostrar()
                        valido = True
                    else:
                        valido = False

            self.limpiar_x()
            turno += 1

            tablero_lleno = all("-" not in fila for fila in self.grilla)

            if tablero_lleno:
                print("\nEl tablero está lleno. Fin del juego.")
                self.finalizar_partida()
                break

    def finalizar_partida(self):
        """Realiza el conteo final de fichas y declara al ganador."""
        self.limpiar_x()
        self.mostrar()

        f_blancas = sum(fila.count("B") for fila in self.grilla)
        f_negras = sum(fila.count("N") for fila in self.grilla)

        print("\n--- FIN DE LA PARTIDA ---")
        print(f"Fichas Blancas (B): {f_blancas}")
        print(f"Fichas Negras (N): {f_negras}")

        if f_blancas > f_negras:
            print("¡Gana el jugador de fichas blancas (B)!")
        elif f_negras > f_blancas:
            print("¡Gana el jugador de fichas negras (N)!")
        else:
            print("¡Es un empate!")

def menu():
    """Menu principal"""
    print("================================")
    print("          MENU OTHELLO          ")
    print("================================")
    print("1. Jugador vs Jugador")
    print("2. Jugador vs CPU")
    print("================================")

    while True:
        opcion = input("Seleccione una opcion:")
        if opcion in ["1","2"]:
            return opcion
        print ("Porfavor seleccione una opción válida(1-2)")  
    

    
if __name__ == "__main__":
    opcion = menu()
    
    tablero_juego = Tablero()
    tablero_juego.iniciar_tablero()

    jugador_b = tablero_juego.crear_jugador("B")

    if opcion == "1":
        jugador_n = tablero_juego.crear_jugador("N")
    else:
        jugador_n = Agente("N")
   
    tablero_juego.iniciar_partida(jugador_b, jugador_n)   
