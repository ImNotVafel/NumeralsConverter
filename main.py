"""
Module for converting roman numerals to arabic, and vice versa.

"""
# SECTION: Standart library imports:
from operator import add, sub
# SECTION: Related third party imports:
...
# SECTION: Local application specific imports:
...


# SECTION: Types, constants, utils.
RomanNumber = RomanNumeral = str
ArabicNumber = ArabicNumeral = int

NUMERALS: dict[RomanNumeral, ArabicNumeral] = {
    # PEP8 is furious, but the dictionary is pretty
    'I' : 1,
    'IV': 4,
    'V' : 5,
    'IX': 9,
    'X' : 10,
    'XL': 40,
    'L' : 50,
    'XC': 90,
    'C' : 100,
    'CD': 400,
    'D' : 500,
    'CM': 900,
    'M' : 1000,
}


# SECTION: Main.
def get_arabic_as_roman(number: ArabicNumber) -> RomanNumber:
    """Returns string with roman number."""
    result = ""

    while number > 0:
        for roman_numeral, arabic_numeral in reversed(NUMERALS.items()):
            if number < arabic_numeral: continue
            number -= arabic_numeral
            result += roman_numeral
            break

    return result


def get_roman_as_arabic(number: RomanNumber) -> ArabicNumber:
    """Returns string with arabic number."""
    result = 0

    for index, numeral in enumerate(number):
        is_last_number = index + 1 == len(number)
        next_number = None if is_last_number else number[index + 1]
        next_bigger = False if next_number is None else NUMERALS[next_number] > NUMERALS[numeral]
        operator = sub if next_bigger else add

        result = operator(result, NUMERALS[numeral])

    return result


