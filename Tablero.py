import Jugador

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

    def iniciarPartida(self, jugador1, jugador2):
        turno = 0
        switch = True
        while switch:
            valido = True
            if turno % 2 == 0:
                while valido:
                    print(f"Turno del jugador blanco.")
                    fila = int(input("Ingrese la fila: "))
                    columna = int(input("Ingrese la columna: "))
                    if jugador1.ponerFicha(self, fila, columna) == False:
                        valido = True
                    else:
                        valido = False
            else:
                while valido:
                    print(f"Turno del jugador negro.")
                    fila = int(input("Ingrese la fila: "))
                    columna = int(input("Ingrese la columna: "))
                    if jugador2.ponerFicha(self, fila, columna) == False:
                        valido = True
                    else:
                        valido = False
            self.mostrar()
            turno += 1


tablero = Tablero(valor="-")
tablero.iniciarTablero()
tablero.mostrar()

jugador1 = tablero.crearJugador("B")
jugador2 = tablero.crearJugador("N")

tablero.iniciarPartida(jugador1, jugador2)