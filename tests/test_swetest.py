import unittest
from swetest.swetest import Swetest


class TestUtils(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(Swetest.set_path("../ephemeris/"), Swetest.get_path())
        self.assertEqual(Swetest.set_query("-h"), Swetest.get_output())
