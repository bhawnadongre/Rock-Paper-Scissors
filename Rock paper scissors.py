import random
print("Welcome to Rock Paper Scissors Game")
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
Choice=[rock,paper,scissors]
choice_name=["Rock","Paper","Scissors"]
Users_choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print(Choice[Users_choice])
print(choice_name[Users_choice])
if(Users_choice <0 or Users_choice>2):  
    print("Invalid Choice")
else:
    Computer_choice=random.randint(0,2)
    print(Choice[Computer_choice])
    print(choice_name[Computer_choice])
    print()
    if(Computer_choice==Users_choice):
        print("Draw!")
    elif(Computer_choice==0 and Users_choice==2):
        print("You Loose!")
    elif(Computer_choice==2 and Users_choice==0):
        print("You Win!")
    elif(Computer_choice>Users_choice):
        print("You Loose!")
    elif(Users_choice>Computer_choice):
        print("You Win!")
    
