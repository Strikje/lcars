class Employee:
  def __init__(self,firstNameValue, lastNameValue, salaryValue):
    self.firstName = firstNameValue
    self.lastName = lastNameValue
    self.salary = salaryValue

  def calculatePaycheck(self):
    return self.salary/52