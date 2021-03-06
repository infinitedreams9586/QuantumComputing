from unittest import TestCase

from complex_number import ComplexNumber, ComplexNumberPolar, ComplexNumberCartesian


class TestComplexNumber(TestCase):
    def setUp(self):
        self.cn1 = ComplexNumberCartesian(3, 2)
        self.cn2 = ComplexNumberCartesian(-1, -1)

    def test__compare_cartesian_and_polar(self):
        cartesian = ComplexNumberCartesian(1, 1)
        polar = ComplexNumberPolar(1.41, 45)
        self.assertEqual(cartesian.real_component, round(polar.real_component, 1))
        self.assertEqual(cartesian.imaginary_component, round(polar.imaginary_component, 1))

    def test__mathematical_operations(self):
        c1 = self.cn1
        c2 = self.cn2

        self.assertEqual("2+i", (c1+c2).to_string())
        self.assertEqual("4+3i", (c1-c2).to_string())
        self.assertEqual("-1-5i", (c1*c2).to_string())
        self.assertEqual("-2.5+0.5i", (c1/c2).to_string())
        self.assertEqual(3.605551275463989, c1.modulus())
        self.assertEqual(1.4142135623730951, c2.modulus())
        self.assertEqual(3.61, c1.modulus(rounded=True))
        self.assertEqual(1.41, c2.modulus(rounded=True))
        self.assertEqual("3-2i", c1.conjugate().to_string())
        self.assertEqual("-1+i", c2.conjugate().to_string())
    
    def test__edge_case_for_mathematical_operations(self):
        c1 = ComplexNumberCartesian(0, 0)
        c2 = ComplexNumberCartesian(0, 0)
        
        self.assertEqual("0", (c1+c2).to_string())
        self.assertEqual("0", (c1-c2).to_string())
        self.assertEqual("0", (c1*c2).to_string())
        self.assertEqual(None, (c1/c2))
        self.assertEqual(0, c1.modulus())
        self.assertEqual(0, c2.modulus())
        self.assertEqual("0", c1.conjugate().to_string())
        self.assertEqual("0", c2.conjugate().to_string())
    
    def test__get_magnitude(self):
        c1 = ComplexNumberCartesian(3, 4)
        c2 = ComplexNumberCartesian(1, 1)
        self.assertEqual(5.0, c1.get_magnitude())
        self.assertEqual(1.4142135623730951, c2.get_magnitude())
        self.assertEqual(1.41, c2.get_magnitude(rounded=True))

    def test__get_phase(self):
        c1 = ComplexNumberCartesian(1, 1)
        self.assertEqual(45.0, c1.get_phase(in_degree=True))
        self.assertEqual(0.79, c1.get_phase(rounded=True))
    
    def test__should_interchange_representations(self):
        c1 = ComplexNumberPolar(2, 45)
        self.assertEqual((1.41, 1.41), c1.get_cartesian_representation(rounded=True))
        c2 = ComplexNumberCartesian(1.41, 1.41)
        self.assertEqual((1.99, 0.79), c2.get_polar_representation(rounded=True))
        self.assertEqual((1.99, 45.0), c2.get_polar_representation(rounded=True, in_degrees=True))

    def test__get_cartesian_representation(self):
        c1 = ComplexNumber(1, 1)
        self.assertEqual((1, 1), c1.get_cartesian_representation())
        c2 = ComplexNumber(real=None, imaginary=None, modulus=1.41, angle_degree=45)
        self.assertEqual((1, 1), c2.get_cartesian_representation(rounded=True))

    def test__get_polar_representation(self):
        c1 = ComplexNumber(1, 1)
        self.assertEqual((1.41, 0.79), c1.get_polar_representation(rounded=True))
        c2 = ComplexNumber(real=None, imaginary=None, modulus=1.41, angle_degree=45)
        self.assertEqual((1.41, 0.79), c2.get_polar_representation(rounded=True))