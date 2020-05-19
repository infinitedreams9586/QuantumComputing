import math

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real_component = int(real) if isinstance(real, int) else float(real)
        self.imaginary_component = int(imaginary) if isinstance(imaginary, int) else float(imaginary)

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
