import random

while True:

    # Display instructions
    print("")
    print("The rules of the game below:")
    print("Paper beats rock, rock beats scissors, scissors beats paper.")
    print("")

    # Select player
    print("1)Rock")
    print("2)Paper")
    print("3)Scissors")
    print("")
    player = input("Please select from the list: ").lower()
    print("")

    # Determine player
    if player == "1" or player == "Rock" or player == "rock":
        print("You have selected rock!")
        print("")
        break
    elif player == "2" or player == "Paper" or player == "paper":
        print("You have selected paper!")
        print("")
        break
    elif player == "3" or player == "Scissors" or player == "scissors":
        print("You have selected scissors!")
        print("")
        break
    else:
        player = input("That is an invalid choice, try again: ")
        print("")
        

while True:
    print("")
    # Computer choice
    computer = ["Rock", "Paper", "Scissors"]
    computer_choice = (random.choice(computer)).lower()

    print("Computer has choosen: " + computer_choice + "!")
    print("")

    # Determine winner
    if computer_choice == player:
        print("It's a tie!")
        print("")
    elif computer_choice == "rock": 
        if player == "paper":
            print("You win!")
            print("")
        else: 
            print("You lose!") 
    elif computer_choice == "paper": 
        if player == "scissors":
            print("You win!")
            print("")
        else: 
            print("You lose!") 
            print("")
    elif computer_choice == "scissors": 
        if player == "rock":
            print("You win!")
            print("")
        else: 
            print("You lose!")   
            print("")
    
    # Play game again?
    again = input("Play again? (Y/N): ")
    if again == "y" or again == "Y" or again == "Yes" or again == "yes":
        player = input("Please select from the list: ").lower()
    elif again.lower() != "y":
        break

  
    
        