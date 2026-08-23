class Reglas:
    """Clase estática con la lógica y reglas del juego Othello."""

    @staticmethod
    def espacio_vacio(tablero, fila, columna):
        """Verifica si un espacio está vacío o tiene marca de movimiento."""
        return tablero.grilla[fila][columna] in ["-", "X"]

    @staticmethod
    def espacio_ocupado(tablero, fila, columna):
        """Verifica si un espacio está ocupado por una ficha (B o N)."""
        return tablero.grilla[fila][columna] in ["B", "N"]

    @staticmethod
    def jugada_valida(tablero, fila, columna, color):
        """Verifica si jugar en la coordenada captura fichas rivales."""
        fichas = Reglas.obtener_fichas_a_voltear(tablero, fila, columna, color)
        return len(fichas) > 0

    @staticmethod
    def obtener_fichas_a_voltear(tablero, fila, columna, color):
        """Calcula las coordenadas de las fichas que serían capturadas."""
        fichas_totales = []
        if tablero.grilla[fila][columna] not in ["-", "X", color]:
            return fichas_totales

        rival = "N" if color == "B" else "B"
        direcciones = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        for df, dc in direcciones:
            f_actual, c_actual = fila + df, columna + dc
            fichas_temp = []

            # Avanzamos buscando fichas del rival en la dirección actual.
            while (0 <= f_actual < tablero.dimension and
                   0 <= c_actual < tablero.dimension and
                   tablero.grilla[f_actual][c_actual] == rival):
                fichas_temp.append((f_actual, c_actual))
                f_actual += df
                c_actual += dc

            # Si atrapamos fichas rivales y cerramos con nuestro color.
            if (len(fichas_temp) > 0 and
                    0 <= f_actual < tablero.dimension and
                    0 <= c_actual < tablero.dimension):
                if tablero.grilla[f_actual][c_actual] == color:
                    fichas_totales.extend(fichas_temp)

        return fichas_totales

    @staticmethod
    def voltear_fichas(tablero, fila, columna, color):
        """Convierte las fichas capturadas al color del jugador actual."""
        fichas_a_voltear = Reglas.obtener_fichas_a_voltear(
            tablero, fila, columna, color
        )
        for f, c in fichas_a_voltear:
            tablero.grilla[f][c] = color

    @staticmethod
    def obtener_movimientos_validos(tablero, color):
        """Retorna coordenadas donde el jugador tiene un movimiento legal."""
        movimientos = []
        for f in range(tablero.dimension):
            for c in range(tablero.dimension):
                if tablero.grilla[f][c] in ["-", "X"]:
                    if Reglas.jugada_valida(tablero, f, c, color):
                        movimientos.append((f, c))
        return movimientos
