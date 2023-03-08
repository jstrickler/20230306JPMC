

person = "Bill", "Gates", "Microsoft", "1955-10-24"
# person = ("Bill", "Gates", "Microsoft", "1955-10-24")

print(f"person: {person}")
print(f"person[0]: {person[0]}")
print(f"person[-1]: {person[-1]}")

# iterable unpacking
first_name, last_name, product, dob = person
print(first_name, last_name)
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'NeXT', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
    ('Millard', 'Fillmore', '1842'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
]

for first_name, last_name, *product, dob in people:
    #  first_name, last_name, product, dob = next_element
    print(first_name, last_name, product, dob)
print()

print(f"people[-1]: {people[-1]}")
print(f"people[-1][1]: {people[-1][1]}")
print(f"people[-1][1][3]: {people[-1][1][3]}")
print('-' * 60)

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print()

for color in 'green', 'red', 'purple':
    print(color)
print()

a = 'wombat'
b = 'pangolin'
c = 'meercat'

for animal in a, b, c:
    print(animal)
print()






