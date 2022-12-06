from roster import student_roster
import itertools

class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def _sort_alphabetically(self, students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

# sort names alphabetically
x = ClassroomOrganizer()
#print(x.sorted_names)
#x_iter = iter(x.sorted_names)
#for i in range(10):
  #print(next(x_iter))

# combinations of students sitting together
#y = itertools.combinations(x.sorted_names, 2)
#print(y)
#for combos in y:
  #print(combos)
#[print(combos) for combos in y]

math_science_quads = x.get_students_with_subject("Math") + x.get_students_with_subject("Science")

print(list(itertools.combinations(math_science_quads, 4)))
