def add (a,b):
	return a + b

def subtration (a,b):
	return a - b

def multiplication (a,b):
	return a * b

def division (a,b):
	if b == 0:
		return(f"Error: {a} is not divisible by {b}")
	
	return a / b

start = True
while start:
	print ("Simple Calculation")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")

	choice = input("Enter an operator (1 - 4): ")
	num1 = float(input("Enter the first number: "))
	num2 = float(input("Enter the second number: "))
	if choice == "1" or choice == "2" or choice == "3" or choice =="4":
		result = 0
		if choice == "1":
			result = add(num1,num2)
		elif choice == "2":
			result = subtration(num1,num2)
		elif choice == "3":
			result = multiplication(num1,num2)
		elif choice == "4":
			result = division(num1,num2)
		
		print("Result:", result)
		
	else:
		end = input("Do you want to exit the program? (yes/no): ").lower()
		if end == "yes":	
			start = False
			print("Exiting the program")
		if end == "no":
			continue
		else:
			print("Invalid input. Exiting")
			break
		 


