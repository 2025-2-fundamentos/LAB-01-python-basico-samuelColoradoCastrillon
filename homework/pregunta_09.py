"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    with open("./files/input/data.csv", newline="", encoding="utf-8") as f:
        total = {}
        for raw_line in f:
            # Eliminamos salto de línea y separamos manualmente por tab
            parts = raw_line.strip().split("\t")
            if len(parts) != 5:
                raise ValueError(f"Línea mal formateada: {raw_line}")
            
            lista = [x.split(":") for x in parts[4].split(",")]

            for i in lista:
                if i[0] not in total.keys():
                    total[i[0]] = 1
                else:
                    total[i[0]] += 1
        return total