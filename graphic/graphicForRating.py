import matplotlib.pyplot as plt
import numpy as np


def graphic_for_rating():
    # leemos el archivo
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    # array donde guardaremos los valores
    new_rating = []
    # se va a recorrer el contenido
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')
        # eliminamos la cabecera de la lista
        if (words[3] != "rating"):
            new_rating.append(words[3])

    # ordenamos el array de forma ascendente del array
    ratings = sorted(new_rating)

    # asignamos que irá en el eje "Y" y que cosa irá en el eje "X"
    ypoints = np.array(ratings)
    xpoints = np.array(range(len(ratings)))

    # llamamos a la funcion de matplot y vemos que grafico deseamos
    plt.plot(xpoints, ypoints)
    # mostramos el gráfico
    plt.show()
