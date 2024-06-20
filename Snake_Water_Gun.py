# A Digital Snake_Water_Gun game 

import random

def Snake_Water_Gun(name="User"):
    # Snake: 1
    # Water: -1
    # Gun: 0

    '''
    Snake Drinks Water (Snake Wins)
    Water Douses Gun (Water Wins)
    Gun Shoots Snake (Gun Wins)
    '''
    print("Basic terms:\n", Snake_Water_Gun.__doc__)

def start(name="User"):
    Comp_Guess = random.choice([1, -1, 0])
    My_Guess = input("Enter Snake, Water or Gun (S/W/G): ").upper()
    My_Scorecard = {1: "S", -1: "W", 0: "G"}
    Rand_Scorecard = {"S": 1, "W": -1, "G": 0}
    
    if My_Guess not in Rand_Scorecard:
        print("Invalid input. Please enter S, W, or G.")
        return 0
    
    if Rand_Scorecard[My_Guess] == Comp_Guess:
        print(f"Computer chose {My_Scorecard[Comp_Guess]} and You chose {My_Guess}")
        print("Draw ;)")
        return 0
    else:
        if Rand_Scorecard[My_Guess] == -1 and Comp_Guess == 1:
            print(f"Computer chose {My_Scorecard[Comp_Guess]} and You chose {My_Guess}")
            print("You lose the turn! :(")
            return -1
        elif Rand_Scorecard[My_Guess] == -1 and Comp_Guess == 0:
            print(f"Computer chose {My_Scorecard[Comp_Guess]} and You chose {My_Guess}")
            print("You Win the turn! :)")
            return 1
        elif Rand_Scorecard[My_Guess] == 1 and Comp_Guess == -1:
            print(f"Computer chose {My_Scorecard[Comp_Guess]} and You chose {My_Guess}")
            print("You Win the turn! :)")
            return 1
        elif Rand_Scorecard[My_Guess] == 1 and Comp_Guess == 0:
            print(f"Computer chose {My_Scorecard[Comp_Guess]} and You chose {My_Guess}")
            print("You lose the turn! :(")
            return -1
        elif Rand_Scorecard[My_Guess] == 0 and Comp_Guess == 1:
            print(f"Computer chose {My_Scorecard[Comp_Guess]} and You chose {My_Guess}")
            print("You Win the turn! :)")
            return 1
        elif Rand_Scorecard[My_Guess] == 0 and Comp_Guess == -1:
            print(f"Computer chose {My_Scorecard[Comp_Guess]} and You chose {My_Guess}")
            print("You lose the turn! :(")
            return -1
        else:
            print("Error! Try Again")
            return 0

name = input("Enter your name: ")
Snake_Water_Gun(name)
My_score = 0
Comp_score = 0

while True:
    choice_play = int(input("Enter 1 to Resume and 2 to Stop: "))
    if choice_play == 1:
        result = start(name)
        if result == 1:
            My_score += 1
        elif result == -1:
            Comp_score += 1
    elif choice_play == 2:
        print(f"Final score! \n\tYour score: {My_score} \n\tComputer score: {Comp_score}")
        if My_score > Comp_score:
            print(f"Bravo! {name} won !!")
        elif Comp_score > My_score:
            print("Better luck next time!\n\tComputer wins!!")
        else:
            print("Draw!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
