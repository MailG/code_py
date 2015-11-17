
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
        self.assertNotEqual(fun(3), 3)
        self.assertTrue(fun(3) == 4)
        self.assertFalse(fun(3) == 3)
        self.assertIs(fun(3), int)
        self.assertIsNot(fun(3), double)





if __name__ == "__main__":
    unittest.main()
