# esto permite escribir los resultados en una tabla
from tabulate import tabulate

# definimos la funcion la cual tiene dos parametros


def search_by_price_range(price1, price2):
    # leemos el archivo
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    # array donde se guardará la información
    information = []

    # recorremos el contenido, linea por linea
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')

        # eliminamos la cabecera de la lista para trabajar solo con los valores
        if (words[7] != "price"):
            price = words[7]
            # hacemos la validacion, price1 debe ser menor y price2 debe ser mayor
            if(price1 <= price <= price2):
                # si ambas validaciones son verdaderas entonces se guardará en un array
                information.append(words)

    # vemos si hay información en el array, si es así entonces se cumple el rango y se puede mostrar una tabla
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        print(tabulate(information[:10], headers=[
            "winery", "wine", "year", "rating", "num_reviews", "country", "region", "price", "type", "body", "acidity"]))
