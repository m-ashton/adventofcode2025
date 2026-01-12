# frozen_string_literal: true

def max_joltage(battery, length: 2)
  digits = []
  start = 0
  remaining = length
  end_pos = battery.length - remaining
  while remaining.positive?
    max_digit = battery[start..end_pos].max
    position = battery[start..end_pos].index(max_digit) + start
    digits.append(max_digit)

    remaining -= 1
    start = position + 1
    end_pos = battery.length - remaining
  end
  digits.map(&:to_s).join.to_i
end

def part1
  lines = File.open('input.txt').readlines
  lines.map { |line| max_joltage(line.strip.chars.map(&:to_i)) }.sum
end

def part2
  lines = File.open('input.txt').readlines
  lines.map { |line| max_joltage(line.strip.chars.map(&:to_i), length: 12) }.sum
end

if $PROGRAM_NAME == __FILE__
  ARGV[0] == '2' ? puts(part2) : puts(part1)
end
