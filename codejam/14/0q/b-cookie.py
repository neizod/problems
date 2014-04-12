def optimal_cookie(new_farm_cost, prodct_cookie, finale_cookie):
    income_cookie = 2.0
    optimal_spent = 0
    while True:
        new_farm_time = new_farm_cost / income_cookie
        expect_cookie = prodct_cookie + income_cookie
        wait_win_time = finale_cookie / income_cookie
        upgd_win_time = finale_cookie / expect_cookie + new_farm_time
        if wait_win_time > upgd_win_time:
            income_cookie = expect_cookie
            optimal_spent += new_farm_time
        else:
            optimal_spent += wait_win_time
            break
    return optimal_spent

for case in range(int(input())):
    answer = optimal_cookie(*[float(n) for n in input().split()])
    print('Case #{}: {:.7f}'.format(case+1, answer))
