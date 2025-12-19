import sys
from functools import reduce

def max_joltage(battery, length = 2):
    digits = []
    start = 0
    remaining = length
    end = len(battery) - remaining + 1
    while remaining > 0:
        max_digit = max(battery[start:end])
        position = battery[start:end].index(max_digit) + start
        digits.append(max_digit)
        remaining -= 1

        end = len(battery) - remaining + 1
        start = position + 1
    return int(''.join(map(str, digits)))

def part1():
    with open('input.txt') as f:
        maxes = map(lambda x: max_joltage(x.strip()), f)
        return sum(maxes)



def part2():
    with open('input.txt') as f:
        maxes = map(lambda x: max_joltage(x.strip(), 12), f)
        return sum(maxes)

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '2':
        print(part2())
    else:
        print(part1())