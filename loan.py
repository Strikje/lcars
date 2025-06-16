# Get details of loan
moneyOwed = float(input("How much money is owed in dollars? ")) # 50000
annualPercentageRate = float(input("How much interest is it annually? ")) # 3
payment = float(input("How much in the payment in dollars? ")) # 1000
months = int(input("How many month's do you want to see for? ")) # 24

monthlyRate = annualPercentageRate / 100 /12 

for i in range(months):
  # Calculate the monthly payment
  interestPaid = moneyOwed * monthlyRate

  # Add in interest
  moneyOwed = moneyOwed + interestPaid

  if (moneyOwed - payment < 0):
    print("The last payment is: ", moneyOwed)
    print("You paid of the load in", i + 1, "months")
    break
  
  # Make payment
  moneyOwed = moneyOwed - payment

  print("Paid", round(payment,2),"of wich was", round(interestPaid,2), "interest.", end = ' ')
  print("Now I owe", round(moneyOwed,2))
