# test_app.py
import unittest
from app import soma, subtrai, multiplica, divide, potencia

class TestApp(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(1, 2), 3)
        self.assertEqual(soma(-1, 1), 0)

    def test_subtrai(self):
        self.assertEqual(subtrai(2, 1), 1)
        self.assertEqual(subtrai(1, 1), 0)

    def test_multiplica(self):
        self.assertEqual(multiplica(3, 4), 12)
        self.assertEqual(multiplica(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)

if __name__ == '__main__':
    unittest.main()
