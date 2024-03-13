class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        representation = f"{self.imaginary}j"
        if self.real != 0:
            representation = (
                f"({self.real}{'+' if self.imaginary >= 0 else ''}{representation})"
            )
        return representation

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        denom = other.real**2 + other.imaginary**2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denom
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denom
        return ComplexNumber(real, imaginary)
