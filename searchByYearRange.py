# esto permite escribir los resultados en una tabla
from tabulate import tabulate

# definimos la funcion donde tiene dos parametros


def search_by_year_range(annio1, annio2):
    # leemos el archivo
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    # array donde se guardará la información
    information = []

    # recorremos el contenido linea a linea
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')

        # hacemos validaciones, eliminamos la cabecera de la lista, eliminamos los que vengan como "N.V"
        # y los que vengan vacios
        if (words[2] != 'N.V.' and words[2] != "" and words[2] != "year"):
            year = words[2]
            # comprobamos que todos sean digitos
            if year.isdigit() and annio1.isdigit() and annio2.isdigit():
                # los pasamos a int para poder comparar numeros
                if(int(annio1) <= int(year) <= int(annio2)):
                    # hacemos push al array
                    information.append(words)

    # si el largo del array es mayor a cero entonces esos rangos existen en nuestros registros
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        print(tabulate(information[:10], headers=[
            "winery", "wine", "year", "rating", "num_reviews", "country", "region", "price", "type", "body", "acidity"]))
