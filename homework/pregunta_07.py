"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    with open("./files/input/data.csv", newline="", encoding="utf-8") as f:
        total = {}
        for raw_line in f:
            # Eliminamos salto de línea y separamos manualmente por tab
            parts = raw_line.strip().split("\t")
            if len(parts) != 5:
                raise ValueError(f"Línea mal formateada: {raw_line}")
            
            tipo = parts[0]
            numero = int(parts[1])

            print(tipo, numero)

            if numero not in total.keys():
                total[numero] = [tipo]
            else:
                total[numero].append(tipo)

        return sorted(total.items())