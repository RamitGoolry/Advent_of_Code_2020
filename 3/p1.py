# FILE = 'example.txt'
FILE = 'test.txt'

RIGHT = 3
DOWN = 1

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
    
    print(count_trees(m, RIGHT, DOWN))

if __name__ == '__main__':
    main()