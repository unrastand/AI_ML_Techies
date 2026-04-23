list_a=["a","b","c","d","e "] #can be changed

tuple_fruits=("apple","banana","mango") #cannot be changed
set_names={"Alice","Bob","Charlie","Alice"}
print(set_names)# {'Alice', 'Bob', 'Charlie'}  not allowing duplicate
dict_info={"name":"Mary","age":30,"city":"Lagos"} #key value pairs can be accesd with key

#improved guessing game
import random

num=random.randint(1,20)
guess_list=[]
for i in range(5):
    try:
        guess = int(input("Please enter a whole number between 1-20: "))
        guess_list.append(guess)
        
    except ValueError:
        print("That is not a valid integer. Try again.")
        continue

    if num== guess:
        print("\n Congratulations You guessed Right\n")
        break
    elif num > guess:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    
    if i==4:
        print("\nSorry you have used all your chances. The number was", num,"\n")

print("\n Your guesses were:", guess_list,"\n")