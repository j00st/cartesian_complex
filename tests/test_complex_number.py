import unittest
import logging
import operator
from parameterized import parameterized

from complex_number.complex_number import ComplexNumber

# Configure logging
logging.basicConfig(level=logging.DEBUG)

complex_numbers = [
    (0, 0),  # Origin
    (1, 0),  # Pure real
    (0, 1),  # Pure imaginary
    (-1, 0),  # Negative real
    (0, -1),  # Negative imaginary
    (3, 4),  # Arbitrary positive
    (-3, -4),  # Arbitrary negative
    (1e-10, -1e-10),  # Small magnitude
]

representations = [
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
}


class TestComplexNumber(unittest.TestCase):

    @parameterized.expand(
        [
            (op_name, op_func, lhs, rhs)
            for op_name, op_func in operations.items()
            for lhs in complex_numbers
            for rhs in complex_numbers
        ]
    )
    def test_operations(self, op_name, op_func, lhs, rhs):
        with self.subTest(op_name=op_name, lhs=lhs, rhs=rhs):
            logging.debug(f"Testing operation {lhs} {op_name} {rhs}")
            test_lhs = ComplexNumber(*lhs)
            test_rhs = ComplexNumber(*rhs)
            control_lhs = complex(*lhs)
            control_rhs = complex(*rhs)
            if op_name == "division" and rhs == (0, 0):
                with self.assertRaises(ZeroDivisionError):
                    op_func(test_lhs, test_rhs)
            else:
                test_result = op_func(test_lhs, test_rhs)
                control_result = op_func(control_lhs, control_rhs)
                self.assertEqual(type(test_result), ComplexNumber)
                self.assertEqual(type(control_result), complex)
                self.assertEqual(test_result.real, control_result.real)
                self.assertEqual(test_result.imaginary, control_result.imag)

    @parameterized.expand(
        [(lhs, rhs) for lhs in complex_numbers for rhs in complex_numbers]
    )
    def test_equal(self, lhs, rhs):
        with self.subTest(lhs=lhs, rhs=rhs):
            test_lhs = ComplexNumber(*lhs)
            test_rhs = ComplexNumber(*rhs)
            control_lhs = complex(*lhs)
            control_rhs = complex(*rhs)
            expected_result = control_lhs == control_rhs
            actual_result = test_lhs == test_rhs
            logging.debug(f"Testing {test_lhs} == {test_rhs} = {actual_result}")
            self.assertEqual(actual_result, expected_result)

    @parameterized.expand(
        [(real, imaginary, control) for real, imaginary, control in representations]
    )
    def test_repr(self, real, imaginary, control):
        test_instance = ComplexNumber(real, imaginary)
        self.assertEqual(repr(test_instance), control)
