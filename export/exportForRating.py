# nuevamente esta definición es para que se muestren las categorias de los vinos
def isfloat(txt):
    return txt.replace('.', '', 1).replace(',', '', 1).isdigit()

# la definición permitira ver el rating de cada vino y será buscado en la lista enlazada

# definimos la funcion , la cual trabaja con dos parametros


def export_by_rating_range(rating1, rating2):
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()
    # array donde guardaremos los valores que cumplan con las condiciones
    information = []

# el for será utilizado para analizar los elementos de la lista
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')

# en esta parte su objetivo es buscar la categoría número 3 de la lista y buscar en todos esos datos y agrupar los que cumplen lo requerido
        if (words[3] != 'N.V.' and words[3] != "" and words[3] != "rating"):
            rating = words[3]
            # el float es agregado para permitir que la persona pueda ingresar "," y "." ya que las valoraciones suelen ser ej: 4.8 o 3.6, etc
            if isfloat(rating1) and isfloat(rating) and isfloat(rating2):
                if(float(rating1) <= float(rating) <= float(rating2)):
                    information.append(words)

# acá es para mostrar cuando la información preguntada no se encuentra disponible
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        # el filemane será el nombre del archivo en el que se exportará lo solicitado
        filename = f"Wines_by_rating_{rating1}_to_{rating2}.csv"
        file = open(filename, "w")
        file.write(content[0])
        for line in information:
            line = ",".join(line)
            file.write(f"{line}\n")
        file.close()
        print(f"los datos solicitados fueron exportados al archivo {filename}")
