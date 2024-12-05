class TestCalculatorIntegration(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_combined_operations(self):
        # Perform (10 + 5) * 2
        result = self.calc.multiply(self.calc.add(10, 5), 2)
        self.assertEqual(result, 30)

    def test_chained_operations(self):
        # Perform ((10 / 2) - 3) * 4
        division_result = self.calc.divide(10, 2)
        subtraction_result = self.calc.subtract(division_result, 3)
        final_result = self.calc.multiply(subtraction_result, 4)
        self.assertEqual(final_result, 8)