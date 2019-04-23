import unittest
import romanConverter as conv


class TestRomanConverter(unittest.TestCase):
    ##### romanToInt #####
    def testRomanToIntSimple(self):
        result = conv.romanToInt('I')
        self.assertEqual(result, '1')

    def testRomanToIntTwoSymbol(self):
        result = conv.romanToInt('IV')
        self.assertEqual(result, '4')

    def testRomanToIntHard(self):
        result = conv.romanToInt('MMDLXXVII')
        self.assertEqual(result, '2577')

    def testRomanToIntMax(self):
        result = conv.romanToInt('MMMCMXCIX')
        self.assertEqual(result, '3999')

    def testRomanToIntGibberishRaisesError(self):
        with self.assertRaises(ValueError):
            conv.romanToInt('k')


    ##### intToRoman #####
    def testIntToRomanSimple(self):
        result = conv.intToRoman(1)
        self.assertEqual(result, 'I')

    def testIntToRomanTwoSymbol(self):
        result = conv.intToRoman(4)
        self.assertEqual(result, 'IV')

    def testIntToRomanHard(self):
        result = conv.intToRoman(2577)
        self.assertEqual(result, 'MMDLXXVII')

    def testRomanToIntMax(self):
        result = conv.intToRoman(3999)
        self.assertEqual(result, 'MMMCMXCIX')


    ##### convert #####
    def testConvertNumLess(self):
        result, _, valid = conv.convert('0')
        self.assertEqual(result, "Can't convert 0 and negative numbers")
        self.assertFalse(valid)

    def testConvertNumMin(self):
        result, _, valid = conv.convert('1')
        self.assertEqual(result, 'I')
        self.assertTrue(valid)

    def testConvertNumMax(self):
        result, _, valid = conv.convert('3999')
        self.assertEqual(result, 'MMMCMXCIX')
        self.assertTrue(valid)

    def testConvertNumGreater(self):
        result, _, valid = conv.convert('4000')
        self.assertEqual(result, 'Numbers greater than 3999 are not represented')
        self.assertFalse(valid)


    def testConvertRomanMin(self):
        result, _, valid = conv.convert('I')
        self.assertEqual(result, '1')
        self.assertTrue(valid)

    def testConvertRomanMax(self):
        result, _, valid = conv.convert('MMMCMXCIX')
        self.assertEqual(result, '3999')
        self.assertTrue(valid)

    def testConvertRomanSmallLetters(self):
        result, _, valid = conv.convert('iii')
        self.assertEqual(result, '3')
        self.assertTrue(valid)

    def testConvertRomanInvalid(self):
        result, _, valid = conv.convert('IC')
        self.assertEqual(result, 'Not a valid roman number')
        self.assertFalse(valid)

    def testConvertGibberish(self):
        result, _, valid = conv.convert('k')
        self.assertEqual(result, 'Cannot evaluate expression')
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()
