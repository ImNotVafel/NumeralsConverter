# Numerals Converter.
Writed on python converter for convert arabic numbers to roman, and vice versa.

Operating range: 1-3999 (inclusive).


## Requirements/Instalation.
Requires only python (Tested versions: 3.11.0).


## Usage Example:
```python
# Simple tests:
assert get_arabic_as_roman(1000) == 'M'
assert get_arabic_as_roman(4) == 'IV'
assert get_arabic_as_roman(1) == 'I'
assert get_arabic_as_roman(1990) == 'MCMXC'
assert get_arabic_as_roman(2008) == 'MMVIII'

assert get_roman_as_arabic("CCCXLIX") == 349
assert get_roman_as_arabic("XXI") == 21
assert get_roman_as_arabic("I") == 1
assert get_roman_as_arabic("IV") == 4
assert get_roman_as_arabic("MMVIII") == 2008
assert get_roman_as_arabic("MDCLXVI") == 1666
```


