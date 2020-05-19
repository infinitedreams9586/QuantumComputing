import math

class ComplexNumber(object):
    def __init__(self, real=None, imaginary=None, modulus=None, angle_degree=None):
        if ((real != None) and (imaginary != None)):
            self.real_component = int(real) if isinstance(real, int) else float(real)
            self.imaginary_component = int(imaginary) if isinstance(imaginary, int) else float(imaginary)
        if ((modulus != None) and (angle_degree != None)):
            if not angle_degree in range(0, 361) and not isinstance(modulus, float):
                return None
            self.real_component = modulus * math.sin(math.radians(angle_degree))
            self.imaginary_component = modulus * math.cos(math.radians(angle_degree))

    def __repr__(self):
        return "{real}{sign}{imaginary}{i}".format(real=self.real_component,
                                                 sign='+' if self.imaginary_component > 0 else '',
                                                 imaginary= '' if self.imaginary_component in [0, 1] else self.imaginary_component,
                                                 i = 'i' if self.imaginary_component != 0 else '')

    def __add__(self, other):
        if not self._is_complex_number(other):
            return
        real_add = self.real_component + other.real_component
        imaginary_add = self.imaginary_component + other.imaginary_component
        return ComplexNumber(real_add, imaginary_add)

    def __sub__(self, other):
        if not self._is_complex_number(other):
            return
        real_sub = self.real_component - other.real_component
        imaginary_sub = self.imaginary_component - other.imaginary_component
        return ComplexNumber(real_sub, imaginary_sub)

    def __mul__(self, other):
        if not self._is_complex_number(other):
            return
        # self: (a1, b1) where a is real component, and b is imaginary component
        # other: (a2, b2) where a is real component, and b is imaginary component
        a1a2 = self.real_component * other.real_component
        b1b2 = self.imaginary_component * other.imaginary_component
        a1b2 = self.real_component * other.imaginary_component
        a2b1 = self.imaginary_component * other.real_component

        return ComplexNumber(a1a2 - b1b2, a1b2 + a2b1)

    def __truediv__(self, other):
        if not self._is_complex_number(other):
            return
        if self.real_component == 0 and self.imaginary_component == 0:
            return None

        # self: (a1, b1) where a is real component, and b is imaginary component
        # other: (a2, b2) where a is real component, and b is imaginary component
        a1a2 = self.real_component * other.real_component
        b1b2 = self.imaginary_component * other.imaginary_component
        a1b2 = self.real_component * other.imaginary_component
        a2b1 = self.imaginary_component * other.real_component
        a2_squared = other.real_component ** 2
        b2_squared = other.imaginary_component ** 2
        
        return ComplexNumber((a1a2 + b1b2) / (a2_squared + b2_squared), (a2b1 - a1b2) / (a2_squared + b2_squared))

    def modulus(self):
        return math.sqrt(self.real_component ** 2 + self.imaginary_component ** 2)

    def conjugate(self):
        return ComplexNumber(self.real_component, (-1) * self.imaginary_component)

    def _is_complex_number(self, other):
        if not isinstance(other, ComplexNumber):
            print("Invalid complex number.")
            return False
        return True
    
    def get_degree(self):
        return math.degrees(self.get_radian())
    
    def get_radian(self):
        if self.real_component == 0:
            return None
        return math.atan(self.imaginary_component/self.real_component)
    
    def get_length(self):
        return self.modulus()

    def to_string(self):
        return str(self)

    def get_polar_representation(self, rounded=False):
        r = (self.modulus(), self.get_radian())
        def rounding():
            return tuple(map(lambda x: round(x, 2), r))
        if not rounded:
            return r
        return rounding()

    def get_cartesian_representation(self, rounded=False):
        r = (self.real_component, self.imaginary_component)
        def rounding():
            return tuple(map(lambda x: round(x, 2), r))
        if not rounded:
            return r
        return rounding()


class ComplexNumberPolar(ComplexNumber):
    def __init__(self, modulus, angle_degree):
        super(ComplexNumberPolar, self).__init__(real=None, imaginary=None, modulus=modulus, angle_degree=angle_degree)


class ComplexNumberCartesian(ComplexNumber):
    def __init__(self, real, imaginary):
        super(ComplexNumberCartesian, self).__init__(real=real, imaginary=imaginary, modulus=None, angle_degree=None)