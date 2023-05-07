#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or len(roman_string) == 0:
        return 0

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }

    decimal = 0
    for i in range(len(roman_string)):
        if (i != (len(roman_string) - 1) and roman_dict[roman_string[i]] >=
                roman_dict[roman_string[i + 1]]):
            decimal += roman_dict[roman_string[i]]
        elif i == (len(roman_string) - 1):
            decimal += roman_dict[roman_string[i]]
        elif (i != (len(roman_string) - 1) and roman_dict[roman_string[i]] <
                roman_dict[roman_string[i + 1]]):
            decimal -= roman_dict[roman_string[i]]

    return decimal
