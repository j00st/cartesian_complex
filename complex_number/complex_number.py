class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        if self.imaginary == 0:
            return f"{self.real}"
        elif self.real == 0:
            return f"{self.imaginary}j"
        else:
            return f"({self.real}{'+' if self.imaginary >= 0 else ''}{self.imaginary}j)"

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real + other.real
            imaginary = self.imaginary + other.imaginary
        elif isinstance(other, (int, float)):
            real = self.real + other
            imaginary = self.imaginary
        else:
            return NotImplemented
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real - other.real
            imaginary = self.imaginary - other.imaginary
        elif isinstance(other, (int, float)):
            real = self.real - other
            imaginary = self.imaginary
        else:
            return NotImplemented
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imaginary * other.imaginary
            imaginary = self.imaginary * other.real + self.real * other.imaginary
        elif isinstance(other, (int, float)):
            real = self.real * other
            imaginary = self.imaginary * other
        else:
            return NotImplemented
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denom = other.real**2 + other.imaginary**2
            real = (self.real * other.real + self.imaginary * other.imaginary) / denom
            imaginary = (
                self.imaginary * other.real - self.real * other.imaginary
            ) / denom
        elif isinstance(other, (int, float)):
            denom = other**2
            real = self.real * other / denom
            imaginary = self.imaginary * other / denom
        else:
            return NotImplemented
        return ComplexNumber(real, imaginary)
