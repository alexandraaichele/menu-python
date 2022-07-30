# esto permite escribir los resultados en una tabla
from tabulate import tabulate

# definimos la función que recibe dos parametros


def search_by_rating_range(rating1, rating2):
    # leemos el archivo
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    # array donde guardaremos la información
    information = []

    # recorremos linea a linea
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')

        # eliminamos la cabecera de la lista
        if (words[3] != "rating"):
            rating = words[3]
            # hacemos la comparacion si es que rating 1 es menor y rating 2 es mayor
            if(rating1 <= rating <= rating2):
                # si cumple la validacion entonces lo guardaremos
                information.append(words)

    # comprobamos cual es el largo del array, si es mayor a cero entonces si existe ese rango en nuestros datos
    # por lo que podemos imprimir la tabla.
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        print(tabulate(information[:10], headers=[
            "winery", "wine", "year", "rating", "num_reviews", "country", "region", "price", "type", "body", "acidity"]))
