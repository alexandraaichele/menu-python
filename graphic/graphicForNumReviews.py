import matplotlib.pyplot as plt
import numpy as np


def graphic_for_num_reviews():
    # leemos el archivo
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()
    # array donde se guardarán los valores que deseamos
    new_reviews = []
    # recorremos el contenido
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')
        # con esta validación eliminamos el cabecera de la lista, para poder trabajar solo con datos
        if (words[4] != "num_reviews"):
            # guardamos nuestros valores
            new_reviews.append(words[4])

    reviews = sorted(new_reviews)

    # con np, asignamos que irá en el eje "Y" y que cosas en el eje "X"
    ypoints = np.array(reviews)
    xpoints = np.array(range(len(reviews)))

    # llamamos a una función del matplot y le pasamos los
    # argumentos necesarios
    plt.plot(ypoints, xpoints)
    # mostramos el gráfico
    plt.show()
