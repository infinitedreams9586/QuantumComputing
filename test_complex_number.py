from unittest import TestCase

from complex_number import ComplexNumber


class TestComplexNumber(TestCase):
    def test__mathematical_operations(self):
        c1 = ComplexNumber(3, 2)
        c2 = ComplexNumber(-1, -1)

        self.assertEqual("2+i", (c1+c2).to_string())
        self.assertEqual("4+3i", (c1-c2).to_string())
        self.assertEqual("-1-5i", (c1*c2).to_string())
        self.assertEqual("-2.5+0.5i", (c1/c2).to_string())
        self.assertEqual(3.605551275463989, c1.modulus())
        self.assertEqual(1.4142135623730951, c2.modulus())
        self.assertEqual("13", c1.conjugate().to_string())
        self.assertEqual("2", c2.conjugate().to_string())
