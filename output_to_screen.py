cave_man = "Fred Flintstone"
city = "Bedrock"
value = 89.38032

print(cave_man, city, value)

#   str(cave_man) + " " + str(city) + " " + str(value) + "\n"
print("cave man:", cave_man)

print(cave_man, city, sep=',')
print(cave_man, city, sep='#')
print(cave_man, city, sep='')
print(cave_man, city, sep='\n')

print("first part", end=" ")
# if ...
print("more", end=" ")
# if ...
print("more", end=" ")
print("end")

print(cave_man, city, sep=',')
print()

x = cave_man + ',' + city + ',' + str(value)
print(x)

s = f"{cave_man},{city},{value}"
print(s)
print(f"{cave_man} lives in {city}")

print(f"{cave_man} lives in {city} VALUE: {value}")
print(f"{cave_man} lives in {city} VALUE: {value:.1f}")

print(f"2 + 2 = {2 + 2}")

# f"" only >= version 3.6
print("{} lives in {} VALUE: {:.1f}".format(cave_man, city, value))

x = 57
print(f"x: {x}")











