# Complex Number Implementation

The `ComplexNumber` class represents a complex number with real and imaginary parts,
offering a range of operations for complex number arithmetic.

## Features

- Representation of complex numbers in Cartesian format.
- Arithmetic operations: addition, subtraction, multiplication, division, and exponentiation.
- Utility methods: square root, conjugation, modulus (absolute value), argument (phase angle), and conversions between polar and cartesian forms.

## Installation

To use the `ComplexNumber` class, include the `complex_number.py` file in your project and import it as needed.

```python
from complex_number import ComplexNumber
```

## Usage

### Initialization

```python
# Initialize a complex number with real and imaginary parts
z = ComplexNumber(3, 4)
```

### Operations

#### Addition

Adds two complex numbers, or a complex number and a real number.

```python
z1 = ComplexNumber(1, 2)
z2 = ComplexNumber(3, 4)
result = z1 + z2
```

Mathematically: $(a + bi) + (c + di) = (a+c) + (b+d)i$

#### Subtraction

Subtracts two complex numbers, or a complex number and a real number.

```python
result = z1 - z2
```

Mathematically: $(a + bi) - (c + di) = (a-c) + (b-d)i$

#### Multiplication

Multiplies two complex numbers, or a complex number and a real number.

```python
result = z1 * z2
```

Mathematically: $(a + bi) \cdot (c + di) = (ac-bd) + (ad+bc)i$

#### Division

Divides two complex numbers, or a complex number by a real number.

```python
result = z1 / z2
```

Mathematically: $\frac{a + bi}{c + di} = \frac{ac+bd}{c^2+d^2} + \frac{bc-ad}{c^2+d^2}i$, assuming $c^2 + d^2 \neq 0$

#### Exponentiation

Raises a complex number to the power of a real number. Complex exponents are not implemented.

```python
result = z1 ** 2
```

Mathematically: $r(\cos(\theta) + i\sin(\theta)))^n = r^n(\cos(n\theta) + i\sin(n\theta))$, where $r$ is the modulus and $\theta$ is the argument of the complex number.

### Utility Methods

#### Square Root

Calculates the square root of a complex number.

```python
result = z1.sqrt()
```

#### Conjugate

Returns the conjugate of a complex number.

```python
result = z1.conjugate()
```

Mathematically: If $z = a + bi$, then $\bar{z} = a - bi$

#### Modulus

Calculates the modulus (absolute value) of a complex number.

```python
result = z1.modulus()
```

Mathematically: $|a + bi| = \sqrt{a^2 + b^2}$

#### Argument

Returns the argument (phase angle) of a complex number in radians.

```python
result = z1.argument()
```

Mathematically: $\theta = \tan^{-1}(\frac{b}{a})$

#### Polar Conversion

Converts a complex number to its polar form (magnitude and phase).

```python
result = z1.to_polar()
```

### Class Methods

#### From Polar

Creates a complex number instance from polar coordinates.

```python
z = ComplexNumber.from_polar(magnitude, angle)
```

## Tests

Comprehensive tests covering arithmetic operations, utility methods, and special cases are included in the `tests` directory. Ensure to run these tests to validate functionality.
