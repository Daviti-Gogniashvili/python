class Students:
  def __init__(self, name, surname, age, average_point):
    self.name = name
    self.surname = surname
    self.age = age
    self.average_point = average_point


  def GPA(self):
    if self.average_point > 92:
      print(self.name,self.surname,": GPA is A")
    else:
      print(self.name,self.surname,": GPA isn't A")



student1 = Students("david", "gogniasvhili", "18", 95)
Students.GPA(student1)

student2 = Students("daniel", "desuza", "21", 89)
Students.GPA(student2)
