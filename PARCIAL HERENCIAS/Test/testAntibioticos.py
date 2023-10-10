import unittest
from Modelos.Antibioticos import Antibiotico

class TestAntibiotico(unittest.TestCase):
    def setUp(self):
        self.antibiotico = Antibiotico("Antibiótico 1", "500Kg", "bovinos", 15.0)  # Dosis válida: 500Kg

    def test_tipo_animal_antibiotico(self):
        self.assertEqual(self.antibiotico.validar_tipo_animal("bovinos"), "bovinos")
        self.assertEqual(self.antibiotico.validar_tipo_animal("caprinos"), "caprinos")
        self.assertEqual(self.antibiotico.validar_tipo_animal("porcinos"), "porcinos")
        with self.assertRaises(ValueError):
            self.antibiotico.validar_tipo_animal("otros")

    def test_dosis_antibiotico(self):
        self.assertEqual(self.antibiotico.dosis, "500Kg")
        self.antibiotico.validar_dosis("400Kg")
        self.assertEqual(self.antibiotico.dosis, "400Kg")
        self.antibiotico.validar_dosis("600Kg")
        self.assertEqual(self.antibiotico.dosis, "600Kg")

        # Dosis inválidas
        with self.assertRaises(ValueError):
            self.antibiotico.validar_dosis("300Kg")  # Dosis por debajo del rango
        with self.assertRaises(ValueError):
            self.antibiotico.validar_dosis("700Kg")  # Dosis por encima del rango

if __name__ == '__main__':
    unittest.main()
