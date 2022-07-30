# esta definición es para que se muestren las categorias de los vinos
def isfloat(txt):
    return txt.replace('.', '', 1).replace(',', '', 1).isdigit()

# Y aqui es donde se crea una función para que tenga donde exportarse los vinos dependiendo de si cumplen o no


def export_by_acidity_range(acidity1, acidity2):
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    information = []

# el for lo utlizamos para recorrer los elementos de la lista y ver cuales funcionan y cuales no
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')
# en esta parte es para dar la orden de la categoria en la que se tienen que basar los resultados
        if (words[10] != 'N.V.' and words[10] != "" and words[10] != "acidity"):
            acidity = words[10]
            if isfloat(acidity1) and isfloat(acidity) and isfloat(acidity2):
                if(float(acidity1) <= float(acidity) <= float(acidity2)):
                    information.append(words)

# aqui es para confirmar si hay datos o no hay datos en realción con lo puesto por la persona
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        # luego se crea el "filename" para avisar que los resultados puestos por las peronas han sido exportados al nombre
        # que es igual "filename"
        filename = f"Wines_by_acidity_{acidity1}_to_{acidity2}.csv"
        file = open(filename, "w")
        file.write(content[0])

        # se recorre el array
        for line in information:
            line = ",".join(line)
            # se escribe el archivo
            file.write(f"{line}\n")
        file.close()
        print(f"los datos solicitados fueron exportados al archivo {filename}")
