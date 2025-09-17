"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    with open("./files/input/data.csv", newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        total = {}
        for fila in lector:
            fila[0] = fila[0].split()
            if fila[0][0] not in total.keys():
                total[fila[0][0]] = set()
                total[fila[0][0]].add(int(fila[0][1]))
            else:
                total[fila[0][0]].add(int(fila[0][1]))
        
        resultado = []

        for key in sorted(total):
            resultado.append((key, max(total[key]), min(total[key])))

        return resultado