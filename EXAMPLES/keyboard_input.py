#!/usr/bin/env python

from getpass import getpass

user_name = input("What is your name: ")
quest = input("What is your quest? ")
print("{} seeks {}".format(user_name, quest))

raw_num = input("Enter number: ")  # <1>
num = float(raw_num)  # <2>

print("2 times {} is {}".format(num, 2 * num))

secret = getpass("What is your password? ")
print(f"Your password is {secret} (and not really secret now)")