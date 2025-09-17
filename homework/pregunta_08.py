"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

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
                total[numero] = set()
                total[numero].add(tipo)
            else:
                total[numero].add(tipo)

        for key in total:
            total[key] = sorted(list(total[key]))

        return sorted(total.items())