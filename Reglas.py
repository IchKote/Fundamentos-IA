class Reglas:
    def __init__(self):
        self.reglas = []

    def espacioVacio(tablero, fila, columna):
        if tablero.grilla[fila][columna] == "-":
            return True
        else:
            return False
        
    def espacioOcupado(tablero, fila, columna):
        if tablero.grilla[fila][columna] == "B" or tablero.grilla[fila][columna] == "N":
            return True
        else:
            return False

    def jugadaValida(tablero, fila, columna, color):
        fichas = Reglas.obtenerFichasA_Voltear(tablero, fila, columna, color)
        return len(fichas) > 0

    @staticmethod
    def obtenerFichasA_Voltear(tablero, fila, columna, color):
        fichas_totales = []
        if tablero.grilla[fila][columna] not in ["-", color]:
            return fichas_totales # Retorna lista vacía si no es espacio vacío
            
        rival = "N" if color == "B" else "B"
        direcciones = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        
        for df, dc in direcciones:
            f_actual, c_actual = fila + df, columna + dc
            fichas_temp = []
            
            # Avanzamos viendo al rival
            while 0 <= f_actual < tablero.dimension and 0 <= c_actual < tablero.dimension and tablero.grilla[f_actual][c_actual] == rival:
                fichas_temp.append((f_actual, c_actual))
                f_actual += df
                c_actual += dc
                
            # Si atrapamos fichas y cerramos con nuestro color
            if len(fichas_temp) > 0 and 0 <= f_actual < tablero.dimension and 0 <= c_actual < tablero.dimension:
                if tablero.grilla[f_actual][c_actual] == color:
                    # Agregamos estas fichas a la lista total
                    fichas_totales.extend(fichas_temp)
                    
        return fichas_totales

    def voltearFichas(tablero, fila, columna, color):
        fichas_a_voltear = Reglas.obtenerFichasA_Voltear(tablero, fila, columna, color)
        for f, c in fichas_a_voltear: 
            tablero.grilla[f][c] = color
