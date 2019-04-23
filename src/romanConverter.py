import sys, json

NUM_LST = [1000, 900, 500, 400, 100, 90, 50, 40,
    10, 9, 5, 4, 1]

ROMAN_LST = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL',
    'X', 'IX', 'V', 'IV', 'I']

# Greedy algorithm for converting roman numeral to arabic integer
def romanToInt(romanNum):
    num = 0
    while len(romanNum) > 0:
        # Try first two chars
        if romanNum[:2] in ROMAN_LST:
            index = ROMAN_LST.index(romanNum[:2])
            num += NUM_LST[index]
            romanNum = romanNum[2:]
        # Try first char
        elif romanNum[:1] in ROMAN_LST:
            index = ROMAN_LST.index(romanNum[:1])
            num += NUM_LST[index]
            romanNum = romanNum[1:]
        else:
            raise ValueError
    return str(num)


# Greedy algorithm for converting arabic integer to roman numeral
def intToRoman(num):
    romanNum = ''
    symbolIndex = 0
    while num > 0:
        romanSymbolOccurences = num // NUM_LST[symbolIndex]
        for _ in range(romanSymbolOccurences):
            romanNum += ROMAN_LST[symbolIndex]
            num -= NUM_LST[symbolIndex]
        symbolIndex += 1
    return romanNum


# Parse user input and convert arabic int to roman numeral or reverse
def convert(query):
    try:
        num = int(query, 10)
    # Roman numeral to Arabic integer
    except ValueError:
        try:
            queryUp = query.upper()
            convInt = romanToInt(queryUp)
            # Check that it is valid roman numeral and not i.e. 'IC'
            # by converting back to roman and see if we get the original
            if (queryUp != intToRoman(int(convInt))):
                return 'Not a valid roman number', query, False
            return convInt, 'Roman to arabic', True
        except ValueError:
            return 'Cannot evaluate expression', query, False
    # Arabic integer to Roman numeral
    else:
        if num < 1:
            return "Can't convert 0 and negative numbers", query, False
        elif num > 3999:
            return 'Numbers greater than 3999 are not represented', query, False
        return intToRoman(num), 'Arabic to roman', True


# Get the query and output to Alfred in JSON-format
if __name__ == '__main__':
    query = sys.argv[1]
    title, subtitle, valid = convert(query)
    jsonResult = json.dumps({'items': [
        {
            'title': title,
            'subtitle': subtitle,
            'arg': title,
            'valid': valid
        }
    ]})
    print(jsonResult)
