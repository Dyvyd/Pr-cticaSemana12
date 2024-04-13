#Ejercicio #2

print("Ejercicio #2")
print("Programa que muestra las estadísticas de La Casadora S.A.")

#Creación de matriz que organizará los datos
datos = []

#Función del menú principal
def menu():
    print("\nBienvenido al menú")
    print("Ingrese una opción\n")
    print("1 - Ingresar datos")
    print("2 - Mostrar estadísticas")
    print("3 - Salir")
    op = input(">>")
    return op

#Función del condicional
def condicional():
    #Variable que determina si la opción es válida
    valido = True

    while(valido == True):
        
        op = menu()
        
        #Condicional
        if(op == "1"):
            ingresar_datos(datos)
        elif(op == "2"):
            mostrar_datos(datos)
        elif(op == "3"):
            print("Usted saldrá correctamente")
            valido = False
        else:
            print("Ingrese una opción válida")

#Función para ingresar datos
def ingresar_datos(datos):

    for dia in range(5):
        for servicio in range(4):

            #Variables locales
            cantidad = 0
            valido = False

            while (valido == False):
                #Solicitud de datos
                print("Ingrese la cantidad de pasajeros del día", dia + 1, "en el servicio", servicio + 1)
                cantidad = int(input(">>"))

                #Verifica que no sean más de 60
                if(cantidad > 60):
                    print("La capacidad máxima del autobus es de 60, ingrese un valor correcto")
                else:
                    valido = True

            #Agrega los datos a la matriz
            datos.append([cantidad,servicio,dia])

#Función para mostrar datos  
def mostrar_datos(datos):
    #Verifica si hay datos
    if(datos == []):
        print("No hay datos almacenados")
    else:
        print("\nEstadísticas\n")
        
        print("El promedio de pasajeros del día #1 es:", promedio_dia(1, datos))
        print("El mejor servicio en el día #1 es:", mejor_servicio(1, datos))
        print("El promedio de pasajeros del día #2 es:", promedio_dia(2, datos))
        print("El mejor servicio en el día #2 es:", mejor_servicio(2, datos))
        print("El promedio de pasajeros del día #3 es:", promedio_dia(3, datos))
        print("El mejor servicio en el día #3 es:", mejor_servicio(3, datos))
        print("El promedio de pasajeros del día #4 es:", promedio_dia(4, datos))
        print("El mejor servicio en el día #4 es:", mejor_servicio(4, datos))
        print("El promedio de pasajeros del día #5 es:", promedio_dia(5, datos))
        print("El mejor servicio en el día #5 es:", mejor_servicio(5, datos))
        
        print("\nEl promedio de pasajeros es:", promedio(datos))
        
        print("El día y servicio en el que menos se transportaron es:", peor_dia(datos))

#Función para el promedio del día
def promedio_dia(dia, datos):

    #Variable para acumular el promedio
    promedio = 0

    #Ciclo que recorre la matriz
    for fila in range(20):
        if(datos[fila][2] == dia - 1):
            #Acumula el valor
            promedio += datos[fila][0]

    #Cálculo del promedio
    promedio /= 4

    #Retorna el promedio
    return promedio

#Función para el mejor servicio del día
def mejor_servicio(dia, datos):

    #Variable para calcular el mejor servicio
    mejor = 0
    mejor_servicio = 0

    #Ciclo que recorre la matriz
    for fila in range(20):
        if(datos[fila][2] == dia - 1):
            if(datos[fila][0] >= mejor):
                mejor = datos[fila][0]
                mejor_servicio = datos[fila][1]

    #Retorna el mejor servicio
    return mejor_servicio + 1

#Función para calcular el promedio general
def promedio(datos):
    #Variable para acumular el promedio
    promedio = 0

    #Ciclo que recorre la matriz
    for fila in range(20):
        promedio += datos[fila][0]

    #Cálculo del promedio
    promedio /= 5

    #Retorna el promedio
    return promedio

def peor_dia(datos):
    #Variables locales
    peor = 60
    dia = 0
    servicio = 0

    #Ciclo que recorre la matriz
    for fila in range(20):
        if(datos[fila][0] <= peor):
            peor = datos[fila][0]
            dia = datos[fila][2]
            servicio = datos[fila][1]

    return dia, servicio
    


#Invoca el condicional
condicional()







            
