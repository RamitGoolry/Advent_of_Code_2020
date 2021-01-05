# FILE = 'example.txt'
FILE = 'test.txt'

def is_valid(line):
    condition, password = [x.strip() for x in line.split(':')]

    # Parsing Condition
    range, char = condition.split()
    lower, upper = [int(n) - 1 for n in range.split('-')]

    count = sum([password[lower] == char, password[upper] == char])

    return count == 1

def main():
    with open(FILE) as file:
        lst = file.read().split('\n')[:-1]

    print(sum(map(is_valid, lst)))

if __name__ == '__main__':
    main()
