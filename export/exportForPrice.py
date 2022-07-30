# nuevamente esta definicion es para mostrar las categorias de la lista
def isfloat(txt):
    return txt.replace('.', '', 1).replace(',', '', 1).isdigit()

# la definición siguiente es para abrir el archivo donde sacaremos la información de los vinos

# se define la funcion, esta trabaja con dos parametros


def export_by_price_range(price1, price2):
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    # array donde se guardará la información
    information = []
# el for lo utlizamos para recorrer los elementos de la lista y ver cuales funcionan y cuales no
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')

# acá es donde nuevamente ordenamos a la definición que utilice la categoria 7 de la lista
        if (words[7] != 'N.V.' and words[7] != "" and words[7] != "price"):
            price = words[7]
            # el precio esta puesto "price.isdigit" para que se permitan solo te creo digitos
            if price.isdigit() and price1.isdigit() and price2.isdigit():
                if(int(price1) <= int(price) <= int(price2)):
                    information.append(words)

# acá es para mostrar cuando la información preguntada no se encuentra disponible
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        # en esta parte se dara el nombre del nuevo archivo creado con las exportaciones solicitadas
        filename = f"Wines_by_price_{price1}_to_{price2}.csv"
        file = open(filename, "w")
        file.write(content[0])
        # se recorreo el array donde se guardó la info
        for line in information:
            line = ",".join(line)
            # se escribe el archivo
            file.write(f"{line}\n")
        file.close()
        print(f"los datos solicitados fueron exportados al archivo {filename}")
