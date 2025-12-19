import sys
from functools import reduce

def max_joltage(battery):
    most_significant_digit = -1
    least_significant_digit = -1
    sig_dig_pos = 0
    for i, c in enumerate(battery[0:-1]):
        if int(c) > most_significant_digit:
            most_significant_digit = int(c)
            sig_dig_pos = i
    for c in battery[(sig_dig_pos + 1):]:
        if int(c) > least_significant_digit:
            least_significant_digit = int(c)
    return (10 * most_significant_digit) + least_significant_digit

def part1():
    with open('input.txt') as f:
        maxes = map(lambda x: max_joltage(x.strip()), f)
        return sum(maxes)


def part2():
    pass

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '2':
        print(part2())
    else:
        print(part1())