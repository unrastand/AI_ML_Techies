

def Calculator(num1,num2,operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."

    return f"The result of {num1} {operator} {num2} is: {result}"


def checkEven(num):
    if num/2 ==0:
        return True
    else:
        return False
    

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

result = Calculator(num1, num2, operator)
print(result)

num=int(input("Enter a number to check if it's even: "))
is_even = checkEven(num)
print(f"The number {num} is even: {is_even}")   