""" 
Check passport requirements.
"""
import re

from typing import Dict

def is_four_digit_str(input_str):
    return isinstance(input_str, str) and len(input_str) == 4

def is_valid_height(input_str):
    if input_str.endswith("cm"):
        input_num = int(input_str[:-2])
        return input_num >= 150 and input_num <= 193
    elif input_str.endswith("in"):
        input_num = int(input_str[:-2])
        return input_num >= 59 and input_num <= 76
    else:
        return False

def is_valid_hair_colour(input_str):
    if not input_str.startswith("#") or len(input_str) != 7:
        return False
    try:
        input_num = int(input_str[1:], 16)
        return True
    except ValueError:
        return False

REQUIRED_FIELDS_ONE = {x: lambda y: True for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]}
REQUIRED_FIELDS_TWO = {"byr": lambda y: is_four_digit_str(y) and int(y) >= 1920 and int(y) <= 2002,
                       "iyr": lambda y: is_four_digit_str(y) and int(y) >= 2010 and int(y) <= 2020,
                       "eyr": lambda y: is_four_digit_str(y) and int(y) >= 2020 and int(y) <= 2030,
                       "hgt": is_valid_height,
                       "hcl": is_valid_hair_colour,
                       "ecl": lambda y: y in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
                       "pid": lambda y: len(y) == 9 and y.isnumeric()}


def is_valid(passport: Dict, required_fields) -> bool:
    """For each key in required_fields, check the passport satisfies the condition.
    
    For Part 1, it's just True
    For Part 2, it's more complicated.
    """
    for required_field, test in required_fields.items():
        if required_field not in passport or not test(passport[required_field]):
            return False
    return True
    

if __name__ == "__main__":

# read the passport data in
    with open("input.txt") as flines:
        input_data = flines.read()
    passports = [x.split() for x in input_data.split("\n\n")]
    
    valid_passports_one = 0
    valid_passports_two = 0
    for passport in passports:
        passport_dict = dict([x.split(":") for x in passport])
        if is_valid(passport_dict, REQUIRED_FIELDS_ONE):
            valid_passports_one += 1
        if is_valid(passport_dict, REQUIRED_FIELDS_TWO):
            valid_passports_two += 1
    print(valid_passports_one)
    print(valid_passports_two)