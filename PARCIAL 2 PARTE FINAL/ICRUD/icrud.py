# ICRUD/icrud.py
from abc import ABC, abstractmethod

import sys
sys.path.append('/Users/57304/Documents/PARCIAL II PARTE FINAL')

from Modelos.Clientes import Cliente,clientes_registrados
from Modelos.Facturas import Factura
from Modelos.ControldePlagas import ControlPlagas
from Modelos.ControldeFertilizantes import ControlFertilizantes
from Modelos.Antibioticos import Antibiotico

class ICrud(ABC):
    @abstractmethod
    def crear_cliente(self, nombre, cedula):
        pass

    @abstractmethod    
    def crear_factura(self, cliente, fecha):
        pass

    @abstractmethod
    def leer_cliente(self, cedula ):
        pass

    @abstractmethod
    def leer_facutra(self, cliente, fecha):
        pass

    @abstractmethod
    def actualizar_cliente(self, cedula, nombre):
        pass

    @abstractmethod
    def actualizar_factura(self, cliente, fecha, nuevos_productos):
        pass

    @abstractmethod
    def eliminar_cliente(self, cedula):
        pass

    @abstractmethod
    def eliminar_factura(self, cliente, fecha):
        pass



class ImpCrudCuenta(ICrud):
    def crear_cliente(self, nombre, cedula):
        nuevo_cliente = Cliente(nombre, cedula)
        clientes_registrados[cedula] = nuevo_cliente  # Agregar el cliente al diccionario de clientes
        return nuevo_cliente
    
    def leer_cliente(self, cedula):
        if cedula in clientes_registrados:
            return clientes_registrados[cedula]
        else:
            return None
        

    def actualizar_cliente(self, cedula, nombre):
        if cedula in clientes_registrados:
            clientes_registrados[cedula].nombre = nombre
            return True
        else:
            return False
        
    def eliminar_cliente(self, cedula):
        if cedula in clientes_registrados:
            del clientes_registrados[cedula]
            return True
        else:
            return False


    def crear_factura(self, cliente, fecha):
        nueva_factura = Factura(fecha, cliente)
        cliente.facturas.append(nueva_factura)  # Agregar la factura al cliente
        return nueva_factura
    
    def leer_facutra(self, cliente, fecha):
        for factura in cliente.facturas:
            if factura.fecha == fecha:
                return factura
        return None
    
   
    def actualizar_factura(self, cliente, fecha, nuevos_productos):
        for factura in cliente.facturas:
            if factura.fecha == fecha:
                factura.productos_comprados = nuevos_productos
                return True
        return False
    
    def eliminar_factura(self, cliente, fecha):
        for factura in cliente.facturas:
            if factura.fecha == fecha:
                cliente.facturas.remove(factura)
                return True
        return False
       