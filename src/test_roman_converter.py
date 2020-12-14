import pytest
from roman_converter import roman_to_int, int_to_roman, convert


class TestRomanToInt:
    def test_two_symbol(self):
        assert roman_to_int('IV') == '4'

    def test_hard(self):
        assert roman_to_int('MMDLXXVII') == '2577'

    def test_max(self):
        assert roman_to_int('MMMCMXCIX') == '3999'

    def test_gibberish_raises_error(self):
        with pytest.raises(ValueError):
            roman_to_int('k')


class TestIntToRoman:
    def test_simple(self):
        assert int_to_roman(1) == 'I'

    def test_two_symbol(self):
        assert int_to_roman(4) == 'IV'

    def test_hard(self):
        assert int_to_roman(2577) == 'MMDLXXVII'

    def test_max(self):
        assert int_to_roman(3999) == 'MMMCMXCIX'


class TestConvert:
    def test_num_less(self):
        result, _, is_valid = convert('0')
        assert result == "Can't convert 0 and negative numbers"
        assert is_valid is False

    def test_num_min(self):
        result, _, is_valid = convert('1')
        assert result == 'I'
        assert is_valid

    def test_num_max(self):
        result, _, is_valid = convert('3999')
        assert result == 'MMMCMXCIX'
        assert is_valid

    def test_num_greater(self):
        result, _, is_valid = convert('4000')
        assert result == 'Numbers greater than 3999 are not represented'
        assert is_valid is False

    def test_roman_min(self):
        result, _, is_valid = convert('I')
        assert result == '1'
        assert is_valid

    def test_roman_max(self):
        result, _, is_valid = convert('MMMCMXCIX')
        assert result == '3999'
        assert is_valid

    def test_roman_small_letters(self):
        result, _, is_valid = convert('iii')
        assert result == '3'
        assert is_valid

    def test_roman_invalid(self):
        result, _, is_valid = convert('IC')
        assert result == 'Not a valid roman number'
        assert is_valid is False

    def test_gibberish(self):
        result, _, is_valid = convert('k')
        assert result == 'Cannot evaluate expression'
        assert is_valid is False
