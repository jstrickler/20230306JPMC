s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"Guido\n"
print(len(s1), len(s2))
print(s5)

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")

query = """
    select *
    from secret_account
    where id is "wombat"
"""

path = r"C:\Users\jstrick\numbers.txt"
path = "C:/Users/jstrick/numbers.txt"


