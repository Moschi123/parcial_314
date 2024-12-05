import os
import random

def limpiar_consola() -> None:
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

def crear_array_bidimensional(filas:int, columnas:int) -> list:
    array = [] 
    for i in range(filas): #crear una fila llena de ceros
        fila = [0] * columnas 
        array += [fila] 
    return array

def ordenar_votos_burbuja(matriz:list, orden:str, clave:int) -> list:
    largo_matriz = len(matriz)

    for i in range(largo_matriz):
        for j in range(0, largo_matriz-i-1):
            if (orden == 'asc' and matriz[j][clave] > matriz[j+1][clave]) or (orden == 'desc' and matriz[j][clave] < matriz[j+1][clave]):
                matriz[j], matriz[j+1] = matriz[j+1], matriz[j]

    return matriz

def cargar_notas_participantes(lista_participantes:list) -> list:

    for i in range(len(lista_participantes)):
        lista_participantes[i][0] = i+1

        print(f"Empecemos por el participante N°{i+1}")

        for j in range(1,4):
            while True:
                    try:
                        lista_participantes[i][j] = int(input(f"Ingrese el voto del jurado nro {j}(del 1 a 100): "))
                        if lista_participantes[i][j] < 1 or lista_participantes[i][j] > 100:
                            print(f"Sólo se pueden ingresar numeros del 1 al 100")
                        else:
                            break
                    except ValueError:
                        print("Por favor ingrese un número válido.")

        lista_participantes[i][5] = lista_participantes[i][1] + lista_participantes[i][2] + lista_participantes[i][3]
        promedio_participante = (lista_participantes[i][5] / 3)
        lista_participantes[i][4] = promedio_participante

        print("\n")
        
    return lista_participantes

def mostrar_notas(lista_participantes: list,cantidad_participantes: int) -> None:

    print(f"\n{'Participante n° ':<15}|{' Nota 1er jurado ':<15}|{' Nota 2do jurado ':<15}|{' Nota 3er jurado ':<15}|{' Promedio ':<15}")
    print("=" * 75) 

    for i in range(cantidad_participantes): # Mostrar los datos de cada lista
        numero_participante = lista_participantes[i][0]
        primer_nota = lista_participantes[i][1]
        segunda_nota = lista_participantes[i][2]
        tercera_nota = lista_participantes[i][3]
        promedio_participante = lista_participantes[i][4]

        print(f"\t{numero_participante:<15}{primer_nota:<15}{segunda_nota:<15}{tercera_nota:<15}{promedio_participante:.2f}")
        print("\n")

def mostrar_tres_peores_promedios(lista_participantes:list) -> None:

    lista_participantes_ordenada = ordenar_votos_burbuja(lista_participantes,"asc",4)     
    
    print("Los 3 peores promedios son: ")
    mostrar_notas(lista_participantes_ordenada,3)

def mostrar_mayores_promedios(lista_participantes: list) -> None:

    lista_participantes_ordenada = ordenar_votos_burbuja(lista_participantes,"desc",4)
    cantidad_mayor_promedio = 0 
    promedio_total = 0

    for fila in lista_participantes_ordenada:
        promedio_total += fila[4]
    promedio_total /= 5

    for fila in lista_participantes_ordenada:
        if fila[4] > promedio_total:
            cantidad_mayor_promedio += 1

    print(f"Los {cantidad_mayor_promedio} mejores promedios son: ")
    mostrar_notas(lista_participantes_ordenada,cantidad_mayor_promedio)

def mostrar_jurado_malo(lista_participantes: list) -> None:

    jurados_promedio = [[1,0],[2,0],[3,0]]
    
    for fila in lista_participantes:
        jurados_promedio[0][1] += fila[1]
        jurados_promedio[1][1] += fila[2]
        jurados_promedio[2][1] += fila[3]

    jurados_promedio = ordenar_votos_burbuja(jurados_promedio,"asc",1) 
        
    print("El jurado que dio las peores notas es/son:")
    for i in range(3):
        if jurados_promedio[i][1] == jurados_promedio[0][1]:
            print(f"Jurado {jurados_promedio[i][0]}")
    print("\n")

