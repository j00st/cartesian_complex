import unittest
import logging
import operator
import cmath
from parameterized import parameterized

from complex_number.complex_number import ComplexNumber

# Configure logging
logging.basicConfig(level=logging.DEBUG)

complex_test_numbers = [
    (0, 0),  # Origin complex number
    (1, 0),  # Pure real complex number
    (0, 1),  # Pure imaginary complex number
    (-1, 0),  # Negative real complex number
    (0, -1),  # Negative imaginary complex number
    (3, 4),  # Arbitrary positive complex number
    (-3, -4),  # Arbitrary negative complex number
    (1e-3, -1e-3),  # Small magnitude complex number
]

real_test_numbers = [
    0,  # Zero
    3,  # Arbitrary positive number
    -3,  # Arbitrary negative number
    1e-3,  # Small magnitude number
]

test_representations = [
    (0, 0, "0"),
    (1, 0, "1"),
    (0, 1, "1j"),
    (-1, 0, "-1"),
    (0, -1, "-1j"),
    (1, 1, "(1+1j)"),
    (-1, -1, "(-1-1j)"),
    (1, -1, "(1-1j)"),
    (-1, 1, "(-1+1j)"),
    (3.5, -2.5, "(3.5-2.5j)"),
]

# Mapping of operation names to their corresponding operator functions
operations = {
    "addition": operator.add,
    "subtraction": operator.sub,
    "multiplication": operator.mul,
    "division": operator.truediv,
    "exponentiation": operator.pow,
}


class TestComplexNumber(unittest.TestCase):

    @parameterized.expand(
        [
            (op_name, op_func, lhs, rhs)
            for op_name, op_func in operations.items()
            for lhs in complex_test_numbers + real_test_numbers
            for rhs in complex_test_numbers + real_test_numbers
            if not (isinstance(lhs, (int, float)) and isinstance(rhs, (int, float)))
        ]
    )
    def test_operations(self, op_name, op_func, lhs, rhs):
        if op_name == "exponentiation" and isinstance(rhs, tuple):
            # TODO: Remove skip when exponentiation by ComplexNumber is implemented
            self.skipTest(
                reason="Exponentiation with ComplexNumber as exponent not implemented"
            )
        with self.subTest(op_name=op_name, lhs=lhs, rhs=rhs):
            logging.debug(f"Testing operation {lhs} {op_name} {rhs}")
            test_lhs = ComplexNumber(*lhs) if type(lhs) == tuple else lhs
            test_rhs = ComplexNumber(*rhs) if type(rhs) == tuple else rhs
            expected_lhs = complex(*lhs) if type(lhs) == tuple else lhs
            expected_rhs = complex(*rhs) if type(rhs) == tuple else rhs
            if op_name == "division" and rhs in ((0, 0), 0):
                with self.assertRaises(ZeroDivisionError):
                    op_func(test_lhs, test_rhs)
            elif op_name == "exponentiation" and lhs == (0, 0) and rhs < 0:
                with self.assertRaises(ZeroDivisionError):
                    op_func(test_lhs, test_rhs)
            else:
                test_result = op_func(test_lhs, test_rhs)
                expected_result = op_func(expected_lhs, expected_rhs)
                self.assertEqual(type(test_result), ComplexNumber)
                self.assertEqual(type(expected_result), complex)
                self.assertAlmostEqual(test_result.real, expected_result.real)
                self.assertAlmostEqual(
                    test_result.imaginary, expected_result.imag, delta=1e-5
                )

    @parameterized.expand(
        [
            (lhs, rhs)
            for lhs in complex_test_numbers + real_test_numbers
            for rhs in complex_test_numbers + real_test_numbers
            if not (isinstance(lhs, (int, float)) and isinstance(rhs, (int, float)))
        ]
    )
    def test_equal(self, lhs, rhs):
        with self.subTest(lhs=lhs, rhs=rhs):
            test_lhs = ComplexNumber(*lhs) if type(lhs) == tuple else lhs
            test_rhs = ComplexNumber(*rhs) if type(rhs) == tuple else rhs
            expected_lhs = complex(*lhs) if type(lhs) == tuple else lhs
            expected_rhs = complex(*rhs) if type(rhs) == tuple else rhs
            expected_result = expected_lhs == expected_rhs
            actual_result = test_lhs == test_rhs
            logging.debug(f"Testing {test_lhs} == {test_rhs} = {actual_result}")
            self.assertEqual(actual_result, expected_result)

    @parameterized.expand(test_representations)
    def test_repr(self, real, imaginary, expected):
        test_instance = ComplexNumber(real, imaginary)
        test_str = repr(test_instance)
        logging.debug(f"Testing repr {test_str} == {expected}")
        self.assertEqual(test_str, expected)

    @parameterized.expand(complex_test_numbers)
    def test_conjugate(self, real, imaginary):
        complex_number = ComplexNumber(real, imaginary)
        conjugate_number = complex_number.conjugate()

        self.assertEqual(conjugate_number.real, real)
        self.assertEqual(conjugate_number.imaginary, -imaginary)

        expected_conjugate = complex(real, imaginary).conjugate()
        logging.debug(f"Testing conjugate {conjugate_number} == {expected_conjugate}")
        self.assertEqual(conjugate_number.real, expected_conjugate.real)
        self.assertEqual(conjugate_number.imaginary, expected_conjugate.imag)

    @parameterized.expand(complex_test_numbers)
    def test_sqrt(self, real, imaginary):
        complex_number = ComplexNumber(real, imaginary)
        control_number = complex(real, imaginary)
        test_result = complex_number.sqrt()
        expected_result = cmath.sqrt(control_number)
        self.assertAlmostEqual(test_result.real, expected_result.real)
        self.assertAlmostEqual(test_result.imaginary, expected_result.imag)

    @parameterized.expand(complex_test_numbers)
    def test_modulus(self, real, imaginary):
        complex_number = ComplexNumber(real, imaginary)
        control_number = complex(real, imaginary)
        test_result = complex_number.modulus()
        expected_result = abs(control_number)
        self.assertEqual(test_result, expected_result)

    @parameterized.expand(complex_test_numbers)
    def test_argument(self, real, imaginary):
        complex_number = ComplexNumber(real, imaginary)
        control_number = complex(real, imaginary)
        test_result = complex_number.argument()
        expected_result = cmath.phase(control_number)
        self.assertEqual(test_result, expected_result)

    @parameterized.expand(complex_test_numbers)
    def test_to_polar(self, real, imaginary):
        complex_number = ComplexNumber(real, imaginary)
        control_number = complex(real, imaginary)
        test_result = complex_number.to_polar()
        expected_result = cmath.polar(control_number)
        self.assertAlmostEqual(test_result[0], expected_result[0])
        self.assertAlmostEqual(test_result[1], expected_result[1])

    @parameterized.expand(
        [
            (magnitude, angle)
            for magnitude, angle in complex_test_numbers  # Re-using the tuple
            if magnitude >= 0
        ]
    )
    def test_from_polar(self, magnitude, angle):
        complex_number = ComplexNumber.from_polar(magnitude, angle)
        control_number = cmath.rect(magnitude, angle)
        self.assertAlmostEqual(complex_number.real, control_number.real)
        self.assertAlmostEqual(complex_number.imaginary, control_number.imag)
