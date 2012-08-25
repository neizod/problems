for test in range(int(input())):
    input()
    foods = [int(food) for food in input().split()]

    day = 0
    while all(foods):
        foods.sort(reverse=True)
        fridge = foods.pop()
        foods = [food-1 for food in foods]
        foods.append(fridge)
        day += 1

    print(day)

