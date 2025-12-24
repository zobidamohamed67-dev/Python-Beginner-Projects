import random

game_history = []  # تسجيل نتائج الجولات

# Rock Paper Scissors ASCII Art
rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_ascii = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("\nWelcome to the ROCK, PAPER, SCISSORS game!")

while True:
    # المستخدم يقرر يكمل أو يشوف القواعد
    confirm = input("Press Enter to continue or type (Help) for the rules \n").lower()

    if confirm == "help":
        print("""
        **********RULES**********
        1) YOU CHOOSE AND THE COMPUTER CHOOSES
        2) ROCK SMASHES SCISSORS -> ROCK WIN
        3) SCISSORS CUT PAPER -> SCISSORS WIN
        4) PAPER COVERS ROCK -> PAPER WIN
        """)

    # إدخال اختيار المستخدم
    user_choice = input("Enter your choice (rock, paper, scissors):\n").lower()

    # التحقق من صحة الإدخال
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors")
        continue

    # عرض اختيار المستخدم
    if user_choice == "rock":
        print(f"\nYou chose:\n{rock_ascii}")
    elif user_choice == "paper":
        print(f"\nYou chose:\n{paper_ascii}")
    else:
        print(f"\nYou chose:\n{scissors_ascii}")

    # اختيار الكمبيوتر (عشوائي)
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # عرض اختيار الكمبيوتر
    if computer_choice == "rock":
        print(f"Computer chose:\n{rock_ascii}")
    elif computer_choice == "paper":
        print(f"Computer chose:\n{paper_ascii}")
    else:
        print(f"Computer chose:\n{scissors_ascii}")

    # تحديد الفائز وإضافة النتيجة للتاريخ
    if user_choice == computer_choice:
        print("It's a tie!")
        game_history.append("Tie")
    
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print(f"YOU WIN! {user_choice} beats {computer_choice}")
        game_history.append("Win")
        
    else:
        print(f"YOU LOSE! {computer_choice} beats {user_choice}")
        print("GAME OVER!!!!!")
        game_history.append("Lose")

    # سؤال المستخدم لو يحب يلعب تاني
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nYour game history:")
        print(game_history)
        print("Thanks for playing!")
        break
