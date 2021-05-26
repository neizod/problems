#!/usr/bin/env ruby

gets.to_i.times do |test|
  cj, jc, pattern = gets.split
  ans = 0
  pattern.delete("?").split("").each_cons(2) { |a,b|
    ans += cj.to_i if a+b == "CJ"
    ans += jc.to_i if a+b == "JC"
  }
  puts "Case ##{test+1}: #{ans}"
end
