print("Welcome to the Treasure Island Game 🏝️")
print("Your mission is to find the treasure.")

door = input("You're at a crossroad. Where do you want to go? Type 'red' or 'blue'\n").lower()

if door == "blue":
    print("You entered a room of crocodiles. 🐊")
    print("GAME OVER")

elif door == "red":
    print("You found three boxes: 'White', 'Black', and 'Green'. 📦")
    box = input("Which box would you like to open? \n").lower()

    if box == "white":
        print("You found a box full of snacks! But they were poisoned. ☠️")
        print("GAME OVER")
    elif box == "black":
        print("You found a box full of spiders! 🕷️")
        print("GAME OVER")
    elif box == "green":
        print("🎉 CONGRATULATIONS! YOU FOUND THE TREASURE! 💰")
        print("YOU WON!")
    else:
        print("Invalid choice. You found nothing.")
        print("GAME OVER")

else:
    print("Invalid choice. You fell into a hole.")
    print("GAME OVER")
