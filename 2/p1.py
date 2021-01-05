# FILE = 'example.txt'
FILE = 'test.txt'

def is_valid(line):
    condition, password = [x.strip() for x in line.split(':')]

    # Parsing Condition
    range, char = condition.split()
    lower, upper = [int(n) for n in range.split('-')]

    count = len(filter(lambda x : x == char, password))

    return lower <= count <= upper

def main():
    with open(FILE) as file:
        lst = file.read().split('\n')[:-1]

    print(sum(map(is_valid, lst)))

if __name__ == '__main__':
    main()
