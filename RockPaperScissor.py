import random
user_wins = 0
comp_wins = 0
option = ["rock", "paper", "scissor"]
print("Welcome to the Rock Paper Scissor Game!")
print("You have to choose between Rock, Paper and Scissor.")

while True:
     user_choice= input("Enter your choice: rock/paper/scissor, or press Q to quit ").lower()
     if user_choice == "q":
         break
     if user_choice not in option:
          print("Invalid choice. Please try again.")
          continue
     random_number = random.randint(0, 2)
     comp_choice = option[random_number]
     print("Computer chose " + comp_choice + ".")
#from the option list, we can see index 0 is rock, 1 is paper and 2 is scissor    
     if user_choice == comp_choice:
        print("It's a tie!")
        user_wins += 1
        comp_wins += 1
     elif user_choice == "rock" and comp_choice == "scissor":
        print("You win!")
        comp_wins += 1
     elif user_choice == "paper" and comp_choice == "rock":
        print("You win!")
        user_wins += 1
     elif user_choice == "scissor" and comp_choice == "paper":
        print("You win!")
        user_wins += 1
     else:
        print("Computer wins!")
        comp_wins += 1  
            
print("You won " + str(user_wins) + " times.")
print("Computer won " + str(comp_wins) + " times.")
print("Good bye!")

