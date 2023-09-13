# Bonus Exercise: Create a function that converts a number to its Roman numeral representation.

def to_roman(num):
    # Your code here
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    rm = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            rm += syms[i]
            num -= val[i]
        i += 1
    return rm

    #pass

# Unit tests
import unittest

class TestBonusExercise(unittest.TestCase):

    def test_to_roman(self):
        self.assertEqual(to_roman(58), "LVIII")
        self.assertEqual(to_roman(1994), "MCMXCIV")

if __name__ == '__main__':
    unittest.main()
