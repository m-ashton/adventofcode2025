import unittest
import solution

class SolutionTest(unittest.TestCase):
    def test_max_joltage(self):
        self.assertEqual(solution.max_joltage('123954812'), 98)

    def test_max_joltage_most_sig_dig_is_last(self):
        self.assertEqual(solution.max_joltage('123459'), 59)

    def test_max_joltage_sample_values(self):
        self.assertEqual(solution.max_joltage('987654321111111'), 98)
        self.assertEqual(solution.max_joltage('811111111111119'), 89)
        self.assertEqual(solution.max_joltage('234234234234278'), 78)
        self.assertEqual(solution.max_joltage('818181911112111'), 92)

    def test_max_joltage_with_higher_lengths(self):
        self.assertEqual(solution.max_joltage('987654321111111', 12), 987654321111)
        self.assertEqual(solution.max_joltage('811111111111119', 12), 811111111119)
        self.assertEqual(solution.max_joltage('234234234234278', 12), 434234234278)
        self.assertEqual(solution.max_joltage('818181911112111', 12), 888911112111)

if __name__ == '__main__':
    unittest.main()