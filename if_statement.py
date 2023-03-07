value = 81

if value > 75:
    print("wallaby")
    print("wombat")
    if value > 90:
        print("indent 4 spaces -- Guido says so")
elif value > 50:   # else if
    print("kangaroot")
    print("kookaburra")
    print("koala")
else:
    print("mongoose")
    print("mango")

print("ALL DONE")

# if elif else while for with def class try except finally

# if number:
#     0 is False, non-0 is True
# if obj has a length:
#    len(0) is is False, len() non-0 is True

#   A ? B : C

#  B if A else C

DEBUG = True

color = "RED" if DEBUG else "GREEN"

# update_screen("RED" if DEBUG else "GREEN")

#   == != > < >= <=


VERBOSE = False

#  and or not

if DEBUG and VERBOSE:
    print("I have a bad feeling about this")


# if (a > 100) and (b < 35):
#     ...
import os
if not os.path.exists("wombats.txt"):
    print("sorry, no file")




























