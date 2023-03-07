import sys

print(f"sys.argv: {sys.argv}")

print(f"sys.argv[0]: {sys.argv[0]}")   # script name
print(f"sys.argv[1]: {sys.argv[1]}")   # 1st param
#                     sys.argv[2]      # 2nd param etc

file_to_process = sys.argv[1]   
print(f"file_to_process: {file_to_process}")