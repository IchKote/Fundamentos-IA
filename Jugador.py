from Reglas import Reglas 

#Pablo
class Jugadores:
    def __init__(self, color):
        self.color = color

    def ponerFicha(self, tablero, fila, columna):
        if 0 < fila <= tablero.dimension and 0 < columna <= tablero.dimension:
            if Reglas.espacioVacio(tablero, fila-1, columna-1):
                if Reglas.jugadaValida(tablero, fila-1, columna-1, self.color) == False:
                    tablero.grilla[fila-1][columna-1] = "-"
                    print("Jugada inválida.")
                    return False
                else:
                    tablero.grilla[fila-1][columna-1] = self.color
                    Reglas.voltearFichas(tablero, fila-1, columna-1, self.color)
                    return True
            elif Reglas.espacioOcupado(tablero, fila-1, columna-1) == True:
                print("La celda ya está ocupada.")
        else:
            print("Coordenadas fuera de rango.")
            return False