"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    with open("./files/input/data.csv", newline="", encoding="utf-8") as f:
        total = {}
        for raw_line in f:
            # Eliminamos salto de línea y separamos manualmente por tab
            parts = raw_line.strip().split("\t")
            if len(parts) != 5:
                raise ValueError(f"Línea mal formateada: {raw_line}")
            
            tipo = parts[0]
            diccionario = {k: int(v) for k, v in (x.split(":") for x in parts[4].split(","))}
            
            if tipo not in total.keys():
                total[tipo] = 0

            for key in diccionario:
                total[tipo] += diccionario[key]
                
        return total