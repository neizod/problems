fs = require 'fs'

optimal_cookie = (new_farm_cost, prodct_cookie, finale_cookie) ->
    income_cookie = 2.0
    optimal_spent = 0
    loop
        new_farm_time = new_farm_cost / income_cookie
        expect_cookie = prodct_cookie + income_cookie
        wait_win_time = finale_cookie / income_cookie
        upgd_win_time = finale_cookie / expect_cookie + new_farm_time
        if wait_win_time > upgd_win_time
            income_cookie = expect_cookie
            optimal_spent += new_farm_time
        else
            optimal_spent += wait_win_time
            break
    optimal_spent

fs.readFile 'B-large.in', (err, raw) ->
    data = raw.toString().split('\n')
    for i in [1..Number(data.shift())]
        answer = optimal_cookie((Number(n) for n in data.shift().split(' '))...)
        console.log("Case ##{i}: #{answer.toFixed(7)}")
