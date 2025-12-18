import unittest
import solution

class SolutionTest(unittest.TestCase):
    def test_is_valid(self):
        self.assertFalse(solution.is_valid(1010))
        self.assertTrue(solution.is_valid(101))
        self.assertTrue(solution.is_valid(1110))

if __name__ == '__main__':
    unittest.main()