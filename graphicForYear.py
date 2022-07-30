import matplotlib.pyplot as plt
import numpy as np


def graphic_for_year():
    # leemos el archivo
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    # array donde guardaremos los valores
    new_year = []
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')

        # mientras el año que recorremos sea distinto a las validaciones entonces cumple y lo guardaremos
        if (words[2] != 'N.V.' and words[2] != "" and words[2] != "year"):
            new_year.append(words[2])

    # ordenaremos el array de forma ascendente
    years = sorted(new_year)

    # asigamos que cosas tomará el valor en el eje "Y" y que cosas en el eje "X"
    ypoints = np.array(years)
    xpoints = np.array(range(len(years)))
    # llamamos a las funciones de matplot
    plt.plot(xpoints, ypoints)
    # mostramos el gráfico
    plt.show()
