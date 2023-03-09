import sqlite3

file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        for raw_line in file_in:
            print(raw_line.rstrip())
except FileNotFoundError as err:  # AKA catch
    # print or log error, etc
    print(err)

nums = [0, 800, 80, 1000, 32, 255, 0.0, 400, 5, "123", 5000]

for num in nums:
    try:
        result = 10000 / num
    except (TypeError, ZeroDivisionError) as err:
        print(err)
    except ValueError as err:
        print(err) # or log, whatever...
    else:
        print(result)

print("ALL DONE")

try:
    conn = None
    conn = sqlite3('wombats.db')
    cursor = conn.cursor()
except sqlite3.Error as err:
    print(err)
finally:
    if conn:
        conn.close()

try:
    with sqlite3('pigeons.db') as conn:
        cursor = conn.cursor()
        # blah blah
except sqlite3.Error as err:
    print(err)






