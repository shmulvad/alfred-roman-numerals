import pytest
from roman_converter import roman_to_int, int_to_roman, convert


# roman_to_int
def test_roman_to_int_two_symbol():
    assert roman_to_int('IV') == '4'


def test_roman_to_int_hard():
    assert roman_to_int('MMDLXXVII') == '2577'


def test_roman_to_int_max():
    assert roman_to_int('MMMCMXCIX') == '3999'


def test_roman_to_int_gibberish_raises_error():
    with pytest.raises(ValueError):
        roman_to_int('k')


# int_to_roman
def test_int_to_roman_simple():
    assert int_to_roman(1) == 'I'


def test_int_to_roman_two_symbol():
    assert int_to_roman(4) == 'IV'


def test_int_to_roman_hard():
    assert int_to_roman(2577) == 'MMDLXXVII'


def test_int_to_roman_max():
    assert int_to_roman(3999) == 'MMMCMXCIX'


# convert
def test_convert_num_less():
    result, _, is_valid = convert('0')
    assert result == "Can't convert 0 and negative numbers"
    assert is_valid is False


def test_convert_num_min():
    result, _, is_valid = convert('1')
    assert result == 'I'
    assert is_valid


def test_convert_num_max():
    result, _, is_valid = convert('3999')
    assert result == 'MMMCMXCIX'
    assert is_valid


def test_convert_num_greater():
    result, _, is_valid = convert('4000')
    assert result == 'Numbers greater than 3999 are not represented'
    assert is_valid is False


def test_convert_roman_min():
    result, _, is_valid = convert('I')
    assert result == '1'
    assert is_valid


def test_convert_roman_max():
    result, _, is_valid = convert('MMMCMXCIX')
    assert result == '3999'
    assert is_valid


def test_convert_roman_small_letters():
    result, _, is_valid = convert('iii')
    assert result == '3'
    assert is_valid


def test_convert_roman_invalid():
    result, _, is_valid = convert('IC')
    assert result == 'Not a valid roman number'
    assert is_valid is False


def test_convert_gibberish():
    result, _, is_valid = convert('k')
    assert result == 'Cannot evaluate expression'
    assert is_valid is False
