#Ejercicio 4
import os

ingresos = ["juan", "felipe", "carlos"]

#Crear Archivo

def crear():
    archivo = open("Ingresos.txt", "a+")
    archivo.close()
def subir():
    archivo = open("Ingresos.txt", "w")
    archivo.write(str(ingresos))
    archivo.close()

def guardar():
    archivo = open("Ingresos.txt", "r")
    ing = archivo.read()
    ing = eval(ing)
    global ingresos
    ingresos = ing
    archivo.close()


#Aplicación 1 registrar el ingreso

def ingreso():
    global ingresos
    print()
    print("Desea ingresar al sistema? ")
    print()
    op = str(input(":"))
    salir = False
    while len(ingresos)<10 and salir==False:
            print(salir, op)
            if op.upper() == "SI":
                nomb = str(input("Digite su nombre"))
                ingresosUpper = []
                for i in ingresos:
                    ingresosUpper += [i.upper()]
                print(ingresosUpper)
                if nomb.upper() not in ingresosUpper:
                    ingresos += [nomb]                    
                    print("Ingresado con exito", ingresos)
            if salir == False or up.upper()== "NO":
                print("Desea seguir?")
                op = str(input(": "))
                if op.upper() == "SI":
                    continue
                elif op.upper() == "NO":
                    salir = True
    subir()
    guardar()
    if len(ingresos)>= 10:
        print("+10")
crear()
guardar()


def egreso():
    egresados = []
    global ingresos
    print()
    egresar = input("Escriba el nombre de la persona a sacar: ")
    for i in ingresos:
        if i.upper() != egresar.upper():
            egresados += [i]
            ingresos = egresados
        elif i.upper() == egresar.upper():
            continue
    if egresar not in ingresos:
        print("Nombre no disponible")
        
subir()
guardar()

crear()
guardar()


while True:
    print()
    print()
    print("Desea ingresar a alguien (1), egresar a alguien del sistema(2), o salir(3)")
    print()
    print()
    op = int(input(""))

    if op == 1:
        ingreso()
    elif op == 2:
        egreso()
    elif op == 3:
        break
