# FILE = 'example.txt'
FILE = 'test.txt'

from functools import reduce

X, Y = 0, 1

def count_trees(m, dx, dy):
    x_len, y_len = len(m[0]), len(m)

    pos = [0, 0]
    count = 0

    while pos[Y] < y_len:
        if m[pos[Y]][pos[X]] == '#':
            count += 1
        
        pos[X] = (pos[X] + dx) % x_len
        pos[Y] = pos[Y] + dy
    
    return count

def main():
    with open(FILE) as file:
        m = file.read().split()
    
    print(reduce(lambda x, y : x * y, [count_trees(m, right, down) for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))
        

if __name__ == '__main__':
    main()