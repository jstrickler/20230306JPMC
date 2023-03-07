i = 0
while i < 3:
    print(i)
    i += 1
print("done")

while True:
    name = input("Enter your name (q to quit): ")
    if name == 'q':
        break  # exit loop
    if name == '':
        print("please enter a name")
        continue # go to top
    print(f"Welcome, {name}")


