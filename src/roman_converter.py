import sys
import json
from typing import Tuple

NUM_LST = [1000, 900, 500, 400, 100, 90, 50, 40,
           10, 9, 5, 4, 1]

ROMAN_LST = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL',
             'X', 'IX', 'V', 'IV', 'I']


# Greedy algorithm for converting roman numeral to arabic integer
def roman_to_int(roman_num: str) -> str:
    ret_num = 0
    while len(roman_num) > 0:
        # Try first two chars
        if roman_num[:2] in ROMAN_LST:
            index = ROMAN_LST.index(roman_num[:2])
            ret_num += NUM_LST[index]
            roman_num = roman_num[2:]
        # Try first char
        elif roman_num[:1] in ROMAN_LST:
            index = ROMAN_LST.index(roman_num[:1])
            ret_num += NUM_LST[index]
            roman_num = roman_num[1:]
        else:
            raise ValueError
    return str(ret_num)


# Greedy algorithm for converting arabic integer to roman numeral
def int_to_roman(num: int) -> str:
    roman_num = ''
    symbol_idx = 0
    while num > 0:
        num_roman_symbol_occurences = num // NUM_LST[symbol_idx]
        roman_num += ROMAN_LST[symbol_idx] * num_roman_symbol_occurences
        num -= NUM_LST[symbol_idx] * num_roman_symbol_occurences
        symbol_idx += 1
    return roman_num


# Parse user input and convert arabic int to roman numeral or reverse
def convert(query: str) -> Tuple[str, str, bool]:
    try:
        num = int(query, 10)
    # Roman numeral to Arabic integer
    except ValueError:
        try:
            query_up = query.upper()
            conv_int = roman_to_int(query_up)
            # Check that it is valid roman numeral and not i.e. 'IC'
            # by converting back to roman and see if we get the original
            if (query_up != int_to_roman(int(conv_int))):
                return 'Not a valid roman number', query, False
            return conv_int, 'Roman to arabic', True
        except ValueError:
            return 'Cannot evaluate expression', query, False
    # Arabic integer to Roman numeral
    else:
        if num < 1:
            return "Can't convert 0 and negative numbers", query, False
        elif num > 3999:
            return 'Numbers greater than 3999 are not represented', query, False
        return int_to_roman(num), 'Arabic to roman', True


# Get the query and output to Alfred in JSON-format
if __name__ == '__main__':
    query = sys.argv[1]
    title, subtitle, is_valid = convert(query)
    json_res = json.dumps({'items': [{
        'title': title,
        'subtitle': subtitle,
        'arg': title,
        'valid': is_valid
    }]})
    print(json_res)
