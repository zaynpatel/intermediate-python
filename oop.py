class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  
  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, number):
    self.numberOfStudents = number
  
  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students '

test = School("Zayn", 5, 20)
#print(test)
#print(test.get_name())
#print(test.get_level())
test.set_numberOfStudents(500)
#print(test.get_numberOfStudents)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def set_pickupPolicy(self, policy):
    self.pickupPolicy = policy
  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    # set a variable to override root repr constructor
    parentRepr = super().__repr__()
    return parentRepr + "has a pickup policy of {policy}".format(policy = self.pickupPolicy)

test_two = PrimarySchool("Zayn", 500, "after 4 pm.")
#print(test_two)

test_two.set_pickupPolicy("pickup at 5 pm")
#print(test_two.get_pickupPolicy)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self.sportsTeams
  """
  def __repr__(self):
    sportsRepr = super().__repr__()
    return sportsRepr + "has {self.sportsTeams}"

test_three = HighSchool("Zayn", 50, ['Tennis', 'Soccer'])
print(test_three.get_sportsTeams())
print(test_three)
"""
