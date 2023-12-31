import gui

def main():
    while True:
        print("Opciones:")
        print("1. Listar clientes")
        print("2. Buscar cliente por cédula")
        print("3. Registrar cliente")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("6. Registrar factura")
        print("7. Salir")

        opcion = int(input("DIGITE LA OPCIÓN QUE DESEA REALIZAR: "))

        if opcion == 1:
            gui.lista_clientes()
        elif opcion == 2:
            gui.mostrar_cliente()
        elif opcion == 3:
            gui.registrar_cliente()
        elif opcion == 4:
            gui.actualizar_cliente()
        elif opcion == 5:
            gui.eliminar_cliente()
        elif opcion == 6:
            gui.factura()
        elif opcion == 7:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")





if __name__ == '__main__':
    main()

