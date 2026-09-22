try:
    gwade = int(input("enter your grade (1-100"))
    if gwade >0 and gwade <=100:
       print("your grade valid...")
    elif gwade > 100:
       print("your grade invalid... (More than 100)")
    elif gwade < 0:
       print("your grade invalid... (Less than 0)")

except ValueError:
    print("your grade must be in numeric format...")