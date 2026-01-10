# frozen_string_literal: true

def rotate(position, distance)
  rotations = 0
  until distance.zero?
    if distance.negative?
      position -= 1
      distance += 1
      position += 100 if position.negative?
    elsif distance.positive?
      position += 1
      distance -= 1
      position -= 100 if position > 99
    end
    rotations += 1 if position.zero?
  end
  [position, rotations]
end

def part1
  zeroes = 0
  position = 50
  File.open('input.txt').readlines.each do |line|
    distance = line.strip.chars[1..].join.to_i
    distance = -distance if line.start_with?('L')
    position, = rotate(position, distance)
    zeroes += 1 if position.zero?
  end
  zeroes
end

def part2
  zeroes = 0
  position = 50
  File.open('input.txt').readlines.each do |line|
    distance = line.strip.chars[1..].join.to_i
    distance = -distance if line.start_with?('L')
    position, rotations = rotate(position, distance)
    zeroes += rotations
  end
  zeroes
end

ARGV[0] == '2' ? puts(part2) : puts(part1)
