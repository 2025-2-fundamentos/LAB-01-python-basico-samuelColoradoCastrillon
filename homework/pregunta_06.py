"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    
    with open("./files/input/data.csv", newline="", encoding="utf-8") as f:
        total = {}
        for raw_line in f:
            # Eliminamos salto de línea y separamos manualmente por tab
            parts = raw_line.strip().split("\t")
            if len(parts) != 5:
                raise ValueError(f"Línea mal formateada: {raw_line}")
            
            lista = [x.split(":") for x in parts[4].split(",")]

            print(lista[0])
            for i in lista:
                if i[0] not in total.keys():
                    total[i[0]] = set()
                    total[i[0]].add(int(i[1]))
                else:
                    total[i[0]].add(int(i[1]))
        resultado = []

        for key in sorted(total):
            resultado.append((key, min(total[key]), max(total[key])))

        return resultado