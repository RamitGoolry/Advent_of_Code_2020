# FILE = 'example.txt'
FILE = 'test.txt'

import pandas as pd

def convert(boarding_pass):
    row_enc, seat_enc = boarding_pass[:7], boarding_pass[7:]

    row_enc = eval('0b' + row_enc.replace('F', '0').replace('B', '1'))
    seat_enc = eval('0b' + seat_enc.replace('L', '0').replace('R', '1'))

    return {
        'pass' : boarding_pass,
        'row' : row_enc,
        'seat' : seat_enc,
        'seat_id' : row_enc * 8 + seat_enc
    }

def main():
    with open(FILE) as file:
        passes = file.read().split()
    
    passes = pd.DataFrame(map(convert, passes))
    
    sids = sorted(passes.seat_id)

    for i in range(len(sids) - 1):
        if sids[i + 1] - sids[i] != 1:
            print(sids[i] + 1)

if __name__ == '__main__':
    main()