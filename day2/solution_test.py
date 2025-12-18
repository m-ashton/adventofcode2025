import unittest
import solution

class SolutionTest(unittest.TestCase):
    def test_is_valid_part1(self):
        self.assertFalse(solution.is_valid_part1(1010))
        self.assertTrue(solution.is_valid_part1(101))
        self.assertTrue(solution.is_valid_part1(1110))

    def test_is_valid_part2(self):
        self.assertFalse(solution.is_valid_part2(1010101010))
        self.assertFalse(solution.is_valid_part2(123123123))
        self.assertFalse(solution.is_valid_part2(11))
        self.assertTrue(solution.is_valid_part2(123))

if __name__ == '__main__':
    unittest.main()