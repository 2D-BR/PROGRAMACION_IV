# create.py

import sys
sys.path.append('/Users/57304/Documents/PARCIAL II PARTE 2')

from Modelos.Clientes import Cliente,clientes_registrados
from Modelos.Facturas import Factura
from Modelos.ControldePlagas import ControlPlagas
from Modelos.ControldeFertilizantes import ControlFertilizantes
from Modelos.Antibioticos import Antibiotico


def crear_cliente(nombre, cedula):
    nuevo_cliente = Cliente(nombre, cedula)
    clientes_registrados[cedula] = nuevo_cliente  # Agregar el cliente al diccionario de clientes
    return nuevo_cliente

def crear_factura(cliente, fecha):
    nueva_factura = Factura(fecha, cliente)
    cliente.facturas.append(nueva_factura)  # Agregar la factura al cliente
    return nueva_factura
