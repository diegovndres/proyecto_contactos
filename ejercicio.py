import os, time
from funciones import *

while True:
    os.system('cls')
    print("MENU CONTACTOS")
    print("1. AGREGAR CONTACTOS")
    print("2. VER CONTACTOS")
    print("3. EXPORTAR ARCHIVO")
    print("4. SALIR")
    opc = int(input("Ingrese opción: "))

    os.system('cls')
    if opc==1:
        opcion_1()
    elif opc==2:
        opcion_2()
    elif opc==3:
        opcion_3()
    else:
        opcion_4()
    time.sleep(3)