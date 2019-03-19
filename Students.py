class Students:
  def __init__(self, name, surname, age, credits, subject1):
    self.name = name
    self.surname = surname
    self.age = age
    self.credits = credits
    self.subject1 = subject1

  def names(self):
    print("hi my name is {}".format(self.name))

  def bachelor(self):
    if self.credits >= 240:
      print("Student {} successfully became bachelor".format(self.name))
      print(self.name,"was studying",self.subject1)
    else:
      print("Student {} didn't succeed becoming bachelor")
      

  
student1 = Students("mari", "avazashvili", 22, 255, "math")
Students.names(student1)
Students.bachelor(student1)

student2 = Students("gio", "imerlishvili", 23, 270, "chemistry")
Students.names(student2)
Students.bachelor(student2)
