import unittest
import solution

class SolutionTest(unittest.TestCase):
    def test_adjacent_positions(self):
        self.assertEqual(
            sorted(solution.adjacent_positions(0, 0)),
            sorted([(0,1), (1,0), (1,1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1) ])
        )


if __name__ == '__main__':
    unittest.main()