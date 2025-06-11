import random
import os

os.system("clear")

roll = random.randint(1,6)
# print ("The computer rolled a " + str(roll))
guess = int(input("Guess the dice roll: "))

if guess == roll:
  print("Correct! The computer rolled a: " + str(roll) + ".")
else:
  print("Wrong! The computer rolled a: " + str(roll) + ".")
