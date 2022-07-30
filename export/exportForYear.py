# la definición será para mostrar el año de creación de cada vino
# definimos la función, la cual tiene dos parametros
def export_by_year_range(annio1, annio2):
    archive = open("wines.csv", "r")
    content = archive.readlines()
    archive.close()

    information = []
# el for será utilizado para recorrer los elementos iterables de una lista
    for line in content:
        line = line.replace('"', '').strip()
        words = line.split(',')

# acá se ordena a la función buscar los resultados ingresados en la segunda linea de la lista, donde se encuentra la categoría preguntada
        if (words[2] != 'N.V.' and words[2] != "" and words[2] != "year"):
            year = words[2]
            # aqui es agrega el ".isdigit" para que solo se permitan numeros ingresados
            if year.isdigit() and annio1.isdigit() and annio2.isdigit():
                # hacemos la validacion del rango
                if(int(annio1) <= int(year) <= int(annio2)):
                    # si se cumple la validacion, entonces se guarda en el array
                    information.append(words)

# aca es para mostrar cuando la información ingresada no existe en la lista
    if len(information) == 0:
        print('No tenemos esta información en nuestros datos.')
    else:
        # nuevamente el filename será el nmombre del archivo donde se irá dirigido lo exportado
        filename = f"Wines_by_year_{annio1}_to_{annio2}.csv"
        file = open(filename, "w")
        for line in information:
            line = ",".join(line)
            file.write(f"{line}\n")
        file.close()
        print(f"los datos solicitados fueron exportados al archivo {filename}")
