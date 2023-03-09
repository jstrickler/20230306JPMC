
def get_message():
    return "Hello, JPMC world"

m = get_message()
print(f"get_message(): {get_message()}")

def greet():
    m = get_message()
    print(m)

greet()

def hello(whom='world'):
    print(f"Hello, {whom}")

hello('world')
hello('Mom')
hello('Sailor')
hello()

def search_files(search_term, *file_paths):
    print(f"file_paths: {file_paths}")

    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    line = raw_line.rstrip()
                    print(line)

search_files('rabbit', 'DATA/alice.txt', 'DATA/words.txt')
print('-' * 60)
search_files('rabbit', 'DATA/alice.txt')
print('-' * 60)
search_files('rabbit')




