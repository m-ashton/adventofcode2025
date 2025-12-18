import sys

def is_valid_part1(id):
    id = str(id)
    num_digits = len(id)
    if num_digits % 2 != 0:
        return True
    first_half = id[0:(num_digits//2)]
    second_half = id[(num_digits//2):]
    return first_half != second_half

def is_valid_part2(id):
    id = str(id)
    num_digits = len(id)
    for sub_length in range(1, num_digits):
        if num_digits % sub_length != 0:
            continue
        subsequences = []
        start = 0
        end = sub_length
        while end <= num_digits:
            subsequences.append(id[start:end])
            start += sub_length
            end += sub_length
        if all(map(lambda x: x == subsequences[0], subsequences[1:])):
            return False
    return True


def part1():
    invalid_id_sum = 0
    with open('input.txt') as f:
        input = f.read()
        for ids in input.split(','):
            start, end = map(int, ids.strip().split('-'))
            invalid_ids = filter(lambda x: not is_valid_part1(x), range(start, end + 1))
            invalid_id_sum += sum(invalid_ids)
    return invalid_id_sum

def part2():
    invalid_id_sum = 0
    with open('input.txt') as f:
        input = f.read()
        for ids in input.split(','):
            start, end = map(int, ids.strip().split('-'))
            invalid_ids = filter(lambda x: not is_valid_part2(x), range(start, end + 1))
            invalid_id_sum += sum(invalid_ids)
    return invalid_id_sum

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '2':
        print(part2())
    else:
        print(part1())