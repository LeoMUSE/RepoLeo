import unittest
from App.multi import multiplicacion

class TestMulti(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(multiplicacion(2,3), 6)

if __name__ == "__main__":
    unittest.main()