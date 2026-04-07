import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):
    def test_basic_stats(self):
        engine = StatEngine([10, 20, 30])
        self.assertEqual(engine.get_mean(), 20.0)
        self.assertEqual(engine.get_median(), 20.0)

    def test_outliers(self):
        engine = StatEngine([1, 1, 1, 1, 1, 100])
        self.assertIn(100, engine.get_outliers(threshold=1))

if __name__ == "__main__":
    unittest.main()
