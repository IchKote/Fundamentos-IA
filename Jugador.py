from Reglas import Reglas


class Jugador:
    """Representa a un jugador de la partida."""

    def __init__(self, color):
        self.color = color

    def poner_ficha(self, tablero, fila, columna):
        """Intenta colocar una ficha y voltea las capturadas."""
        if 0 < fila <= tablero.dimension and 0 < columna <= tablero.dimension:
            if Reglas.espacio_vacio(tablero, fila - 1, columna - 1):
                es_valida = Reglas.jugada_valida(
                    tablero, fila - 1, columna - 1, self.color
                )
                if not es_valida:
                    tablero.grilla[fila - 1][columna - 1] = "-"
                    print("Jugada inválida. No captura fichas del rival.")
                    return False
                else:
                    tablero.grilla[fila - 1][columna - 1] = self.color
                    Reglas.voltear_fichas(
                        tablero, fila - 1, columna - 1, self.color
                    )
                    return True
            elif Reglas.espacio_ocupado(tablero, fila - 1, columna - 1):
                print("La celda ya está ocupada.")
                return False
        else:
            print("Coordenadas fuera de rango.")
            return False
