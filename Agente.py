from math import inf
from Reglas import Reglas

class Agente:
    def alfabeta(self, tablero, turnoAgente, alfa, beta):
        if turnoAgente:
            mejorPuntaje = -inf
            for i in range(tablero.dimension):
                for j in range(tablero.dimension):
                    if Reglas.jugada_valida(tablero, i, j, "B"):
                        tablero[i][j] = "B"
                        puntaje = self.alfabeta(tablero, False, alfa, beta)
                        tablero[i][j] = "-"
                        mejorPuntaje = max(mejorPuntaje, puntaje)
                        alfa = max(alfa, mejorPuntaje)
                        if alfa >= beta:
                            break
        else:
            mejorPuntaje = inf
            for i in range(tablero.dimension):
                for j in range(tablero.dimension):
                    if Reglas.jugada_valida(tablero, i, j, "N"):
                        tablero[i][j] = "N"
                        puntaje = self.alfabeta(tablero, True, alfa, beta)
                        tablero[i][j] = "-"
                        mejorPuntaje = min(mejorPuntaje, puntaje)
                        beta = min(beta, mejorPuntaje)
                        if alfa >= beta:
                            break
        return mejorPuntaje

    def mejor_jugada(self, tablero):
        mejorPuntaje = -inf
        movimiento = None
        for i in range(tablero.dimension):
            for j in range(tablero.dimension):
                if Reglas.jugada_valida(tablero, i, j, "B"):
                    tablero[i][j] = "B"
                    puntaje = self.alfabeta(tablero, False, -inf, inf)
                    tablero[i][j] = "-"
                    if puntaje > mejorPuntaje:
                        mejorPuntaje = puntaje
                        movimiento = (i, j)
        return movimiento