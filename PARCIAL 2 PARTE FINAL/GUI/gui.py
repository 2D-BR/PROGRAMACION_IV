
# UI.py

import sys
sys.path.append('/Users/57304/Documents/PARCIAL II PARTE FINAL')

from Modelos.Clientes import Cliente,clientes_registrados
from Modelos.Facturas import Factura
from Modelos.ControldePlagas import ControlPlagas
from Modelos.ControldeFertilizantes import ControlFertilizantes
from Modelos.Antibioticos import Antibiotico

import tkinter as tk
from tkinter import messagebox, simpledialog
from ICRUD.icrud import ImpCrudCuenta  # Asegúrate de importar la implementación concreta adecuada

icrud_cuenta = ImpCrudCuenta() # Ahora acepta una instancia de ICrud

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión")

        # Botones
        self.btn_lista_clientes = tk.Button(root, text="Listar Clientes", command=self.lista_clientes)
        self.btn_buscar_por_cedula = tk.Button(root, text="Buscar por Cédula", command=self.buscar_por_cedula)
        self.btn_registrar_cliente = tk.Button(root, text="Registrar Cliente", command=self.registrar_cliente)
        self.btn_factura = tk.Button(root, text="Realizar Compra", command=self.factura)
        self.btn_actualizar_cliente = tk.Button(root, text="Actualizar Cliente", command=self.actualizar_cliente)
        self.btn_eliminar_cliente = tk.Button(root, text="Eliminar Cliente", command=self.eliminar_cliente)
        self.btn_mostrar_cliente = tk.Button(root, text="Mostrar Cliente", command=self.mostrar_cliente)

        # Diseño de la interfaz
        self.btn_lista_clientes.pack()
        self.btn_buscar_por_cedula.pack()
        self.btn_registrar_cliente.pack()
        self.btn_factura.pack()
        self.btn_actualizar_cliente.pack()
        self.btn_eliminar_cliente.pack()
        self.btn_mostrar_cliente.pack()

    def lista_clientes(self):
        if clientes_registrados:
            lista_clientes_str = "\n".join([f"Cédula: {cedula}, Nombre: {cliente.nombre}" for cedula, cliente in clientes_registrados.items()])
            messagebox.showinfo("Clientes Registrados", lista_clientes_str)
        else:
            messagebox.showinfo("Clientes Registrados", "No hay clientes registrados en la lista.")
    
    def buscar_por_cedula(self):
        #simpledialog para pedir la cédula al usuario
        cedula = simpledialog.askinteger("Buscar por Cédula", "Digite el número de cédula del cliente que está buscando:")

        cliente = icrud_cuenta.leer_cliente(cedula)

        if cliente:
            #información del cliente
            messagebox.showinfo("Información del Cliente", f"Cédula: {cliente.cedula}, Nombre: {cliente.nombre}")
        else:
            #mensaje si el cliente no se encuentra
            messagebox.showinfo("Cliente no encontrado", f"No se encontró ningún cliente con cédula {cedula}")

    def registrar_cliente(self):
        # Utilizamos simpledialog para pedir la información al usuario
        nombre = simpledialog.askstring("Registrar Cliente", "Digite su nombre:")
        cedula = simpledialog.askinteger("Registrar Cliente", "Digite su número de identidad:")

        # Llamamos a la función crear_cliente de la instancia de ICrud
        nuevo_cliente = icrud_cuenta.crear_cliente(nombre, cedula)

        if nuevo_cliente:
            messagebox.showinfo("Registro Exitoso", "Cliente registrado exitosamente.")
        else:
            messagebox.showinfo("Error en el Registro", "Hubo un error al registrar el cliente.")

    def factura(self):
        # Utilizamos simpledialog para pedir la cédula al usuario
        cedula = simpledialog.askinteger("Facturar", "Digite el número de cédula del cliente:")

        # Llamamos a la función leer_cliente de la instancia de ICrud
        cliente = icrud_cuenta.leer_cliente(cedula)

        if cliente:
            fecha = simpledialog.askstring("Facturar", "Digite la fecha de la compra:")
            nueva_factura = icrud_cuenta.crear_factura(cliente, fecha)
            
            
            if nueva_factura:
                self.registrar_productos(nueva_factura)
                info_factura = "\n--- FACTURA ---\n" + str(nueva_factura)

                # Muestra la información en el cuadro de mensaje
                messagebox.showinfo("Facturación Exitosa", "La factura se ha creado exitosamente." + info_factura)
            else:
                messagebox.showinfo("Error en la Facturación", "Hubo un error al crear la factura.")
        else:
            messagebox.showinfo("Cliente no encontrado", f"No se encontró ningún cliente con cédula {cedula}")


    def registrar_productos(self, factura_cliente):
        def salir(ventana):
            # Función para salir del bucle y destruir la ventana
            nonlocal salir_del_registro
            salir_del_registro = True
            ventana.destroy()

        factura_window = tk.Toplevel(self.root)
        factura_window.title("Registro de Compra")

        salir_del_registro = False  # Variable de control

        while not salir_del_registro:
            # Crear etiqueta para mostrar las opciones
            opciones_label = tk.Label(factura_window, text="\nOpciones:")
            opciones_label.pack()

            # Crear botones para cada opción
            btn_opcion1 = tk.Button(factura_window, text="Registrar producto de control de plagas", command=lambda: self.registrar_control_plagas(factura_cliente, factura_window))
            btn_opcion2 = tk.Button(factura_window, text="Registrar producto de fertilizantes", command=lambda: self.registrar_fertilizantes(factura_cliente, factura_window))
            btn_opcion3 = tk.Button(factura_window, text="Registrar Antibiotico", command=lambda: self.registrar_antibiotico(factura_cliente, factura_window))
            btn_opcion4 = tk.Button(factura_window, text="Salir del registro de compras", command=lambda: salir(factura_window))

            # Colocar botones en la ventana
            btn_opcion1.pack()
            btn_opcion2.pack()
            btn_opcion3.pack()
            btn_opcion4.pack()

            # Esperar hasta que la ventana de la factura se cierre
            factura_window.wait_window()


    

            

    def registrar_control_plagas(self, factura_cliente, window):
        print("--REGISTRO DE PRODUCTO DE CONTROL DE PLAGAS--")
        registro_ica = simpledialog.askinteger("Registrar Compra", "Digite el número de registro ICA del producto:")
        nombre_producto = simpledialog.askstring("Registrar Compra", "Digite el nombre del producto:")
        frecuencia_aplicacion = simpledialog.askstring("Registrar Compra", "Digite la frecuencia de aplicación:")
        valor_producto = simpledialog.askfloat("Registrar Compra", "Digite el valor del producto:")
        periodo_carencia = simpledialog.askinteger("Registrar Compra", "Digite el periodo de carencia:")

        print("\nRegistro exitoso\n")
        plaga = ControlPlagas(registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto, periodo_carencia)
        factura_cliente.agregar_producto(plaga)

        

    def registrar_fertilizantes(self, factura_cliente, window):
        print("--REGISTRO DE PRODUCTO DE FERTILIZANTES--")
        registro_ica = simpledialog.askinteger("Registrar Compra", "Digite el número de registro ICA del producto:")
        nombre_producto = simpledialog.askstring("Registrar Compra", "Digite el nombre del producto:")
        frecuencia_aplicacion = simpledialog.askstring("Registrar Compra", "Digite la frecuencia de aplicación:")
        valor_producto = simpledialog.askfloat("Registrar Compra", "Digite el valor del producto:")
        fecha_ultima_aplicacion = simpledialog.askstring("Registrar Compra", "Digite la fecha de última aplicación:")

        print("\nRegistro exitoso\n")
        fertilizante = ControlFertilizantes(registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto, fecha_ultima_aplicacion)
        factura_cliente.agregar_producto(fertilizante)


    def registrar_antibiotico(self, factura_cliente, window):
        print("--REGISTRO DE ANTIBIOTICO--")
        nombre = simpledialog.askstring("Registrar Compra", "Digite el nombre del antibiótico:")
        dosis = simpledialog.askstring("Registrar Compra", "Digite la dosis del antibiótico (Recuerde que la dosis debe ser entre 400Kg y 600Kg, y los números que digite serán en kilogramos):")
        tipo_animal = simpledialog.askstring("Registrar Compra", "Digite el tipo de animal al que se aplica:").lower()
        precio = simpledialog.askfloat("Registrar Compra", "Digite el precio del antibiótico:")

        antibiotico_registrado = Antibiotico(nombre, dosis, tipo_animal, precio)
        
        try:
            tipo_animal = antibiotico_registrado.validar_tipo_animal(tipo_animal)
            print("\nRegistro exitoso\n")
            factura_cliente.agregar_producto(antibiotico_registrado)
        
        except ValueError as e:
            print(f"Error: {e}")

       



    def actualizar_cliente(self):
        #simpledialog para pedir la cédula al usuario
        cedula = simpledialog.askinteger("Actualizar Cliente", "Digite la cédula del cliente que desea actualizar:")

        # Llamamos a la función leer_cliente de la instancia de ICrud
        cliente = icrud_cuenta.leer_cliente(cedula)

        if cliente:
            
            nuevo_nombre = simpledialog.askstring("Actualizar Cliente", "Digite el nuevo nombre del cliente:")

            
            icrud_cuenta.actualizar_cliente(cedula, nuevo_nombre)

            messagebox.showinfo("Actualización Exitosa", "Cliente actualizado exitosamente.")
        else:
            messagebox.showinfo("Cliente no encontrado", f"No se encontró ningún cliente con cédula {cedula}")


    def eliminar_cliente(self):
        
        cedula = simpledialog.askinteger("Eliminar Cliente", "Digite la cédula del cliente que desea eliminar:")

      
        cliente = icrud_cuenta.leer_cliente(cedula)

        if cliente:
            # Utilizamos messagebox para confirmar la eliminación
            confirmacion = messagebox.askquestion("Confirmación", f"¿Seguro que desea eliminar al cliente {cliente.nombre}?")

            if confirmacion == 'yes':
               
                icrud_cuenta.eliminar_cliente(cedula)

                messagebox.showinfo("Eliminación Exitosa", "Cliente eliminado exitosamente.")
            else:
                messagebox.showinfo("Operación Cancelada", "Operación de eliminación cancelada.")
        else:
            messagebox.showinfo("Cliente no encontrado", f"No se encontró ningún cliente con cédula {cedula}")


    def mostrar_cliente(self):
       
        cedula = simpledialog.askinteger("Mostrar Cliente", "Digite la cédula del cliente que desea mostrar:")

        
        cliente = icrud_cuenta.leer_cliente(cedula)

        if cliente:
            # mensaje con la información del cliente y sus facturas
            mensaje = f"Cliente: {cliente.nombre} (Cédula: {cliente.cedula})\n"

            if cliente.facturas:
                for factura in cliente.facturas:
                    mensaje += f"\nFecha: {factura.fecha}\n"
                    for producto in factura.productos_comprados:
                        if isinstance(producto, ControlPlagas):
                            mensaje += f"Control de Plagas - Nombre: {producto.nombre_producto}, Valor: ${producto.valor_producto:.2f}\n"
                        elif isinstance(producto, ControlFertilizantes):
                            mensaje += f"Control de Fertilizantes - Nombre: {producto.nombre_producto}, Valor: ${producto.valor_producto:.2f}\n"
                        elif isinstance(producto, Antibiotico):
                            mensaje += f"Antibiótico - Nombre: {producto.nombre}, Valor: ${producto.valor_producto:.2f}\n"
            else:
                mensaje += "El cliente no tiene facturas registradas."

            # Utilizamos messagebox para mostrar la información del cliente
            messagebox.showinfo("Información del Cliente", mensaje)
        else:
            messagebox.showinfo("Cliente no encontrado", f"No se encontró ningún cliente con cédula {cedula}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
