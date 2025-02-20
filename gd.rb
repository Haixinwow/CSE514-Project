#!/usr/bin/env ruby
require "optparse"
require "csv"

csv = CSV.read("trainingstd.csv", :headers => true)
# p csv['strength']
# return

ARGV << "-h" if ARGV.empty?

# default args
options = {
  :m => 1,
  :b => 1,
  :a => 0.1,
  :n => 1,
}

# parse command line args
parser = OptionParser.new do |opts|
  opts.banner = "example usage: ruby gd.rb -x 'fly ash' -y 'strength' -a 0.1"

  opts.on("-xX", "column title of input (string)") do |o|
    options[:x] = csv[o.to_s].map { |x| x.to_f }
  end
  opts.on("-yY", "column title of response variable (string)") do |o|
    options[:y] = csv[o.to_s].map { |y| y.to_f }
  end
  opts.on("-mM", "(optional) set starting m value. default: 1") do |o|
    options[:m] = o.to_i
  end
  opts.on("-bB", "(optional) set starting b value. default: 1") do |o|
    options[:b] = o.to_i
  end
  opts.on("-aA", "--alpha", "(optional) set alpha value. default: 0.1") do |o|
    options[:a] = o.to_f
  end
  opts.on("-nN", "--max_iter", "(optional) set max number of iterations. default: 1") do |o|
    options[:b] = o.to_i
  end

  opts.on("-h", "--help", "prints this help") do |o|
    puts opts
    exit
  end
end

parser.require_exact = true
parser.parse!

m = options[:m]
b = options[:b]
x = options[:x]
y = options[:y]
a = options[:a]
max_iter = options[:n]

## TODO:
# 2. calculate VE and print
# 3. run with various a, n(?)

# max_iter.times do
mse = 1
end
while mse > 0.001 do
  m_gradient = 0
  b_gradient = 0

  x.length.times do |i|
    error = y[i] - (m * x[i] + b)
    m_gradient += -2 * x[i] * error
    b_gradient += -2 * error
  end

  m = m - a * m_gradient / x.length
  b = b - a * b_gradient / x.length

  fx = m*x + b
end

puts "m: #{"%.2f" % m}"
puts "b: #{"%.2f" % b}"

return
# calcs
n = csv['strength'].length

# calculate MSE

# calculate variance
# is there a builtin for this because i'm tired
variance = 0
n.times do
  variance +=
end
variance *= (1/n)

# calculate VE
ve = 1 - (mse / variance)
