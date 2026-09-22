try:

    pwin = int(input("Enter your 6 digit PIN "))
    if len(pwin) == 6:
        print("Valid PIN...")
    elif len(pwin) !=6:
        print("Invalid PIN...")

except ValueError:
    print("Invalid PIN...")