import sys
from math import sqrt

def adjacent_positions(x, y):
    adjacent_positions = []
    for delta_x in range(-1, 2):
        for delta_y in range(-1, 2):
            if delta_x == delta_y == 0:
                continue
            adjacent_positions.append((x + delta_x, y + delta_y))
    return adjacent_positions

def accessible_rolls(grid):
    # assume square input
    size = int(sqrt(len(grid.keys())))

    accessible_rolls = []
    for x in range(0, size):
        for y in range(0, size):
            roll_count = 0
            if (grid[(x,y)] == '.'):
                continue
            else:
                for pos in adjacent_positions(x,y):
                    try:
                        val = grid[pos]
                        if val == '@':
                            roll_count += 1
                    except KeyError:
                        pass
            if roll_count < 4:
                accessible_rolls.append((x,y))
    return accessible_rolls


def read_input(filename):
    grid = {}
    with open(filename) as f:
        for y, line in enumerate(f):
            for x, character in enumerate(line.strip()):
                grid[(x, y)] = character
    return grid

def part1():
    grid = read_input('input.txt')
    return len(accessible_rolls(grid))

def part2():
    grid = read_input('input.txt')
    rolls_to_remove = accessible_rolls(grid)
    removed_rolls = 0
    while(rolls_to_remove):
        for position in rolls_to_remove:
            grid[position] = '.'
        removed_rolls += len(rolls_to_remove)
        rolls_to_remove = accessible_rolls(grid)
    return removed_rolls

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '2':
        print(part2())
    else:
        print(part1())