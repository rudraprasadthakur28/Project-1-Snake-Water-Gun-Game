import random
'''
1 for snake
0 for gun
-1 for water

'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ").lower()
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

#By now we have two (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("It's a Draw")

else:
    '''
    if (computer == 1 and you == 0): (computer - you ) = -2
        print("You Win!")

    elif (computer == 1 and you == -1): (computer  - you ) = 2
        print("You Lose!")

    elif (computer == -1 and you == 0): (computer - you) = -1
        print("You Lose!")

    elif (computer == -1 and you == 1): (computer - you) = -2
        print("You Win!")

    elif (computer == 0 and you == 1): (computer - you) = -1
        print("You Lose!")

    elif (computer == 0 and you == -1): (computer - you) = 1
        print("You Win!")

    else:
        print("Something went wrong!")

    The below logic is written on the basis of the value of computer - you

        '''
    if((computer - you) == -1 or (computer - you) == 2):
        print("You Lose!")
    else:
        print("You Win!")