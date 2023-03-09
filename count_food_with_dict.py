food_counts = {}

with open('DATA/breakfast.txt') as food_in:
    for raw_food in food_in:
        print(food_counts, '\n')
        food = raw_food.rstrip()
        print(f"food: {food}")
        if not food in food_counts:
            food_counts[food] = 0  # initialize count for this food
        food_counts[food] += 1  #  f[food] = f[food] + 1

for food, count in food_counts.items():
    print(food, count)