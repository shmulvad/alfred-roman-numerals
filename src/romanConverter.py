import sys, json

valLst = [1000, 900, 500, 400, 100, 90, 50, 40,
    10, 9, 5, 4, 1]

romanLst = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
    "X", "IX", "V", "IV", "I"]

# Greedy algorithm for converting roman numeral to arabic integer
def romanToInt(romanNum):
    num = 0
    while len(romanNum) > 0:
        # Try first two chars
        if romanNum[:2] in romanLst:
            index = romanLst.index(romanNum[:2])
            num += valLst[index]
            romanNum = romanNum[2:]
        # Try first char
        elif romanNum[:1] in romanLst:
            index = romanLst.index(romanNum[:1])
            num += valLst[index]
            romanNum = romanNum[1:]
        else:
            return "ERROR"
    return str(num)


# Greedy algorithm for converting arabic integer to roman numeral
def intToRoman(num):
    romanNum = ''
    i = 0
    while num > 0:
        romanSymbolOccurences = num // valLst[i]
        for _ in range(romanSymbolOccurences):
            romanNum += romanLst[i]
            num -= valLst[i]
        i += 1
    return romanNum


# Parse user input and convert arabic int to roman numeral or reverse
def convert(query):
    try:
        num = int(query, 10)
    except ValueError: # Roman numeral to Arabic integer
        queryUp = query.upper()
        convInt = romanToInt(queryUp)
        if convInt == "ERROR":
            return "Cannot evaluate expression", query, False
        else:
            # Check that it is valid roman numeral and not i.e. "IC"
            # by converting back to roman and see if we get the original
            convRoman = intToRoman(int(convInt))
            if not(queryUp == convRoman):
                return "Not a valid roman number", query, False
            return convInt, "Roman to arabic", True
    else: # Arabic integer to Roman numeral
        if num < 1:
            return "Can't convert 0 and negative numbers", query, False
        elif num > 3999:
            return "Numbers greater than 3999 are not represented", query, False
        return intToRoman(num), "Arabic to roman", True


# Get the query and output to Alfred in JSON-format
query = sys.argv[1]
title, subtitle, valid = convert(query)
jsonResult = json.dumps({"items": [
    {
        "title": title,
        "subtitle": subtitle,
        "arg": title,
        "valid": valid
    }
]})
print(jsonResult)
