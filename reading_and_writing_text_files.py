
file_name = "DATA/mary.txt"

file_obj = open(file_name)
# read file ...
file_obj.close()

with open(file_name, "r") as mary_in:
    print(f"mary_in: {mary_in}")
    
    for raw_line in mary_in:   # mary_in.readline()
        line = raw_line.rstrip()  # remove trailing \n and other space
        print(line)
print('-' * 60)

with open(file_name) as mary_in:
    entire_file = mary_in.read()  # read entire file into 1 string
    print("Entire file:")
    print(entire_file)
    print("=" * 20)
    print("Raw view:")
    print(repr(entire_file))
print('-' * 60)

with open(file_name) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(file_name) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)

with open('DATA/breakfast.txt') as breakfast_in:
    foods = breakfast_in.read().splitlines()
    print(f"foods: {foods}")
print()

unique_foods = set(foods)
print(unique_foods)
print('-' * 60)

min_length = 20
count = 0
with open("DATA/words.txt") as words_in:
    with open("big_words.txt", "w") as words_out:
        for raw_word in words_in:  # loop over all 173K words
            word = raw_word.rstrip()
            if len(word) >= min_length:
                count += 1
                print(word)
                words_out.write(raw_word)

print(f"There were {count} words of length {min_length} or longer")
print()

with open("DATA/parrot.txt") as parrot_in:
    for i, raw_line in enumerate(parrot_in, 1):
        if 7 <= i <= 9:
            print(raw_line.rstrip())
print('-' * 60)

lines_wanted = 4, 7, 11
with open("DATA/parrot.txt") as parrot_in:
    for line_number, raw_line in enumerate(parrot_in, 1):
        if line_number in lines_wanted:
            print(raw_line.rstrip())

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

output_path = "c:/Users/student/Desktop/py3jpmcint4half-AM/fruits.txt"
with open(output_path, "w") as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')
        #  fruits_out.write(f"{fruit}\n")

more_fruits = ['jackfruit', 'durian', 'mangosteen']
with open(output_path, "a") as fruits_out:
    for fruit in more_fruits:
        fruits_out.write(fruit + '\n')

# with open(output_path, "x") as fruits_out:
#     fruits_out.write("mango\n")

