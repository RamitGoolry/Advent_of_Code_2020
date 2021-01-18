# FILE = 'example2.txt'
FILE = 'test.txt'

import re
import pandas as pd

def convert(passport):
    field_dict = {}
    fields = passport.split()

    for field in fields:
        key, value = field.split(':')
        field_dict[key] = value

    return field_dict

def main():
    with open(FILE) as file:
        passports = file.read().split('\n\n')
        passports = list(map(convert, passports))

    passports = pd.DataFrame(passports) # 252 Passports
    passports = passports.drop('cid', axis=1)
    passports = passports.dropna()

    rules = {
        'byr' : r'19[2-9]\d|200[0-2]',
        'iyr' : r'20[1-2]\d',
        'eyr' : r'20[2-3]\d',
        'hgt' : r'1[5-8]\dcm$|19[0-3]cm$|59in$|6\din$|7[0-6]in$',
        'hcl' : r'^#[0-9a-f]{6}$',
        'ecl' : r'amb|blu|brn|gry|grn|hzl|oth',
        'pid' : r'^[0-9]{9}$'
    }
    
    for category in rules:
        passports = passports[passports[category].str.contains(rules[category])]

    print(passports.shape)

if __name__ == '__main__':
    main()