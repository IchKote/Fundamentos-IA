from math import inf
from Reglas import Reglas

class Agente:
    def alfabeta(self, tablero, turnoAgente, alfa, beta):
        """Calcula el valor minimax usando poda alfa-beta."""
        if turnoAgente:
            mejorPuntaje = -inf
            for i in range(tablero.dimension):
                for j in range(tablero.dimension):
                    if (tablero.grilla[i][j] in ["-", "X"] and
                            Reglas.jugada_valida(tablero, i, j, "B")):
                        tablero.grilla[i][j] = "B"
                        Reglas.voltear_fichas(tablero, i, j, "B")
                        puntaje = self.alfabeta(tablero, False, alfa, beta)
                        tablero.grilla[i][j] = "-"
                        if puntaje > mejorPuntaje:
                            mejorPuntaje = puntaje
                        alfa = max(alfa, mejorPuntaje)
                        if beta <= alfa:
                            break
        else:
            mejorPuntaje = inf
            for i in range(tablero.dimension):
                for j in range(tablero.dimension):
                    if (tablero.grilla[i][j] in ["-", "X"] and
                            Reglas.jugada_valida(tablero, i, j, "N")):
                        tablero.grilla[i][j] = "N"
                        Reglas.voltear_fichas(tablero, i, j, "N")
                        puntaje = self.alfabeta(tablero, True, alfa, beta)
                        tablero.grilla[i][j] = "-"
                        if puntaje < mejorPuntaje:
                            mejorPuntaje = puntaje
                        beta = min(beta, mejorPuntaje)
                        if beta <= alfa:
                            break
        return mejorPuntaje

    def mejor_jugada(self, tablero):
        """Retorna la mejor jugada para las fichas blancas."""
        mejor_puntaje = -inf
        movimiento = None

        for i in range(tablero.dimension):
            for j in range(tablero.dimension):
                if (tablero.grilla[i][j] in ["-", "X"] and
                        Reglas.jugada_valida(tablero, i, j, "B")):
                    tablero.grilla[i][j] = "B"
                    Reglas.voltear_fichas(tablero, i, j, "B")
                    puntaje = self.alfabeta(tablero, False, -inf, inf)
                    tablero.grilla[i][j] = "-"

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        movimiento = (i, j)

        return movimiento
