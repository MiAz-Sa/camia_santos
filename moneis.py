vawid_inpwuts = ["cash", "gcash", "card"]
check = print(input("Select payment method. (cash, gcash, card)"))
if check in vawid_inpwuts:
    print("Payment method is valid")
else:
    print("Payment method is not valid")