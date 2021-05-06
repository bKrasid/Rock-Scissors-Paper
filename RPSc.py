#Rock Paper Scissors

#The rules are simple:

#Paper wins over rock
#Rock wins over scissors
#Scissors win over paper

#Have your program generate a random answer 
#for the computer – but don’t display it. 
#Then, ask the player for their answer.

import random
from random import choice

Attack = input("Rock Paper Scissors: ")
cpu_choice = choice(('Rock', 'Paper', 'Scissors'))
print(cpu_choice)
computer = cpu_choice
if cpu_choice == Attack:
    print("It is a tie!")
elif (Attack == 'Rock'):
    if (computer == 'Papper'):
        print("CPU wins!")
elif (Attack == 'Papper'):
    if (computer == 'Scissors'):
        print("CPU wins!")
elif (Attack == 'Scissors'):
    if (computer == 'Rock'):
        print("CPU wins!")
elif (Attack == 'Rock'):
    if (computer == 'Scissors'):
        print("User wins!")
elif (Attack == 'Scissors'):
    if (computer == 'Paper'):
        print("User wins!")
elif (Attack == 'Paper'):
    if (computer == 'Rock'):
        print("User wins!")
