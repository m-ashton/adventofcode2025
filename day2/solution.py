import sys

def is_valid(id):
    id = str(id)
    num_digits = len(id)
    if num_digits % 2 != 0:
        return True
    first_half = id[0:(num_digits//2)]
    second_half = id[(num_digits//2):]
    return first_half != second_half

def part1():
    invalid_id_sum = 0
    with open('input.txt') as f:
        input = f.read()
        for ids in input.split(','):
            start, end = map(int, ids.strip().split('-'))
            invalid_ids = filter(lambda x: not is_valid(x), range(start, end + 1))
            invalid_id_sum += sum(invalid_ids)
    return invalid_id_sum



def part2():
    with open('input.txt') as f:
        pass

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '2':
        print(part2())
    else:
        print(part1())