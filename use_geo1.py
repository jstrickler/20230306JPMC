import sys

# from pkg.pkg import module
# find alpha/mathlib/geometry.py
from alpha.mathlib import geometry


# import geometry  INVALID

area = geometry.circle_area(10)
print(f"area: {area}")

x = geometry.rectangle_area(8, 13)
print(f"x: {x}")

# sys.path come from
# 1. current folder
# 2. folders in PYTHONPATH (if it exists)
# 3. Predefined folders in sys.prefix

for path in sys.path:
    print(path)


