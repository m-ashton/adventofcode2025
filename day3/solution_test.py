import unittest
import solution

class SolutionTest(unittest.TestCase):
    def test_max_joltage(self):
        self.assertEqual(solution.max_joltage('123954812'), 98)

    def test_max_joltage_most_sig_dig_is_last(self):
        self.assertEqual(solution.max_joltage('123459'), 59)

if __name__ == '__main__':
    unittest.main()