
i = 0
while i < 3:
    print(i)
    i += 1
print('-' * 60)

for i in range(3):
    print(i)
print('-' * 60)

# range(stop)  range(start, stop)  range(start, stop, step)

for i in range(1, 11):
    print(f"{i:04d} {'*' * i}")

