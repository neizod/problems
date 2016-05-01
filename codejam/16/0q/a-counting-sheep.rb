#!/usr/bin/env ruby
require 'set'

gets.to_i.times do |test|
    ans = 'INSOMNIA'
    unless (num = gets.to_i).zero?
        ans = 0
        rem = (0..9).to_set
        until rem.size.zero? do
            ans += num
            rem -= ans.to_s.split('').map(&:to_i)
        end
    end
    puts "Case ##{test+1}: #{ans}"
end
