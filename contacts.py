contacts = {
  "number" : 4
  ,"students" :
    [
      {"name":"Sarah Holderness", "email":"sara@example.com"}
      ,{"name":"Harry Potter","email":"harry@example.com"}
      ,{"name":"Hermoine Granger","email":"hermoine@example.com"}
      ,{"name":"Ron Weasley","email":"ron@example.com"}
    ]
}

print("Student information:")
for student in contacts["students"]:
  print(student["email"])