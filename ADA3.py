
postres = {
    "Tarta de manzana": ["manzanas", "azúcar", "canela", "masa"],
    "Brownie": ["chocolate", "azúcar", "huevos", "harina"],
    "Flan": ["huevos", "leche", "azúcar", "vainilla"]
}

def imprimir_ingredientes(postre):
    """Imprime la lista de ingredientes de un postre dado."""
    if postre in postres:
        print(f"Ingredientes de {postre}: {', '.join(postres[postre])}")
    else:
        print("El postre no existe.")

def agregar_ingrediente(postre, ingrediente):
    """Agrega un nuevo ingrediente a la lista de un postre."""
    if postre in postres:
        if ingrediente not in postres[postre]:
            postres[postre].append(ingrediente)
            print(f"Ingrediente '{ingrediente}' agregado a {postre}.")
        else:
            print(f"El ingrediente '{ingrediente}' ya está en la lista.")
    else:
        print("El postre no existe.")

def eliminar_ingrediente(postre, ingrediente):
    """Elimina un ingrediente de la lista de un postre sin eliminar el postre."""
    if postre in postres:
        if ingrediente in postres[postre]:
            postres[postre].remove(ingrediente)
            print(f"Ingrediente '{ingrediente}' eliminado de {postre}.")
        else:
            print(f"El ingrediente '{ingrediente}' no se encuentra en la lista.")
    else:
        print("El postre no existe.")

def agregar_postre(postre, ingredientes):
    """Agrega un nuevo postre con su lista de ingredientes."""
    if postre not in postres:
        if isinstance(ingredientes, list) and all(isinstance(i, str) for i in ingredientes):
            postres[postre] = ingredientes
            print(f"Postre '{postre}' agregado con éxito.")
        else:
            print("Los ingredientes deben ser una lista de cadenas.")
    else:
        print("El postre ya existe.")

def eliminar_postre(postre):
    """Elimina un postre y su lista de ingredientes."""
    if postre in postres:
        del postres[postre]
        print(f"Postre '{postre}' y sus ingredientes eliminados con éxito.")
    else:
        print("El postre no existe.")

def mover_ingrediente(postre_origen, postre_destino, ingrediente):
    """Mueve un ingrediente de un postre a otro."""
    if postre_origen in postres and postre_destino in postres:
        if ingrediente in postres[postre_origen]:
            
            agregar_ingrediente(postre_destino, ingrediente)
           
            eliminar_ingrediente(postre_origen, ingrediente)
            print(f"Ingrediente '{ingrediente}' movido de {postre_origen} a {postre_destino}.")
        else:
            print(f"El ingrediente '{ingrediente}' no se encuentra en {postre_origen}.")
    else:
        if postre_origen not in postres:
            print(f"El postre origen '{postre_origen}' no existe.")
        if postre_destino not in postres:
            print(f"El postre destino '{postre_destino}' no existe.")

def eliminar_ingredientes_repetidos():
    """Elimina ingredientes duplicados de cada postre."""
    for postre, ingredientes in postres.items():
    
        ingredientes_unicos = list(set(ingredientes))
        postres[postre] = ingredientes_unicos
        print(f"Ingredientes duplicados eliminados de {postre}. Nueva lista: {ingredientes_unicos}")

def menu():
    """Muestra el menú y permite al usuario interactuar con el programa."""
    while True:
        print("\n--- Menú ---")
        print("1. Imprimir ingredientes")
        print("2. Agregar ingrediente")
        print("3. Eliminar ingrediente")
        print("4. Agregar nuevo postre")
        print("5. Eliminar un postre")
        print("6. Mover ingrediente entre postres")
        print("7. Eliminar ingredientes duplicados") 
        print("8. Salir")

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == '1':
            nombre_postre = input("Ingrese el nombre del postre: ")
            imprimir_ingredientes(nombre_postre)
        
        elif opcion == '2':
            nombre_postre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el nombre del ingrediente a agregar: ")
            agregar_ingrediente(nombre_postre, ingrediente)

        elif opcion == '3':
            nombre_postre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el nombre del ingrediente a eliminar: ")
            eliminar_ingrediente(nombre_postre, ingrediente)

        elif opcion == '4':
            nombre_postre = input("Ingrese el nombre del nuevo postre: ")
            ingredientes_input = input("Ingrese los ingredientes separados por comas: ")
            ingredientes = [i.strip() for i in ingredientes_input.split(',')]  
            agregar_postre(nombre_postre, ingredientes)

        elif opcion == '5':
            nombre_postre = input("Ingrese el nombre del postre a eliminar: ")
            eliminar_postre(nombre_postre)

        elif opcion == '6':
            origen = input("Ingrese el nombre del postre origen: ")
            destino = input("Ingrese el nombre del postre destino: ")
            ingrediente = input("Ingrese el nombre del ingrediente a mover: ")
            mover_ingrediente(origen, destino, ingrediente)

        elif opcion == '7':
            eliminar_ingredientes_repetidos() 

        elif opcion == '8':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


menu()
