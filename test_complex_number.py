from unittest import TestCase

from complex_number import ComplexNumber


class TestComplexNumber(TestCase):
    def setUp(self):
        self.cn1 = ComplexNumber(3, 2)
        self.cn2 = ComplexNumber(-1, -1)

    def test__mathematical_operations(self):
        c1 = self.cn1
        c2 = self.cn2

        self.assertEqual("2+i", (c1+c2).to_string())
        self.assertEqual("4+3i", (c1-c2).to_string())
        self.assertEqual("-1-5i", (c1*c2).to_string())
        self.assertEqual("-2.5+0.5i", (c1/c2).to_string())
        self.assertEqual(3.605551275463989, c1.modulus())
        self.assertEqual(1.4142135623730951, c2.modulus())
        self.assertEqual("3-2i", c1.conjugate().to_string())
        self.assertEqual("-1+i", c2.conjugate().to_string())
    
    def test__edge_case_for_mathematical_operations(self):
        c1 = ComplexNumber(0, 0)
        c2 = ComplexNumber(0, 0)
        
        self.assertEqual("0", (c1+c2).to_string())
        self.assertEqual("0", (c1-c2).to_string())
        self.assertEqual("0", (c1*c2).to_string())
        self.assertEqual(None, (c1/c2))
        self.assertEqual(0, c1.modulus())
        self.assertEqual(0, c2.modulus())
        self.assertEqual("0", c1.conjugate().to_string())
        self.assertEqual("0", c2.conjugate().to_string())
    
    def test__get_length(self):
        c1 = ComplexNumber(3, 4)
        c2 = ComplexNumber(1, 1)
        self.assertEquals(5.0, c1.get_length())
        self.assertEquals(1.4142135623730951, c2.get_length())

    def test__get_angle(self):
        c1 = ComplexNumber(1, 1)
        self.assertEquals(45.0, c1.get_degree())