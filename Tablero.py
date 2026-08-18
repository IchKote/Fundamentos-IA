import Jugador
from Reglas import Reglas

class Tablero:
    def __init__(self, valor):
        self.dimension = self.ingreseM()
        self.grilla = [[valor for _ in range(self.dimension)] for _ in range(self.dimension)]

    def mostrar(self):
        print("  " + " ".join(str(i+1) for i in range(self.dimension)))
        for i, fila in enumerate(self.grilla):
            print(i+1," ".join(str(celda) for celda in fila))
            
    def ingreseM(self):
        m = input("ingrese la dimension del tablero, solo se admiten numeros pares mayores o iguales a 4: ")
        while not m.isdigit() or int(m) < 4 or int(m) % 2 != 0:
            m = input("ingrese la dimension del tablero, solo se admiten numeros pares mayores o iguales a 4: ")
        return int(m)

    def iniciarTablero(self):
        medio = self.dimension // 2
        self.grilla[medio-1][medio-1] = "B"
        self.grilla[medio][medio] = "B"
        self.grilla[medio-1][medio] = "N"
        self.grilla[medio][medio-1] = "N"

    def crearJugador(self, color):
        return Jugador.Jugadores(color)

    def limpiarX(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.grilla[i][j] == "X":
                    self.grilla[i][j] = "-"

    def iniciarPartida(self, jugador1, jugador2):
        turno = 0
        switch = True
        while switch:
            valido = True
            
            # 1. Nos aseguramos de borrar cualquier "x" del turno anterior
            self.limpiarX()
            
            if turno % 2 == 0:
                jugador_actual = jugador1
                nombre_turno = "blanco"
            else:
                jugador_actual = jugador2
                nombre_turno = "negro"
                
            # 2. Obtenemos movimientos y ESCRIBIMOS la 'x' directo en la grilla
            movimientos_validos = Reglas.obtenerMovimientosValidos(self, jugador_actual.color)
            for f, c in movimientos_validos:
                self.grilla[f][c] = "X"
                
            self.mostrar()
            
            while valido:
                print(f"\nTurno del jugador {nombre_turno}.")
                try:
                    fila = int(input("Ingrese la fila: "))
                    columna = int(input("Ingrese la columna: "))
                    
                    if jugador_actual.ponerFicha(self, fila, columna) == False:
                        self.mostrar()
                        valido = True
                    else:
                        valido = False
                except ValueError:
                    print("Error: Ingrese números válidos.")
            # 3. Después de que el jugador puso su ficha, borramos las "x" que no usó
            self.limpiarX()
            turno += 1


tablero = Tablero(valor="-")
tablero.iniciarTablero()

jugador1 = tablero.crearJugador("B")
jugador2 = tablero.crearJugador("N")

tablero.iniciarPartida(jugador1, jugador2)
