import unittest
import solution

class SolutionTest(unittest.TestCase):
    def test_rotate(self):
        self.assertEqual(solution.rotate(4, -5), (99, 1))
        self.assertEqual(solution.rotate(90, 25), (15, 1))
        self.assertEqual(solution.rotate(50, -68), (82, 1))
        self.assertEqual(solution.rotate(50, 100), (50, 1))
        self.assertEqual(solution.rotate(50, -100), (50, 1))

    def test_multi_rotate(self):
        self.assertEqual(solution.rotate(4, -105), (99, 2))
        self.assertEqual(solution.rotate(90, 225), (15, 3))
        self.assertEqual(solution.rotate(50, -168), (82, 2))
        self.assertEqual(solution.rotate(50, 200), (50, 2))
        self.assertEqual(solution.rotate(50, -200), (50, 2))

    def test_partial_rotation(self):
        self.assertEqual(solution.rotate(50, 25), (75, 0))
        self.assertEqual(solution.rotate(50, -25), (25, 0))

    def test_zero_rotate(self):
        self.assertEqual(solution.rotate(50, 0), (50, 0))
        self.assertEqual(solution.rotate(0, 0), (0, 0))

    def test_starting_at_zero(self):
        self.assertEqual(solution.rotate(0, 100), (0, 1))
        self.assertEqual(solution.rotate(0, 99), (99, 0))
        self.assertEqual(solution.rotate(0, -100), (0, 1))
        self.assertEqual(solution.rotate(0, -99), (1, 0))
        self.assertEqual(solution.rotate(0, 250), (50, 2))
        self.assertEqual(solution.rotate(0, -250), (50, 2))

if __name__ == '__main__':
    unittest.main()