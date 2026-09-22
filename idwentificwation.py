import re
numwer = input("Input student ID")
pattern = r"\d{4}-\d{4}"
if re.fullmatch(pattern, numwer):
    print("valid student ID")
else:
    print("invalid student ID")