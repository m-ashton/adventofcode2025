# frozen_string_literal: true

def valid_part1?(id)
  digits = id.digits
  num_digits = digits.length
  return true if num_digits.odd?

  first_half = digits[0...(num_digits / 2)]
  second_half = digits[(num_digits / 2)..]
  first_half != second_half
end

def valid_part2?(id)
  digits = id.digits
  num_digits = digits.length
  (1...num_digits).each do |sub_length|
    next unless (num_digits % sub_length).zero?

    subsequences = digits.each_slice(sub_length).to_a
    return false if subsequences.all?(subsequences[0])
  end
  true
end

def part1
  invalid_id_sum = 0

  id_ranges = File.open('input.txt').read.strip.split(',')
  id_ranges.each do |id_range|
    start_id, end_id = id_range.split('-').map(&:to_i)
    invalid_ids = (start_id..end_id).reject { |id| valid_part1?(id) }
    invalid_id_sum += invalid_ids.sum
  end
  invalid_id_sum
end

def part2
  invalid_id_sum = 0

  id_ranges = File.open('input.txt').read.strip.split(',')
  id_ranges.each do |id_range|
    start_id, end_id = id_range.split('-').map(&:to_i)
    invalid_ids = (start_id..end_id).reject { |id| valid_part2?(id) }
    invalid_id_sum += invalid_ids.sum
  end
  invalid_id_sum
end

ARGV[0] == '2' ? puts(part2) : puts(part1)
