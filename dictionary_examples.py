d1 = dict()
print(f"d1: {d1}")
print(f"type(d1): {type(d1)}")
capitals = {
    'NC': 'Raleigh',
    'TX': 'Austin',
    'OH': 'Columbus',
    'DE': 'Dover',
    'OH': 'Dayton',
}
print(f"capitals: {capitals}")
print(f"capitals['OH']: {capitals['OH']}")

capitals["NJ"] = "Trenton"
capitals['WI'] = "Madison"
print(f"capitals: {capitals}")

capitals['OH'] = "Dayton"
print(f"capitals: {capitals}")

# dict of lists
# dict of tuples
# dict of strings
# list of dicts
# list of tuples
# list of strings
# dict of lists of tuples of tuples of strings

print(f"capitals['NC']: {capitals['NC']}")
#print(f"capitals['ME']: {capitals['ME']}")
print(f"capitals.get('ME'): {capitals.get('ME')}")
print(f"capitals.get('NJ'): {capitals.get('NJ')}")
print(f"capitals.get('ME', 'not found'): {capitals.get('ME', 'not found')}")

cap = capitals.setdefault('ME', 'August')
print(f"cap: {cap}")
print(f"capitals: {capitals}")








