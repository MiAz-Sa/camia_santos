# INPUTS -
num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))
#CALCULATIONS -
def calculate_sum():

    global num1, num2

    sum = num1 + num2

    print(sum)

def calculate_difference():

    global num1, num2

    difference = num1 - num2

    print(difference)
#DISPLAY OUTPUTS-
calculate_sum()

calculate_difference()
