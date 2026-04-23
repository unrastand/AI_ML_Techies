#creating function
def add(num1, num2):
    print(num1 + num2)

# add(7, 10)

# print(f"the sum of the two numbers is {add(7,10)} ")

def substract(num1, num2):
    return num1-num2

answer = substract(num1=10, num2=7, num3=9)

# print(f"the difference of the two numbers is {answer} ")

#arbituary arguments - works based on position of the argument

def addition(*args):
    sum = 0
    for numbers in args:
        sum += numbers
    return sum

answer = addition(2,4,6,6,7,2,4,5,7,8,9,3,2,2,45,4,4,5)

# print(f"the sum of the numbers is {answer} ")

#keyword arguments - works based on the name of the argument

def division (**kwargs): 
    num1 = kwargs["num1"]
    num2 = kwargs["num2"]
    print(f"first number {num1}, second number {num2}")

division(num1=8, num2=6, num3=8)