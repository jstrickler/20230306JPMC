list1 = list()   # new, empty list
# x = list(iterable)
list2 = ['spam', 'ham', 'toast']    # list
t = 'spam', 'ham', 'toast'   # tuple
list3 = [5, 1, 8, -2, 5.3]
list4 = ['spam', 42, True, None, [1, 2, 3]]
list5 = []  # empty list

#  x = [obj, obj, obj, obj, ...]

cities = ['Delaware', 'Dallas', "Washington", "New York",
          "Boston"]
print(f"cities: {cities}")
print(f"cities[3]: {cities[3]}")
cities[1] = "Austin"
print(f"cities: {cities}")
cities.insert(0, "Easton")
print(f"cities: {cities}")
cities.insert(3, "Milwaukee")
print(f"cities: {cities}")
cities.append("Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch")
print(f"cities: {cities}")
cities.append("Philadelphia")
print(f"cities: {cities}")

more_cities = ['Leicester', 'Worcester', 'Peabody', 'Reno']

cities.append(more_cities)
print(f"cities: {cities}")
cities.extend(more_cities)
print(f"cities: {cities}")

# LIST.insert(pos, obj)   LIST.append(obj)   LIST.extend(iterable)
cities.extend("fun")
print(f"cities: {cities}")

del cities[9]
print(f"cities: {cities}")
del cities[7]
print(f"cities: {cities}")

#   del LIST[pos]   del DICT[key]   del any-obj
cities.remove('f')
cities.remove('u')
print(f"cities: {cities}")


item = cities.pop()
print(f"item: {item}")
print(f"cities: {cities}")

item = cities.pop(2)
print(f"item: {item}")
print(f"cities: {cities}")

#  del LIST[pos]   LIST.remove(value)    LIST.pop(pos)  LIST.pop()

city_to_find = "Milwaukee"
if city_to_find in cities:
    index = cities.index(city_to_find)
    print(f"index: {index}")
    item = cities.pop(index)
    print(f"item: {item}")
    print(f"cities: {cities}")

# cities.remove('Milwaukee')


food = ['eggs', 'spam', 'spam', 'spam', 'eggs', 'spam', 'eggs', 'spam']

start_pos = -1
while True:
    start_pos = food.index('eggs', start_pos + 1)
    print("found at", start_pos)
    if start_pos >= len(food):
        break
print()


