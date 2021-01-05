from functools import reduce

FILE = './test.txt'

def three_sum(lst, target):
    for n in lst:
        ts = two_sum(lst, target - n) 
        if ts != None:
            return n, ts[0], ts[1]
    return None

def two_sum(lst, target):
    ans = -1

    for n in lst:
        if target - n in lst:
            ans = n

    if ans == -1:
        return None
    
    return ans, target - ans

def main():
    with open(FILE) as file:
        lst = [int(number) for number in file.readlines()]

    print(reduce(lambda x, y : x * y, three_sum(lst, 2020)))

if __name__ == '__main__':
    main()
