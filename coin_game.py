import random

print("Welcome to the coin guessing game!")

# 1. Choose method
choice = input("Choose a method to toss the coin:\n 1. Using random.random()\n 2. Using random.randint()\n ")

if choice == "1":
    user_choice = input("Choose a side HEAD OR TAILS\n").upper()
    num = random.random()
    
    if num < 0.5:
        coin_choice = "HEAD"
    else:
        coin_choice = "TAILS"
        
    if user_choice == coin_choice:
        print("You win")
    else:
        print("You lose, please try again")
        print("The answer is:", coin_choice)

elif choice == "2":
    num = random.randint(0, 1)
    if num == 0:
        coin_choice = "HEAD"
    else:
        coin_choice = "TAILS"
        
    user_choice = input("Choose a side HEAD OR TAILS\n").upper()
    
    if user_choice == coin_choice:
        print("You win")
    else:
        print("You lose, please try again")
        print("The answer is:", coin_choice)

else:
    print("Invalid choice!")
