# frozen_string_literal: true

def read_input(filename)
  start_pos = [0, 0]
  # grid is in the form of grid[y] = [x1, x2, x3...]
  grid = Hash.new { |h, k| h[k] = [] }.tap do |grid|
    File.foreach(filename).with_index do |line, y|
      line.strip.chars.each.with_index do |character, x|
        if character == 'S'
          start_pos = [x, y]
        elsif character == '^'
          grid[y] << x
        end
      end
    end
  end
  [start_pos, grid]
end

def part1
  start_pos, grid = read_input('input.txt')
  splits = 0
  beams = [start_pos[0]]
  grid.each_value do |splitter_positions|
    split_beams, continued_beams = beams.partition { |beam| splitter_positions.include?(beam) }
    splits += split_beams.count
    beams = split_beams.map { |x| [x - 1, x + 1] }.flatten + continued_beams
    beams = beams.uniq
  end
  splits
end

def part2
  start_pos, grid = read_input('sample.txt')
  # beams = Hash.new { |h, k| h[k] = 0 }
  # beams[start_pos[0]] = 1
  beams = [start_pos[0]]
  grid.each_value do |splitter_positions|
    # split_beams, continued_beams = beams.partition { |beam, _| splitter_positions.include?(beam) }
    split_beams, continued_beams = beams.partition { |beam| splitter_positions.include?(beam) }
    beams = split_beams.map { |x| [x - 1, x + 1] }.flatten + continued_beams
    # new_beams = Hash.new { |h, k| h[k] = 0 }
    # split_beams.each do |beam|
      # x = beam[0]
      # new_beams[x + 1] += 1
      # new_beams[x - 1] += 1
    # end
    # continued_beams.each do |beam|
      # x = beam[0]
      # new_beams[x] += 1
    # end
    # beams = new_beams
  end
  # beams.values.sum
  beams.count
end

if $PROGRAM_NAME == __FILE__
  ARGV[0] == '2' ? puts(part2) : puts(part1)
end
