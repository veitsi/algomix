import unittest
import add


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(add.add(2, 2), 4,
                         '2+2 is  not 4')


if __name__ == '__main__':
    unittest.main()
