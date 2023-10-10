import unittest


from Modelos.Clientes import Cliente
from Modelos.Facturas import Factura
from Modelos.ControldePlagas import ControlPlagas
from Modelos.ControldeFertilizantes import ControlFertilizantes
from Modelos.Antibioticos import Antibiotico

class TestClienteFactura(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Juan Pérez", "123456789")
        self.factura = Factura("2023-10-05", self.cliente)
        self.plaga1 = ControlPlagas(12345, "Plaga 1", "Quincenal", 50.0, 7)
        self.plaga2 = ControlPlagas(67890, "Plaga 2", "Mensual", 30.0, 14)
        self.fertilizante1 = ControlFertilizantes(54321, "Fertilizante 1", "Mensual", 40.0, "2023-09-30")
        self.antibiotico1 = Antibiotico("Antibiótico 1", "500Kg", "bovinos", 15.0)  # Dosis válida: 500Kg

    def test_agregar_producto_factura(self):
        self.factura.agregar_producto(self.plaga1)
        self.assertEqual(len(self.factura.productos_comprados), 1)

        self.factura.agregar_producto(self.plaga2)
        self.assertEqual(len(self.factura.productos_comprados), 2)

    def test_valor_total_factura(self):
        self.factura.agregar_producto(self.plaga1)
        self.factura.agregar_producto(self.plaga2)
        self.factura.agregar_producto(self.fertilizante1)
        self.assertEqual(self.factura.valor_total, 120.0)

   


if __name__ == '__main__':
    unittest.main()
