"""Headless tests for the calculator logic in main.py.

Importing main must not open a window: the build sits under the
main guard, so these tests run on a machine with no display.
They cover calculate_result() and format_number() only. The
window itself is not run here.
"""
import unittest

import main


class CalculateResultTests(unittest.TestCase):
    def test_whole_numbers(self):
        self.assertEqual(main.calculate_result("5", "3"), "Area: 15, Perimeter: 16")

    def test_decimals(self):
        self.assertEqual(main.calculate_result("2.5", "4"), "Area: 10, Perimeter: 13")

    def test_padded_input(self):
        self.assertEqual(main.calculate_result(" 5 ", " 3 "), "Area: 15, Perimeter: 16")

    def test_exponent_input(self):
        self.assertEqual(main.calculate_result("1e3", "2"), "Area: 2000, Perimeter: 2004")

    def test_zero_side(self):
        self.assertEqual(main.calculate_result("0", "5"), "Area: 0, Perimeter: 10")

    def test_empty_and_text_input(self):
        for bad in ("", "abc"):
            self.assertEqual(main.calculate_result(bad, "3"), "Please enter two numbers")
            self.assertEqual(main.calculate_result("3", bad), "Please enter two numbers")

    def test_non_finite_input_is_rejected(self):
        # Pinned: float() accepts these, and the first version
        # printed "Area: inf" and "Area: nan" as results.
        for bad in ("inf", "-inf", "nan", "1e999"):
            self.assertEqual(main.calculate_result(bad, "2"), "Please enter two numbers")

    def test_negative_side_is_rejected(self):
        self.assertEqual(
            main.calculate_result("-5", "3"), "Base and height cannot be negative"
        )
        self.assertEqual(
            main.calculate_result("5", "-3"), "Base and height cannot be negative"
        )

    def test_large_product_keeps_all_digits(self):
        # Pinned: %g printed this area as 9.44977e+12.
        self.assertEqual(
            main.calculate_result("1234567", "7654321"),
            "Area: 9449772114007, Perimeter: 17777776",
        )

    def test_float_noise_is_trimmed(self):
        self.assertEqual(
            main.calculate_result("0.1", "0.2"), "Area: 0.02, Perimeter: 0.6"
        )


class FormatNumberTests(unittest.TestCase):
    def test_integers_have_no_decimal_tail(self):
        self.assertEqual(main.format_number(15.0), "15")
        self.assertEqual(main.format_number(0.0), "0")

    def test_decimals_keep_their_digits(self):
        self.assertEqual(main.format_number(2.5), "2.5")
        self.assertEqual(main.format_number(0.02), "0.02")


if __name__ == "__main__":
    unittest.main()
