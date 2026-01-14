# frozen_string_literal: true

def read_input(filename)
  lines = File.open(filename).readlines
  problems = lines.map(&:split).transpose
  problems.map { |problem| [*problem[0..-2].map(&:to_i), problem[-1].to_sym] }
end

def read_input_part2(filename)
  lines = File.open(filename).readlines.map { |line| line.gsub("\n", '') }
  operators = lines.pop.gsub(' ', '').chars.map(&:to_sym)
  column_chars = lines.map(&:chars).transpose
  numbers = column_chars.map { |line| line.join.to_i }
  problems = numbers.slice_after(&:zero?).map { |numbers| numbers.reject(&:zero?) }
  problems.zip(operators).map(&:flatten)
end

def part1
  problems = read_input('input.txt')
  problems.sum { |problem| problem[0..-2].reduce(problem.last) }
end

def part2
  problems = read_input_part2('input.txt')
  problems.sum { |problem| problem[0..-2].reduce(problem.last) }
end

if $PROGRAM_NAME == __FILE__
  ARGV[0] == '2' ? puts(part2) : puts(part1)
end
