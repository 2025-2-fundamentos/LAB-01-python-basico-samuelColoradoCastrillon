"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    with open("./files/input/data.csv", newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        total = {}
        for fila in lector:
            fila[0] = fila[0].split()
            fecha = fila[0][2].split("-")
            if fecha[1] not in total.keys():
                total[fecha[1]] = 1
            else:
                total[fecha[1]] += 1
        return sorted(total.items())