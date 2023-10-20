# UI.py

import sys
sys.path.append('/Users/57304/Documents/PARCIAL II PARTE 2')

from Modelos.Clientes import Cliente,clientes_registrados
from Modelos.Facturas import Factura
from Modelos.ControldePlagas import ControlPlagas
from Modelos.ControldeFertilizantes import ControlFertilizantes
from Modelos.Antibioticos import Antibiotico
from CRUD import create, read, update, delete



def lista_clientes():
    if clientes_registrados:
        print("Lista de clientes registrados:")
        for cedula, cliente in clientes_registrados.items():
            print(f"Cédula: {cedula}, Nombre: {cliente.nombre}")
    else:
        print("No hay clientes registrados en la lista.")

def buscar_por_cedula():
    cedula = int(input("Digite el número de cédula del cliente que está buscando: "))
    cliente = read.leer_cliente(cedula)  

    if cliente:
        print(f"Cédula: {cliente.cedula}, Nombre: {cliente.nombre}")
    else:
        print(f"No se encontró ningún cliente con cédula {cedula}")

def registrar_cliente():
    nombre = input("Digite su nombre: ")
    cedula = int(input("Digite su número de identidad: "))
    nuevo_cliente = create.crear_cliente(nombre, cedula)  
    print("Registro exitoso")

def factura():
    print("--COMPRAS PRODUCTOS--")
    cliente_n = buscar_cliente_por_cedula()

    if cliente_n:
        fecha = input("Digite la fecha de la compra: ")
        nueva_factura = create.crear_factura(cliente_n, fecha)  
        registrar_productos(nueva_factura)
        print("\n--- FACTURA ---")
        print(nueva_factura)
    else:
        print("Cliente no encontrado")

def buscar_cliente_por_cedula():
    cedula = int(input("Digite el número de cédula del cliente que está buscando: "))
    cliente = read.leer_cliente(cedula)  
    return cliente

def registrar_productos(factura_cliente):
     while True:
        print("\nOpciones:")
        print("1. Registrar producto de control de plagas")
        print("2. Registrar producto de fertilizantes")
        print("3. Registrar Antibiotico")
        print("4. Salir del registro de compras")

        op = int(input("\nDIGITE LA OPCION QUE DESEA REALIZAR: "))

        if op == 1:
            print("--REGISTRO DE PRODUCTO DE CONTROL DE PLAGAS--")
            registro_ica = int(input("\nDigite el número de registro ICA del producto: "))
            nombre_producto = input("\nDigite el nombre del producto: ")
            frecuencia_aplicacion = input("\nDigite la frecuencia de aplicación: ")
            valor_producto = float(input("\nDigite el valor del producto: "))
            periodo_carencia = int(input("\nDigite el periodo de carencia: "))

            print("\nRegistro exitoso\n")
            Plaga = ControlPlagas(registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto, periodo_carencia)
            factura_cliente.agregar_producto(Plaga)

        elif op == 2:
            print("--REGISTRO DE PRODUCTO DE FERTILIZANTES--")
            registro_ica = int(input("\nDigite el número de registro ICA del producto: "))
            nombre_producto = input("\nDigite el nombre del producto: ")
            frecuencia_aplicacion = input("\nDigite la frecuencia de aplicación: ")
            valor_producto = float(input("\nDigite el valor del producto: "))
            fecha_ultima_aplicacion = input("\nDigite la fecha de última aplicación: ")

            print("\nRegistro exitoso\n")
            Fertilizante = ControlFertilizantes(registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto, fecha_ultima_aplicacion)
            factura_cliente.agregar_producto(Fertilizante)

        elif op == 3:
            print("--REGISTRO DE ANTIBIOTICO--")
            nombre = input("\nDigite el nombre del antibiótico: ")
            dosis = input("\nDigite la dosis del antibiótico(Recuerde que la dosis debe entre 400Kg y 600Kg,y los numeros que digite seran en kilogramos): ")
            tipo_animal = input("\nDigite el tipo de animal al que se aplica: ").lower()  
            precio = float(input("\nDigite el precio del antibiótico: "))
            Antibiotico_registrado = Antibiotico(nombre, dosis, tipo_animal, precio)
            
            try:
                tipo_animal = Antibiotico_registrado.validar_tipo_animal(tipo_animal)
                print("\nRegistro exitoso\n")
                factura_cliente.agregar_producto(Antibiotico_registrado)
            
            except ValueError as e:
                print(f"Error: {e}")

        elif op == 4:
            print("Saliendo de compras. ¡Hasta luego!")
            break  

        else:
            print("Opción no válida. Por favor, elija una opción válida.")

def actualizar_cliente():
    cedula = int(input("Digite la cédula del cliente que desea actualizar: "))
    cliente = read.leer_cliente(cedula) 

    if cliente:
        nuevo_nombre = input("Digite el nuevo nombre del cliente: ")
        update.actualizar_cliente(cedula, nuevo_nombre)  
        print("Cliente actualizado exitosamente")
    else:
        print(f"No se encontró ningún cliente con cédula {cedula}")

def eliminar_cliente():
    cedula = int(input("Digite la cédula del cliente que desea eliminar: "))
    cliente = read.leer_cliente(cedula)  
    if cliente:
        confirmacion = input(f"¿Seguro que desea eliminar al cliente {cliente.nombre}? (S/N): ")
        if confirmacion.lower() == 's':
            delete.eliminar_cliente(cedula)  
            print("Cliente eliminado exitosamente")
        else:
            print("Operación de eliminación cancelada")
    else:
        print(f"No se encontró ningún cliente con cédula {cedula}")


def mostrar_cliente():
    print("Cliente")
    
    cliente = buscar_cliente_por_cedula()

    if cliente:
        print(f" Cliente: {cliente.nombre} (Cédula: {cliente.cedula})")
        if cliente.facturas:
            for factura in cliente.facturas:
                print(f"Fecha: {factura.fecha}")
                for producto in factura.productos_comprados:
                    if isinstance(producto, ControlPlagas):
                        print(f"Control de Plagas - Nombre: {producto.nombre_producto}, Valor: ${producto.valor_producto:.2f}")
                    elif isinstance(producto, ControlFertilizantes):
                        print(f"Control de Fertilizantes - Nombre: {producto.nombre_producto}, Valor: ${producto.valor_producto:.2f}")
                    elif isinstance(producto, Antibiotico):
                        print(f"Antibiótico - Nombre: {producto.nombre}, Valor: ${producto.valor_producto:.2f}")
        else:
            print("El cliente no tiene facturas registradas.")
    else:
        print("Cliente no encontrado.")






    