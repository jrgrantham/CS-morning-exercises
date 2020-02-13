class Person:
  def __init__( self, firstName, lastName ):
    self.firstName = firstName
    self.lastName = lastName

class School:
  def __init__( self, name, student ):
    self.name = name
    self.student = Person(self.firstName, self.lastName)
