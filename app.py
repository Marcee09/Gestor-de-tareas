from gestorTareas import GestorTareas

gestor = GestorTareas()

def menu():
    while True:
        print("Gestor de Tareas")
        print("\n1. Agregar\n2. Listar\n3. Marcar hecha\n4. Eliminar\n5. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            gestor.agregar(input("Título: "), input("Descripción: "))
        elif opcion == "2":
            gestor.listar()
        elif opcion == "3":
            gestor.marcar_hecha(int(input("ID: ")))
        elif opcion == "4":
            gestor.eliminar(int(input("ID: ")))
        elif opcion == "5":
            break

if __name__ == "__main__":
    menu()