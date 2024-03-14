import math
from typing import Union


class ComplexNumber:
    """
    Represents a complex number with a real and imaginary part.

    :param real: The real part of the complex number.
    :type real: float
    :param imaginary: The imaginary part of the complex number.
    :type imaginary: float
    """

    def __init__(self, real: float = 0.0, imaginary: float = 0.0) -> None:
        self.real = real
        self.imaginary = imaginary

    def __repr__(self) -> str:
        """
        Constructs a representation of a complex number in cartesian format.

        :return: The complex number in the format 'real + imaginaryj'.
        :rtype: str
        """
        if self.imaginary == 0:
            return f"{self.real}"
        elif self.real == 0:
            return f"{self.imaginary}j"
        else:
            return f"({self.real}{'+' if self.imaginary >= 0 else ''}{self.imaginary}j)"

    def __add__(self, other: Union[int, float, "ComplexNumber"]) -> "ComplexNumber":
        """
        Adds a real or complex number to this complex number.

        :param other: The other complex or real number to add.
        :type other: Union[int, float, ComplexNumber]
        :return: The result of the addition.
        :rtype: ComplexNumber
        """
        if isinstance(other, ComplexNumber):
            real = self.real + other.real
            imaginary = self.imaginary + other.imaginary
        elif isinstance(other, (int, float)):
            real = self.real + other
            imaginary = self.imaginary
        else:
            return NotImplemented
        return ComplexNumber(real, imaginary)

    def __radd__(self, other: Union[int, float, "ComplexNumber"]) -> "ComplexNumber":
        """
        Adds this complex number to a real or complex number.

        :param other: The other complex or real number to add.
        :type other: Union[int, float, ComplexNumber]
        :return: The result of the addition.
        :rtype: ComplexNumber
        """
        return self.__add__(other)

    def __sub__(self, other: Union[int, float, "ComplexNumber"]) -> "ComplexNumber":
        """
        Subtracts a real or complex number from this complex number.

        :param other: The other complex or real number to subtract.
        :type other: Union[int, float, ComplexNumber]
        :return: The result of the subtraction.
        :rtype: ComplexNumber
        """
        if isinstance(other, ComplexNumber):
            real = self.real - other.real
            imaginary = self.imaginary - other.imaginary
        elif isinstance(other, (int, float)):
            real = self.real - other
            imaginary = self.imaginary
        else:
            return NotImplemented
        return ComplexNumber(real, imaginary)

    def __rsub__(self, other: Union[int, float, "ComplexNumber"]) -> "ComplexNumber":
        """
        Subtracts this complex number from a real or complex number.

        :param other: The real or complex number from which to subtract.
        :type other: Union[int, float, ComplexNumber]
        :return: The result of the subtraction.
        :rtype: ComplexNumber
        """
        if isinstance(other, (int, float)):
            # Create a temporary ComplexNumber from other to perform subtraction
            return ComplexNumber(real=other - self.real, imaginary=-self.imaginary)
        else:
            return NotImplemented

    def __mul__(self, other: Union[int, float, "ComplexNumber"]) -> "ComplexNumber":
        """
        Multiplies this complex number with a real or complex number.

        :param other: The other complex or real number to multiply.
        :type other: Union[int, float, ComplexNumber]
        :return: The result of the multiplication.
        :rtype: ComplexNumber
        """
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imaginary * other.imaginary
            imaginary = self.imaginary * other.real + self.real * other.imaginary
        elif isinstance(other, (int, float)):
            real = self.real * other
            imaginary = self.imaginary * other
        else:
            return NotImplemented
        return ComplexNumber(real, imaginary)

    def __rmul__(self, other: Union[int, float, "ComplexNumber"]) -> "ComplexNumber":
        """
        Multiplies this complex number with a real or complex number.

        :param other: The other complex or real number to multiply.
        :type other: Union[int, float, ComplexNumber]
        :return: The result of the multiplication.
        :rtype: ComplexNumber
        """
        return self.__mul__(other)

    def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
        """
        Divides this complex number by a real or complex number.

        :param other: The other complex or real number to divide by.
        :type other: ComplexNumber or float
        :return: The result of the division.
        :rtype: ComplexNumber
        :raises ZeroDivisionError: If attempting to divide by a complex or real number
        with magnitude zero.
        """
        if isinstance(other, ComplexNumber):
            denom = other.real**2 + other.imaginary**2
            if denom == 0:
                raise ZeroDivisionError("Attempt to divide by zero magnitude")
            real = (self.real * other.real + self.imaginary * other.imaginary) / denom
            imaginary = (
                self.imaginary * other.real - self.real * other.imaginary
            ) / denom
        elif isinstance(other, (int, float)):
            denom = other**2
            if denom == 0:
                raise ZeroDivisionError("Attempt to divide by zero")
            real = self.real * other / denom
            imaginary = self.imaginary * other / denom
        else:
            return NotImplemented
        return ComplexNumber(real, imaginary)

    def __rtruediv__(
        self, other: Union[int, float, "ComplexNumber"]
    ) -> "ComplexNumber":
        """
        Divides a real or complex number by this complex number.

        :param other: The real or complex number to be divided by this complex number.
        :type other: Union[int, float, ComplexNumber]
        :return: The result of the division.
        :rtype: ComplexNumber
        """
        if isinstance(other, (int, float)):
            # Convert the real number to a ComplexNumber for division
            other = ComplexNumber(real=other, imaginary=0)
            return other.__truediv__(self)
        else:
            return NotImplemented

    def __pow__(self, exponent: Union[int, float]) -> "ComplexNumber":
        """
        Raises the complex number to the power of 'exponent'.

        :param exponent: The exponent to raise the complex number to.
        :type exponent: Union[int, float]
        :return: The complex number raised to the specified power.
        :rtype: ComplexNumber
        """
        if isinstance(exponent, (int, float)):
            if self.real == self.imaginary == 0 and exponent < 0:
                raise ZeroDivisionError("0 cannot be raised to a negative power")
            magnitude, angle = self.to_polar()
            magnitude **= exponent
            angle *= exponent
            return ComplexNumber.from_polar(magnitude, angle)
        else:
            # TODO: Implement exponentiation with complex number as exponent
            return NotImplemented

    def __rpow__(self, base: Union[int, float]) -> "ComplexNumber":
        """
        Raises a real number to the power of this complex number.

        :param exponent: The exponent to raise the complex number to.
        :type base: Union[int, float]
        :return: The complex number raised to the specified power.
        :rtype: ComplexNumber
        """
        if isinstance(base, (int, float)) and base <= 0:
            log_base = math.log(base)
            magnitude, angle = self.to_polar()
            result_magnitude = math.exp(log_base * magnitude * math.cos(angle))
            result_angle = log_base * magnitude * math.sin(angle)
            return ComplexNumber.from_polar(result_magnitude, result_angle)
        else:
            return NotImplemented

    def __eq__(self, other: Union[int, float, "ComplexNumber"]) -> bool:
        """
        Checks if two complex numbers are equal.

        :param other: The complex number to compare with.
        :type other: ComplexNumber
        :return: True if the real and imaginary parts of both complex numbers are equal,
        False otherwise.
        :rtype: bool
        """
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        elif isinstance(other, (int, float)):
            return self.real == other and self.imaginary == 0
        else:
            return False

    def sqrt(self) -> "ComplexNumber":
        """
        Calculates the square root of the complex number.

        :return: The square root of the complex number as a new ComplexNumber instance.
        :rtype: ComplexNumber
        """
        return self.__pow__(0.5)

    def conjugate(self) -> "ComplexNumber":
        """
        Returns the conjugate of the complex number.

        The conjugate of a complex number is obtained by changing the sign of its
        imaginary part.

        :return: The conjugate of the complex number as a new ComplexNumber instance.
        :rtype: ComplexNumber
        """
        return ComplexNumber(self.real, -self.imaginary)

    def modulus(self) -> float:
        """
        Returns the modulus (absolute value) of the complex number.

        The modulus is the distance from the origin to the point represented by the
        complex number in the complex plane, calculated as sqrt(a^2 + b^2).

        :return: The modulus of the complex number.
        :rtype: float
        """
        return (self.real**2 + self.imaginary**2) ** 0.5

    def argument(self) -> float:
        """
        Returns the argument (phase) of the complex number in radians.

        The argument is the angle in radians between the positive real axis and the line
        representing the complex number in the complex plane.

        :return: The argument of the complex number in radians.
        :rtype: float
        """
        return math.atan2(self.imaginary, self.real)

    def to_polar(self) -> tuple[float, float]:
        """
        Returns the polar form representation of the complex number.

        The polar form is a tuple containing the magnitude (modulus) and the phase
        (argument) of the complex number.

        :return: A tuple (magnitude, phase) representing the polar form of the complex
        number.
        :rtype: tuple[float, float]
        """
        return (self.modulus(), self.argument())

    @classmethod
    def from_polar(cls, magnitude: float, angle: float) -> "ComplexNumber":
        """
        Creates a ComplexNumber instance from polar coordinates.

        :param magnitude: The magnitude of the complex number. Must be non-negative.
        :type magnitude: float
        :param angle: The angle (in radians) of the complex number.
        :type angle: float
        :return: A new ComplexNumber instance based on the given polar coordinates.
        :rtype: ComplexNumber
        """
        if magnitude < 0:
            raise ValueError("Magnitude must be non-negative.")
        real = magnitude * math.cos(angle)
        imaginary = magnitude * math.sin(angle)
        return cls(real, imaginary)
