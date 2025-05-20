import unittest
from calculadora import suma

class TestCalculadora(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(0, 0), 0)
        
    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -1), -2)
    def test_suma_mixtos(self):
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(1, -1), 0)
        
if __name__ == '__main__':
    unittest.main()