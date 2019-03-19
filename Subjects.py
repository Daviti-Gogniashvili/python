class Subjects:
  def __init__(self, student_name, subject_name, subject_credit, summed_points):
    self.student_name = student_name
    self.subject_name = subject_name
    self.subject_credit = subject_credit
    self.summed_points = summed_points

  def check_subject_credits(self):
    print("subject: {}, credits: {}".format(self.subject_name, self.subject_credit))

  def subject_pass(self):
    if self.summed_points >= 51:
      print("{} passed the exam with {} points".format(self.student_name, self.summed_points))
    else:
      print(self.student_name,"didn't passed exam")

studying1 = Subjects("elene", "management", 4, 89)
Subjects.check_subject_credits(studying1)
Subjects.subject_pass(studying1)

studying2 = Subjects("gigi", "math", 4, 49)
Subjects.check_subject_credits(studying2)
Subjects.subject_pass(studying2)
