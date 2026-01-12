# frozen_string_literal: true

def adjacent_positions(x, y)
  deltas = [-1, 0, 1].product([-1, 0, 1]).reject { |x, y| x.zero? && y.zero? }
  deltas.map { |delta_x, delta_y| [x + delta_x, y + delta_y] }
end

def accessible_rolls(grid)
  # assume square input
  size = Math.sqrt(grid.size).to_i

  [].tap do |accessible_rolls|
    (0...size).each do |x|
      (0...size).each do |y|
        next if grid[[x, y]] == '.'

        roll_count = adjacent_positions(x, y).map { |pos| grid[pos] }.count('@')

        accessible_rolls.append([x, y]) if roll_count < 4
      end
    end
  end
end

def read_input(filename)
  {}.tap do |grid|
    File.foreach(filename).with_index do |line, y|
      line.strip.chars.each.with_index do |character, x|
        grid[[x, y]] = character
      end
    end
  end
end

def part1
  grid = read_input('input.txt')
  accessible_rolls(grid).length
end

def part2
  grid = read_input('input.txt')
  rolls_to_remove = accessible_rolls(grid)
  removed_rolls = 0
  until rolls_to_remove.empty?
    rolls_to_remove.each do |position|
      grid[position] = '.'
    end
    removed_rolls += rolls_to_remove.length
    rolls_to_remove = accessible_rolls(grid)
  end
  removed_rolls
end

if $PROGRAM_NAME == __FILE__
  ARGV[0] == '2' ? puts(part2) : puts(part1)
end
