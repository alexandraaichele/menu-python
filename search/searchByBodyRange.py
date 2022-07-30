# esto permite escribir los resultados en una tabla
from tabulate import tabulate

# definimos la funcion, esta tiene dos parametros con los cuales trabajaremos


def search_by_body_range(body1, body2):
    # leemos el archivo
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    # asignamos una variable para guardar la información
    information = []

    # recorremos linea a linea
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')

        # para poder guardar los valores, debemos hacer que sea distinta a la cabecera y a los que vengan sin valor
        # o sean NA
        if (words[9] != "body" and words[9] != "NA"):
            year = words[9]
            # hacemos la validacion de los rangos
            if(body1 <= year <= body2):
                # le hacemos push al array
                information.append(words)

    # comprobamos si hay información en el array, si no hay es porque no se cumple el rango dado por el usuario
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        print(tabulate(information[:10], headers=[
            "winery", "wine", "year", "rating", "num_reviews", "country", "region", "price", "type", "body", "acidity"]))
