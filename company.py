from employee import Employee

class Company:
  def __init__(self):
    self.employees = []

  def addEmployee(self, newEmployee):
    self.employees.append(newEmployee)

  def  displayEmployee(self):
    print("Current Eployees:")
    for i in self.employees:
      print(i.firstName, i.lastName)
    print("-----------------------")

def main():
  myCompany = Company()

  employee1 = Employee("Sarah", "Hess", 50000)
  myCompany.addEmployee(employee1)
  employee2 = Employee("Lee", "Smith", 25000)
  myCompany.addEmployee(employee2)
  employee3 = Employee("Bob", "Brown", 60000)
  myCompany.addEmployee(employee3)

  myCompany.displayEmployee()

main()