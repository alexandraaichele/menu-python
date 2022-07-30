# esto permite escribir los resultados en una tabla
from tabulate import tabulate

# acá se observará que se buscan los vinos mediante su region de elaboración
# y se buscaran las semejanzas con la lista


def search_by_region(regionInput):
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    information = []
# se bucará el resultado ingresado
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')

# en esta parte muestra que se usará la fila número 6 que es donde se encuentran las regiones
        if (words[6] != 'region'):
            region = words[6]
            if len(regionInput) > 3:
                if(regionInput.lower() in region.lower()):
                    information.append(words)
    # esto se activa cuando no se encuentra el dato ingresado en la lista
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        # en esa parte se tabularan 10 de los datos iguales encontrados en la lista
        print(tabulate(information[:10], headers=[
            "winery", "wine", "year", "rating", "num_reviews", "country", "region", "price", "type", "body", "acidity"]))
