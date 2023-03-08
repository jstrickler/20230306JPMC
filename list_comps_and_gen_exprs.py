
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    new_item = f.upper()
    f0.append(new_item)
print(f"f0: {f0}\n")

#    [new_item for var in iterable if condition]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

x = ['alpha', "bravo", "charlie's angels"]
print(f"x: {x}")

f3 = [f for f in fruits if f.startswith('p')]
print(f"f3: {f3}\n")

# implied 'and'
f4 = [f.upper() for f in fruits if f.startswith('p') if len(f) > 5]
print(f"f4: {f4}\n")

f5 = [f.upper() for f in fruits if (f.startswith('p') or len(f) > 5)]
print(f"f5: {f5}\n")

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
n1 = [round(n / 23, 3) for n in nums if n > 300]
print(f"n1: {n1}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[3] for p in people]
print(f"dobs: {dobs}\n")

old_guys = [(p[0], p[1]) for p in people if p[3] < "1970"]
print(f"old_guys: {old_guys}\n")

old_guys = [p[:2] for p in people if p[3] < "1970"]
print(f"old_guys: {old_guys}\n")

fruits_gen = (f.upper() for f in fruits)
print(f"fruits_gen: {fruits_gen}\n")

for fruit in fruits_gen:
    print(fruit)


dob_gen = (p[3] for p in people)
print(f"dob_gen: {dob_gen}\n")
for dob in dob_gen:
    print(dob)

i_am_not_a_generator = (len(f) for f in fruits)
print(f"i_am_not_a_generator: {i_am_not_a_generator}")

