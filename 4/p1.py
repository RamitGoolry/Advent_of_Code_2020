# FILE = 'example.txt'
FILE = 'test.txt'

VALID = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def is_valid(passport):
    def convert(passport):
        field_dict = {}
        fields = passport.split()

        for field in fields:
            key, value = field.split(':')
            field_dict[key] = value

        return field_dict

    passport = convert(passport)

    return len(VALID & set(passport.keys())) == len(VALID)

def main():
    with open(FILE) as file:
        passports = file.read().split('\n\n')
    
    print(sum(map(is_valid, passports)))

if __name__ == '__main__':
    main()