# frozen_string_literal: true

def read_input(filename)
  ranges, ids = File.open(filename).read.split("\n\n")
  ranges = ranges.split("\n").map do |range|
    range.split('-').map(&:to_i)
  end
  ranges = ranges.map do |start_id, end_id|
    start_id..end_id
  end

  ids = ids.split("\n").map(&:to_i)

  [ranges, ids]
end

def part1
  ranges, ids = read_input('input.txt')
  ids.count do |id|
    ranges.any? { |range| range.include?(id) }
  end
end

def part2
  ranges, = read_input('input.txt')
  ranges = ranges.sort_by(&:first)
  ranges = ranges[1..].each_with_object([ranges.first]) do |next_range, memo|
    current_range = memo.pop
    if next_range.first <= current_range.last
      range_end = [current_range.last, next_range.last].max
      memo << (current_range.first..range_end)
    else
      memo << current_range
      memo << next_range
    end
  end
  ranges.sum(&:count)
end

if $PROGRAM_NAME == __FILE__
  ARGV[0] == '2' ? puts(part2) : puts(part1)
end
