import os
import random

os.system("clear")

computerChoice = random.choice(["rock","paper","scissors"])
userChoice = input("Do you want rock, paper or scissors? ")
print("The computer choose: " + computerChoice + ".")

if computerChoice == userChoice:
  print("True")
elif userChoice == "rock" and computerChoice == "scissors":
  print("Win")
elif userChoice == "paper" and computerChoice == "rock":
  print("Win")
elif userChoice == "scissors" and computerChoice == "paper":
  print("Win")
else:
  print("You lose, computer wins :)")
  