# FILE = 'example.txt'
FILE = 'test.txt'

def parseGroup(group):
    individuals = group.split()

    questions = set(c for c in 'abcdefghijklmnopqrstuvwxyz')

    for individual in individuals:
        questions = questions & set(c for c in individual)
    
    return len(questions)

def main():
    with open(FILE) as file:
        groups = file.read().split('\n\n')
    
    print(sum(map(parseGroup, groups)))

if __name__ == '__main__':
    main()