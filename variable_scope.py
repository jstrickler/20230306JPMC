
x = 0

boom = 42  # (file-)global variable

def spam():
    x = 95  # local variable
    print(f"boom: {boom}")
    return x

x = spam()

print(f"x: {x}")  # INVALID
print(f"m: {m}")



