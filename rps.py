rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
a = 0
a = random.randint(0,2)
if user_choice == 0:
    print(rock)
    if a == 0:
        print(f"Computer chose:\n{rock}\nIt's a draw!")
    elif a == 1:
        print(f"Computer chose:\n{paper}\nYou Lose!")
    else:
        print(f"Computer chose: {scissors}\nYou Win!")

if user_choice == 1:
    print(paper)
    if a == 0:
        print(f"Computer chose:\n{rock}\nYou win!")
    elif a == 1:
        print(f"Computer chose:\n{paper}\nIt's a draw!")
    else:
        print(f"Computer chose: {scissors}\nYou lose!")
        
if user_choice == 2:
    print(scissors)
    if a == 0:
        print(f"Computer chose:\n{rock}\nYou lose!")
    elif a == 1:
        print(f"Computer chose:\n{paper}\nYou win!")
    else:
        print(f"Computer chose: {scissors}\nIt's a draw!")