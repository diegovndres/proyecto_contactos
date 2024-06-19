
contactos = []

def opcion_1():
    print("AGREGAR CONTACTO")
    nombre = input("Ingrese nombre: ")
    telefono = int(input("Ingrese teléfono: "))
    correo = input("Ingrese correo: ")
    contacto = {"nombre":nombre,"telefono":telefono,"correo":correo}
    contactos.append(contacto)
    print("CONTACTO AGREGADO :)!")
def opcion_2():
    if not contactos:
        print("No existen contactos, registre uno en la opcion 1!")
    else:
        print("LISTA DE CONTACTOS")
        for c in contactos:
            print(f"NOMBRE: {c['nombre']}")
            print(f"TELEFONO: {c['telefono']}")
            print(f"CORREO: {c['correo']}")

def opcion_3():
    if not contactos:
        print("NO EXISTEN CONTACTOS,REGISTRE UNO EN LA OPCION 1!")
    else:
        nombre_archivo = input("Ingrese nombre del archivo: ")+".csv"
        import csv
        with open(nombre_archivo,"w",newline="") as archivo:
            escritor = csv.DictWriter(archivo, ["nombre","telefono","correo"])
            escritor.writerows(contactos)
def opcion_4():
    print("GRACIAS")
    exit()

def validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
            