expenses = [10.5,8,5,15,20,5,3]
som = 0
for expense in expenses:
  som = som + expense

print ("You spent $", som, sep = '')

total = sum(expenses)

print ("You spent $", total, sep = '')

total = 0
expenses = []
numberExpenses = int(input("Number of expenses: "))
for i in range(numberExpenses):
  expenses.append(float(input("Enter an expense: ")))
total = sum(expenses)
print("You spent:", total, sep = '')