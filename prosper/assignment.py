# Generate a hidden number between 1 and 20
secret_number = 7

while True:
 min_attempt= 0
 max_attempt= 5

 print("Welcome To Number Guessing Game")
 print("Guess the Secret number 1 - 20 correctly and win a price")
 print(f"You have a total of {max_attempt} attempts. Goodluck...!\n")
 print("Clue: the secret number is a prime number.\n")

 guesses = []
 while min_attempt < max_attempt:
  guess_num= int(input("Enter a number: "))
  guesses.append(guess_num)
  min_attempt +=1
  
  
  if guess_num == secret_number:
   print("Correct...! You got the number correctly.")
   break
  elif guess_num > secret_number:
   print("Too High")
  else:
   print("Too Low")

  print(f"You have {max_attempt - min_attempt} attempt(s) left.\n")

 if min_attempt==max_attempt:
  print("Game over...! You have used up your chances.\n")

 print("Numbers guessed are: ", guesses)

 # To continue the game
 choice=input("Do you want to continue? (Yes or No): ").capitalize()
 if choice == "No":
  print("Thanks for playing")
  break
 elif choice == "Yes":
  continue
 else:
  print("Invalid entry")
  break
