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

print(f"cities: {cities}")


print(f"cities[2]: {cities[2]}")
print(f"cities[9]: {cities[9]}")
print(f"cities[len(cities)-1]: {cities[len(cities)-1]}")
print(f"cities[-1]: {cities[-1]}")
print(f"cities[-2]: {cities[-2]}")

#  STR[0]  BYTES[0] LIST[0]  TUPLE[0]
# print(f"cities[22]: {cities[22]}")
print(f"cities: {cities}")

print(f"cities[0:3]: {cities[0:3]}")

#  start:stop  :stop start:  :    start:stop:step

print(f"cities[3:7]: {cities[3:7]}")
print(f"cities[:4]: {cities[:4]}")
print(f"cities[4:]: {cities[4:]}")
print(f"cities[-3:]: {cities[-3:]}")

client = "J P Morgan Chase"
print(f"client[:10]: {client[:10]}")
print(f"client[-5:]: {client[-5:]}")
print('-' * 60)

for city in cities:
    print(city)
print()

for i, city in enumerate(cities):
    if (i != 0) and ((i % 3) == 0):
        print("====")
    print(i, city)
print()
print(f"list(enumerate(cities)): {list(enumerate(cities))}")


s = "garbanzo"
for char in s:
    print(char)
print()

# for VAR ... in ITERABLE:
#     ...










