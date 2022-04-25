import random
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

images = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if player >= 3 or player < 0: 
    print("You typed an invalid number, you lose!") 
else:

    computer = random.randint(0, 2)
    print(images[player])
    print("Computer chose:")
    print(images[computer])

    if player >= 3 or player < 0: 
        print("You typed an invalid number, you lose!") 
    elif player == 0 and computer == 2:
        print("You win!")
    elif player == 0 and computer == 2:
        print("You lose")
    elif player > computer:
        print("You lose")
    elif player > computer:
        print("You win!")
    elif computer == player:
        print("It's a draw")



