import random

num=random.randint(1,20)

for i in range(5):
    try:
        guess = int(input("Please enter a whole number between 1-20: "))
        
    except ValueError:
        print("That is not a valid integer. Try again.")
        continue

    if num== guess:
        print("Congratulations You guessed Right")
        break
    elif num > guess:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    
    if i==4:
        print("\nSorry you have used all your chances. The number was", num)