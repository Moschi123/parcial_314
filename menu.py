from funciones import *

def mostrar_menu():
    participantes_ingresados = crear_array_bidimensional(5,6)
    notas_cargadas = False
    salir = True
    ganador_definitivo = False
    while(salir):
        print("Masterchef UTN\n1-Cargar notas de los participantes.\n2-Mostrar Notas.\n3-Ordenar notas por promedio.\n4-Peores 3 notas.\n5-Mayores promedios.\n6-Jurados malos.\n7-mostrar_sumatoria.\n8-Definir el  Ganador.\n9.Salir\n")

        while True:
            try:
                boton = int(input("Ingrese su boton( 1 - 9): "))

                if boton < 1 or boton > 9:
                    print(f"Ingresar un numero  del 1 - 9")
                else:
                    break
            except ValueError:
                print("Ingrese un número válido entre 1- 9.")
            
        if boton == 1:
            participantes_ingresados = cargar_notas_participantes(participantes_ingresados)
            notas_cargadas = True
        elif notas_cargadas:
            if boton == 2:
                mostrar_notas(participantes_ingresados,5)
            elif boton == 3:
                while True:
                    try:
                        orden_puntaje = input("De que forma quiere ordenarlos? de Forma ascendente ( asc) o  descendente (desc):")
                        if orden_puntaje != "asc" and orden_puntaje != "desc":
                            print(f"Las botones disponibles de ingresar son asc o desc")
                        else:
                            break
                    except ValueError:
                        print("Por favor ingrese (asc o des)Despues de este mensaje.")
                participantes_ingresados = ordenar_votos_burbuja(participantes_ingresados,orden_puntaje,4)
                print("Se ordenaron los participantes por su  promedio ")
                limpiar_consola()
            elif boton == 4:
                mostrar_tres_peores_promedios(participantes_ingresados)
            elif boton == 5:
                mostrar_mayores_promedios(participantes_ingresados)
            elif boton == 6:
                mostrar_jurado_malo(participantes_ingresados)
            elif boton == 7:
                mostrar_sumatoria(participantes_ingresados)
            elif boton == 8:
                if ganador_definitivo == False:
                    ganador = definir_ganador(participantes_ingresados)
                mostrar_ganador(ganador)
                ganador_definitivo = True
            elif boton == 9:
                salir = False
        elif boton == 9:
            salir = False
        else:
            print("Las notas todavía no están en el sistema")
        limpiar_consola()
mostrar_menu()