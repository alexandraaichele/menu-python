# esto permite escribir los resultados en una tabla
from tabulate import tabulate

# la definición siguiente es para mostrar el rango de los años que serán las
# introducidas por la persona y se buscaran igualdades con la lista de vinos


def search_by_year(annio):
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    information = []
    # el for es para meter y analizar los resultados en la lista y ver si hay similitudes
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')

        # acá observamos como se le pide al ciclo que utilice los valores de la categoria 2 de la lista
        if (words[2] != 'N.V.' and words[2] != "" and words[2] != "year"):
            year = words[2]
            # aqui es para que solo funcionen digitos ingresados en la parte del año
            if year.isdigit() and annio.isdigit():
                if(int(annio) == int(year)):
                    information.append(words)
    # acá es para ver si se encuentra o no los datos puestos
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        # en esa parte se tabularan 10 de los datos iguales encontrados en la lista
        print(tabulate(information[:10], headers=[
            "winery", "wine", "year", "rating", "num_reviews", "country", "region", "price", "type", "body", "acidity"]))
