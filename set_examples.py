with open('DATA/breakfast.txt') as breakfast_in:
    foods = breakfast_in.read().splitlines()
    unique_foods = set(foods)
    print(f"foods: {foods}")
    print(f"unique_foods: {unique_foods}")
print('-' * 60)

jose_countries = ['Guatemala', 'Bulgaria', 'China', 'Argentina', 'India', 'Angola', 'Equador']
miriam_countries = ['Japan', 'Bulgaria', 'Bulgaria', 'Equador',
                    'Burkina Faso', 'Philippines', 'China', 'India']

jose = set(jose_countries)
mir = set(miriam_countries)
jose.add('Canada')

print("COMMON:", jose & mir)  # intersection
print("NOT COMMON:", jose ^ mir)  # xor
print("ALL:", jose | mir)  # union
print("ONLY JOSE:", jose - mir)
print("ONLY MIRIAM:", mir - jose)



