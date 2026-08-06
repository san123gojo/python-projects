import random

emojis={'r':'🗿','p':'📄','s':'✂️'}
choices=('r','p','s')

while True:
 user_choice=input("Enter your choice (r/p/s):").lower()
 if user_choice not in choices:
    print("Invalid choice!")
    continue

 computer_choice=random.choice(choices)

 print(f"You chose {emojis[user_choice]}")
 print(f"computer chose {emojis[computer_choice]}")

 if user_choice == computer_choice:
    print("It's a tie!")#\tells the interpretor its a multi line statement
 elif (user_choice == 'r' and computer_choice == 's') or \
     (user_choice == 'p' and computer_choice == 'r') or \
     (user_choice == 's' and computer_choice == 'p'):
    print("You win!")
 else:
    print("Computer wins!")

 should_continue=input("Do you want to play again? (y/n):").lower()
 if should_continue=='n':
   break