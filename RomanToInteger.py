def romanToInt(s: str) -> int:
    roman_sum = 0
    roman = {"I": 1, "V": 5,
             "X": 10, "L": 50,
             "C": 100, "D": 500,
             "M": 1000
            }

    for char in s:
        roman_sum += roman[char]

    if "IV" in s:
        roman_sum -= 2
    if "IX" in s:
        roman_sum -= 2
    if "XL" in s:
        roman_sum -= 20
    if "XC" in s:
        roman_sum -= 20
    if "CD" in s:
        roman_sum -= 200
    if "CM" in s:
        roman_sum -= 200

    return roman_sum
