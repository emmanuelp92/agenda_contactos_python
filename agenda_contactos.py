def mostrar_menu():
    print("\nAgenda de Comtactos")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Por favor, introduzca el nombre completo del contacto: ")
    telefono = input("Por favor, introduzca el telefono del contacto: ")
    email = input("Por favor, introduzca el correo electrónico del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print("\n")
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Por favor, introduzca el nombre de la persona que desea eliminar: ")  
    if nombre in agenda:
        del agenda[nombre] 
        print(f"El contacto {nombre} ha sido eliminado correctamente.")
    else:
        print(f"No se ha encontrado un contacto con el nombre ingresad {nombre}")
    
def buscar_contacto(agenda):
    nombre = input("Por favor, introduzca el nombre del contacto que está buscando: ")
    if nombre in agenda: 
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"No se ha encontrado un contacto con el nombre ingresado: {nombre}")

def listar_contacto(agenda):
    if agenda:
        print("\nLista de Contactos: ")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info['telefono']}")
            print(f"Email: {info['email']}")
            print("-" * 20)
    else:
        print("La agenda aún está vacía")


def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor, elija una opción: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
            
        elif opcion == "2":
            eliminar_contacto(agenda)

        elif opcion == "3":
            buscar_contacto(agenda)

        elif opcion == "4":
            listar_contacto(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos.")
            break
        else:
            print("Por favor, elija una opción válida")


agenda_contactos()

