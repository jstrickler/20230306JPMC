

cities = ['Delaware', 'Dallas', "Washington", "New York",
          "Boston"]

for city in 'Dallas', 'Durham', 'New York', 'Annapolis':
    print(city, city in cities)
print()

s = "J P Morgan Chase"
print(f"'Morgan' in s: {'Morgan' in s}")
print(f"'Spaghetti' in s: {'Spaghetti' in s}")

a = [1, 2, 3]
b = ["4", "5", "6"]
result = a + b
print(f"result: {result}")

print('-' * 60)
print(f"'=*' * 10: {'=*' * 10}")

print(f"'Python ' * 10: {'Python ' * 10}")

flags = [False] * 10
print(f"flags: {flags}")

values = [0] * 25
print(f"values: {values}\n")

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(f"cities: {cities}")
print(f"nums: {nums}")
print()

print(len(cities), min(cities), max(cities), sorted(cities))
print()

print(len(nums), min(nums), max(nums), sorted(nums), sum(nums))
print()

rcities = reversed(cities)
print(f"rcities: {rcities}")
for city in rcities:
    print(city)
print()


for i, city in enumerate(cities):
    print(i, city)
print()
print(f"list(enumerate(cities)): {list(enumerate(cities))}")
print(f"enumerate(cities): {enumerate(cities)}")

enum_cities = enumerate(cities)
print(f"enum_cities: {enum_cities}")
x = list(enum_cities)
print(f"x: {x}")
