def ordenar_lista(lista:list,orden:str) -> list:
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-i):
            if (orden == 'asc' and lista[j] > lista[j+1]) or (orden == 'desc' and lista[j] < lista[j]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def mostrar_sumatoria(lista_participantes: list) -> None: 
    cantidad_acertados = 0

    numero = int(input(f"Ingrese un numero del 3 al 300: "))
    while numero < 3 and numero > 300:
        numero = int(input(f"Ingreso un numero fuera de rango, ingrese nuevamente un numero del 3 al 300: "))

    for fila in lista_participantes:
        if numero == fila[5]:
            cantidad_acertados += 1
    
    if cantidad_acertados > 0:
        lista_participantes_numero_acertado = crear_array_bidimensional(cantidad_acertados,6)
        j = 0
        for i in range(len(lista_participantes)):
            if numero == lista_participantes[i][5]:
                lista_participantes_numero_acertado[j] = lista_participantes[i]
                j += 1

        print(f"El/Los participante/s que la suma de sus notas da {numero} es/son: ")
        mostrar_notas(lista_participantes_numero_acertado,cantidad_acertados)
    else:
        print(f"Error: Ningun participante coincide la suma de sus notas con el número ingresado.")

def definir_ganador(lista_participantes: list) -> None:
    cantidad_mejor_promedio = 0
    lista_participantes = ordenar_votos_burbuja(lista_participantes,"desc",4)
    
    for fila in lista_participantes:
        if lista_participantes[0][0] != fila[0]:
            if lista_participantes[0][4] == fila[4]:
                cantidad_mejor_promedio += 1
        
    if cantidad_mejor_promedio > 0:
        return desempatar(lista_participantes, cantidad_mejor_promedio+1)
    else: 
        print("El ganador del concurso es: ")
        return lista_participantes[0]

def desempatar(lista_participantes: list, cantidad_mejor_promedio:int):
    limpiar_consola()

    jurados = [0,0,0]
    participantes = crear_array_bidimensional(5,2)
    participante_ganador = [0,0,0,0,0,0]
    ganadores = [lista_participantes[i][0] for i in range(cantidad_mejor_promedio)]

    print("Los siguientes participantes tuvieron la mejor nota: ")
    mostrar_notas(lista_participantes,cantidad_mejor_promedio)
    print("Es hora de desempatar... Jurados, elijan al participante que desee que gane: ")
        
    for i in range(3):
        while True:
            try:
                jurados[i] = int(input(f"Jurado {i+1}: Ingrese el numero de participante que desea que gane: "))

                if jurados[i] not in ganadores:
                    print(f"¡Este participante no es un ganador! Elija uno de los siguientes ganadores: {ganadores}")
                else:
                    break
            except ValueError:
                print("Por favor ingrese un número válido.")
        for j in range(len(participantes)):
            participantes[j][0] = j+1
            if jurados[i] == j+1:
                participantes[j][1] += 1
                
    participantes = ordenar_votos_burbuja(participantes,"desc",1)
    

    if participantes[0][1] == 2:
        participante_ganador = guardar_participante_ganador(lista_participantes,participantes[0][0])
        return participante_ganador
    elif participantes[1][1] == 2:
        participante_ganador = guardar_participante_ganador(lista_participantes,participantes[1][0])
        return participante_ganador
    elif participantes[2][1] == 2:    
        participante_ganador = guardar_participante_ganador(lista_participantes,participantes[2][0])
        return participante_ganador
    elif participantes[3][1] == 2:    
        participante_ganador = guardar_participante_ganador(lista_participantes,participantes[3][0])
        return participante_ganador
    elif participantes[4][1] == 2:    
        participante_ganador = guardar_participante_ganador(lista_participantes,participantes[4][0])
        return participante_ganador
    else:

        print("\nParece que los jurados eligieron distintos participantes...\nSe elegira un numero al azar y ese sera el participante ganador.")

        posibles_ganadores = crear_array_bidimensional(cantidad_mejor_promedio,6)
        posibles_ganadores = [lista_participantes[i] for i in range(cantidad_mejor_promedio)]
        random.shuffle(posibles_ganadores)
        return posibles_ganadores[0]

def guardar_participante_ganador(lista,numero_participante):
    participante_ganador = [0,0,0,0,0,0]
    for i in range(len(lista)):
        if lista[i][0] == numero_participante:
            for j in range(len(participante_ganador)):
                participante_ganador[j] = lista[i][j]
    return participante_ganador

def mostrar_ganador(participante_ganador: list) -> None: 
    print(f"\nEl Participante Ganador es: ")
    print(f"\n{'Participante n° ':<15}|{' Nota 1er jurado ':<15}|{' Nota 2do jurado ':<15}|{' Nota 3er jurado ':<15}|{' Promedio ':<15}")
    print("=" * 75) #linea que deja lindo el mostrar 
    numero_participante = participante_ganador[0]
    primer_nota = participante_ganador [1]
    segunda_nota = participante_ganador[2]
    tercera_nota = participante_ganador[3]
    promedio_participante = participante_ganador[4]

    print(f"\t{numero_participante:<15}{primer_nota:<15}{segunda_nota:<15}{tercera_nota:<15}{promedio_participante:.2f}")
    print("\n")


            


        