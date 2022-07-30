# esto permite escribir los resultados en una tabla
from tabulate import tabulate

# la definición continua es para ingresar una marca de vinos y mostrar todos los tipos de esa marca


def search_by_winery(wineryInput):
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    information = []

# acá es para que se busque el resultado ingresado
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')
# en este if se realizara la busqueda pero con el requisito de que lo ingresado tenga al menos 4 o más letras
# para que la busqueda no tenga que ser demasiado especifica, ademas el otro if es para que la busqueda siempre
# sea en minusculas y no afecten las mayusculas en el resultado
        if (words[0] != 'winery'):
            winery = words[0]
            if len(wineryInput) > 3:
                if(wineryInput.lower() in winery.lower()):
                    information.append(words)
    # esto se activa cuando no esta el dato ingresado en la lista
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        # en esa parte se tabularan 10 de los datos iguales encontrados en la lista
        print(tabulate(information[:10], headers=[
            "winery", "wine", "year", "rating", "num_reviews", "country", "region", "price", "type", "body", "acidity"]))
