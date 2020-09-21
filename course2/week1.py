import unittest


# def factorize(x):
#     """
#     Factorize positive integer and return its factors.
#     :type x: int,>=0
#     :rtype: tuple[N],N>0
#     """
#     return True


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        self.cases = ("string", 1.5)
        for c in self.cases:
            with self.subTest(x=c):
                self.assertRaises(TypeError, factorize, c)

    def test_negative(self):
        self.cases = (-1, -10, -100)
        for c in self.cases:
            with self.subTest(x=c):
                self.assertRaises(ValueError, factorize, c)

    def test_zero_and_one_cases(self):
        self.cases = (0, 1)
        for c in self.cases:
            with self.subTest(x=c):
                self.assertEqual(factorize(c), (c,))

    def test_simple_numbers(self):
        self.cases = (3, 13, 29)
        for c in self.cases:
            with self.subTest(x=c):
                self.assertEqual(factorize(c), (c,))

    def test_two_simple_multipliers(self):
        self.cases = (6, 26, 121)
        self.answers = [(2, 3), (2, 13), (11, 11)]
        for c in self.cases:
            with self.subTest(x=c):
                self.assertIn(factorize(c), self.answers)
                # self.assertEqual(len(factorize(c)), 2)

    def test_many_multipliers(self):
        # self.cases = (1001, 9699690)
        with self.subTest(x=1001):
            self.assertEqual(factorize(1001), (7, 11, 13))
        with self.subTest(x=9699690):
            self.assertEqual(factorize(9699690), (2, 3, 5, 7, 11, 13, 17, 19))
        # self.assertEqual(factorize(c))
        # for c in self.cases:
        #     with self.subTest(x=c):
        #         self.assertGreater(len(factorize(c)), 2)


# if __name__ == '__main__':
#     unittest.main()
