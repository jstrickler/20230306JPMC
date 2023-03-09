from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

print(f"knight_data['Galahad']: {knight_data['Galahad']}")
print(f"knight_data['Galahad'][0]: {knight_data['Galahad'][0]}")
print()

for knight, data in knight_data.items():
    print(f"{data[0]:4s} {knight}")

