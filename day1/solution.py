import sys

def rotate(position, distance):
    rotations = 0
    while distance != 0:
        if distance < 0:
            position -= 1
            distance += 1
            if position < 0:
                position += 100
        elif distance > 0:
            position += 1
            distance -= 1
            if position > 99:
                position -= 100
        if position == 0:
            rotations += 1
    return position, rotations


def part1():
    with open('input.txt') as f:
        zeroes = 0
        position = 50
        for instruction in f:
            distance = int(instruction[1:])
            if instruction.startswith('L'):
                distance = -distance
            position, _ = rotate(position, distance)
            if position == 0:
                zeroes += 1
        return zeroes

def part2():
    with open('input.txt') as f:
        zeroes = 0
        position = 50
        for instruction in f:
            distance = int(instruction[1:])
            if instruction.startswith('L'):
                distance = -distance
            position, rotations = rotate(position, distance)
            zeroes += rotations
        return zeroes

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '2':
        print(part2())
    else:
        print(part1())