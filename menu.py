opcion = ""

while opcion != "5":
    print("Menu")
    print("1.Ver informacion")
    print("2.Agregar datos")
    print("3.Eliminar datos")
    print("4.Realizar calculos")
    print("5.Salir")

    opcion = input("Elige una opción (1-5):")

    if opcion == "1":
        print("Mostrando informacion")

    elif opcion == "2":
        print("Agregando nuevos datos")

    elif opcion == "3":
        print("Eliminando datos")

    elif opcion == "4":
        print("Realizando calculos")

    elif opcion == "5":
        print("Saliendo del programa Hasta luego bye bye")

    else:
        print("Opción no valida.Por favor,intenta nuevamente.")
        break