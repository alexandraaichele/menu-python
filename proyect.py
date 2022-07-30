from search import searchByYearRange
from search import searchByPriceRange
from search import searchByRatingRange
from search import searchByBodyRange
from search import searchByYear
from search import searchByWinery
from search import searchByRegion
from graphic import graphicForYear
from graphic import graphicForRating
from graphic import graphicForNumReviews
from export import exportForYear
from export import exportForPrice
from export import exportForRating
from export import exportForAcidity
import os


resp = 0
# inicio while para manejar el menu, esté siempre estará ejecutandose a menos que el usuario así lo desee
while resp != 5:
    os.system("cls")
    print("¡ BIVENIDO A LA BIBLIOTECA DE VINOS !")
    print("¿Qué información desea obtener sobre vinos?: ")
    print("1-. Datos por rangos de vinos")
    print("2-. Caracteristicas de vinos")
    print("3-. Visualizar datos sobre vinos")
    print("4-. Exportar datos")
    print("5-. Salir")
    resp = int(input("Ingrese el número de la opción: "))
    os.system("cls")
    # si el usuario elige opción 1 entonces le daremos más opciones que pueda escuchar
    if(resp == 1):
        validate = 0
        # se ejecutará el menu mientras el usuario desee
        while not validate:
            os.system("cls")
            print("¿Cual rango desea recibir?")
            print("1-. Rango por año")
            print("2-. Rango por precio")
            print("3-. Rango por calificación")
            print("4-. Rango por cuerpo del vino")
            opt2 = int(input("Ingrese el número de la opción que desee:"))
            os.system("cls")
            if(opt2 == 1):
                # le pedimos argumentos al usuario por lo que le gustaría buscar
                print("Ingrese los año por lo que desea buscar")
                annio1 = input("Año 1: ")
                annio2 = input("Año 2: ")
                # llamada a la función donde se buscar por rango de año
                searchByYearRange.search_by_year_range(annio1, annio2)
                # preguntamos si desea más información
                response = input("¿Desea más información?: (Si/NO) ")
                # hacemos las validaciones para ver si quiere seguir en este mini menu
                if(response.lower() == "si"):
                    validate = 0
                else:
                    validate = 1
            elif(opt2 == 2):
                # le pedimos argumentos al usuario por lo que le gustaría buscar
                print("Ingrese los precios por lo que desea buscar")
                price1 = input("Precio 1: ")
                price2 = input("Precio 2: ")
                # llamamos a la función pasandole los argumentos dados por el usuario
                searchByPriceRange.search_by_price_range(price1, price2)
                response = input("¿Desea más información?: (Si/NO) ")
                # hacemos la validacion para ver si desea seguir aquí o no
                if(response.lower() == "si"):
                    validate = 0
                else:
                    validate = 1
            elif(opt2 == 3):
                # le pedimos argumentos al usuario por lo que le gustaría buscar
                print("Ingrese el rating por el que desea buscar")
                rating1 = input("Rating 1: ")
                rating2 = input("Rating 2: ")
                # llamamos a la funcion a la cual le pasaremos los argumentos necesarios
                searchByRatingRange.search_by_rating_range(
                    rating1, rating2)
                response = input("¿Desea más información?: (Si/NO) ")
                # hacemos la validacion para ver si desea seguir aquí o no
                if(response.lower() == "si"):
                    validate = 0
                else:
                    validate = 1
            elif(opt2 == 4):
                # le pedimos argumentos al usuario por lo que le gustaría buscar
                print("Ingrese el cuerpo por el que desea buscar")
                body1 = input("Body 1: ")
                body2 = input("Body 2: ")
                # llamamos a la funciones para poder entregarle la informacion al usuario
                searchByBodyRange.search_by_body_range(body1, body2)
                response = input("¿Desea más información?: (Si/NO)")
                # hacemos la validacion para ver si desea seguir aquí o no
                if(response.lower() == "si"):
                    validate = 0
                else:
                    validate = 1
            else:
                # si la persona escribe una opcion invalida este sale del while
                print("Opción incorrecta!")
                validate = 1
    # en esta segunda opción se inicia cuando la persona apreta el 2 y presenta algunas de las caracteristicas de los vinos, las cuales les dan para escoger
    elif(resp == 2):
        validate2 = 0
        while not validate:
            os.system("cls")
            # le preguntamos al usuario que caracteristicas le gustario ver del data Set
            print("¿Cuales caracteristicas desea ver?")
            print("1-. Viñedo")
            print("2-. Año")
            print("3-. Región")
            opt3 = int(input("Ingrese el número de la opción que desee:"))
            os.system("cls")
            if(opt3 == 1):
                print("Ingrese el viñedo que desea buscar")
                winery = input("Viñedo : ")
                # llamaremos a al funcion a al cual le pasaremos un argumento
                searchByWinery.search_by_winery(winery)
                response = input("¿Desea más información?: (Si/NO) ")
                # validamos si la persona quiere seguir aqui o no
                if(response.lower() == "si"):
                    validate2 = 0
                else:
                    validate2 = 1
            elif(opt3 == 2):
                # le pedimos que ingrese el año por el que desea buscar
                print("Ingrese año que desea buscar")
                annio = input("Año : ")
                # llamaremos a al funcion a al cual le pasaremos un argumento
                searchByYear.search_by_year(annio)
                response = input("¿Desea más información?: (Si/NO) ")
                # validamos si la persona quiere seguir aqui o no
                if(response.lower() == "si"):
                    validate2 = 0
                else:
                    validate2 = 1
            elif(opt3 == 3):
                # le pedimos que ingrese la region por el que desea buscar
                print("Ingrese la región que desea buscar")
                region = input("Región: ")
                # llamaremos a al funcion a al cual le pasaremos un argumento
                searchByRegion.search_by_region(region)
                response = input("¿Desea más información?: (Si/NO) ")
                # validamos si la persona quiere seguir aqui o no
                if(response.lower() == "si"):
                    validate2 = 0
                else:
                    validate2 = 1
            else:
                # si la persona escribe una opcion invalida este sale del while
                print("Opción incorrecta!")
                validate = 1
    elif(resp == 3):
        validate3 = 0
        # el mini menu se ejecutará siempre que el usuario desee
        while not validate3:
            os.system("cls")
            print("¿Qué gráfico desea ver?: ")
            print("1-. Año")
            print("2-. Rating")
            print("3-. Número de reseñas")
            opt4 = int(input("Ingrese el número de la opción que desee:"))
            os.system("cls")
            if(opt4 == 1):
                # llamaremos a la funcion que trae el gráfico
                graphicForYear.graphic_for_year()
                response = input("¿Desea más información?: (Si/NO)")
                # validamos si la persona quiere seguir aqui o no
                if(response.lower() == "si"):
                    validate3 = 0
                else:
                    validate3 = 1
            elif(opt4 == 2):
                # llamamos a la funcion que trae el grafico
                graphicForRating.graphic_for_rating()
                response = input("¿Desea más información?: (Si/NO)")
                # validamos si la persona quiere seguir aqui o no
                if(response.lower() == "si"):
                    validate3 = 0
                else:
                    validate3 = 1
            elif(opt4 == 3):
                # llamamos a la funcion que trae el grafico
                graphicForNumReviews.graphic_for_num_reviews()
                response = input("¿Desea más información?: (Si/NO)")
                # validamos si la persona quiere seguir aqui o no
                if(response.lower() == "si"):
                    validate3 = 0
                else:
                    validate3 = 1
            else:
                # si la persona escribe una opcion invalida este sale del while
                print("Opción incorrecta!")
                validate3 = 1
    # acá es para que las opciones a escoger se exporten dependiendo de los rangos que fueron escogidos
    elif(resp == 4):
        validate4 = 0
        # este menu seguirá en funcionanmiento mientras el usuairo lo desee
        while not validate:
            os.system("cls")
            print("¿Cuales rangos desea exportar?")
            print("1-. Rango por año")
            print("2-. Rango por precio")
            print("3-. Rango por calificación")
            print("4-. Rango por acidez del vino")
            opt2 = int(input("Ingrese el número de la opción que desee:"))
            os.system("cls")
            if(opt2 == 1):
                # le indicamos al usuario que ingrese el rango por el cual desea exportar datos
                print("Ingrese el rango de años que desea importar")
                annio1 = input("desde el año: ")
                annio2 = input("Hasta el año: ")
                # llamaremos a la funcion a la cual le pasaremos dos argumentos dados por el usuario
                exportForYear.export_by_year_range(annio1, annio2)
                response = input("¿Desea más información?: (Si/NO) ")
                # validamos si la persona quiere seguir aqui o no
                if(response.lower() == "si"):
                    validate4 = 0
                else:
                    validate4 = 1
            elif(opt2 == 2):
                # le indicamos al usuario que ingrese el rango por el cual desea exportar datos
                print("Ingrese los rangos de precios que desea buscar")
                price1 = input("Desde el Precio: ")
                price2 = input("Hasta el precio: ")
                # llamaremos a la funcion a la cual le pasaremos dos argumentos dados por el usuario
                exportForPrice.export_by_price_range(price1, price2)
                response = input("¿Desea más información?: (Si/NO) ")
                # validamos si la persona quiere seguir aqui o no
                if(response.lower() == "si"):
                    validate4 = 0
                else:
                    validate4 = 1
            elif(opt2 == 3):
                # le indicamos al usuario que ingrese el rango por el cual desea exportar datos
                print("Ingrese el rango del rantig que desea buscar")
                rating1 = input("Desde el rating: ")
                rating2 = input("Hasta el rating: ")
                # llamaremos a la funcion a la cual le pasaremos dos argumentos dados por el usuario
                exportForRating.export_by_rating_range(rating1, rating2)
                response = input("¿Desea más información?: (Si/NO) ")
                # validamos si la persona quiere seguir aqui o no
                if(response.lower() == "si"):
                    validate4 = 0
                else:
                    validate4 = 1
            elif(opt2 == 4):
                # le indicamos al usuario que ingrese el rango por el cual desea exportar datos
                print("Ingrese el rango de acidez por la que desea buscar")
                acidity1 = input("desde la acidez: ")
                acidity2 = input("hasta la acidez: ")
                # llamaremos a la funcion a la cual le pasaremos dos argumentos dados por el usuario
                exportForAcidity.export_by_acidity_range(acidity1, acidity2)
                response = input("¿Desea más información?: (Si/NO)")
                # validamos si la persona quiere seguir aqui o no
                if(response.lower() == "si"):
                    validate4 = 0
                else:
                    validate4 = 1
            else:
                # si la persona escribe una opcion invalida este sale del while
                print("Opción incorrecta!")
                validate = 1
