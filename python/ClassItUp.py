#INTRODUCTION TO CLASSES
#Class It Up
########################
#1.Inside the Triangle class:

#Create a variable named number_of_sides and set it equal to 3.
#Create a method named check_angles. The sum of a triangle's three angles should return True if the sum of self.angle1, #self.angle2, and self.angle3 is equal 180, and False otherwise.

class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
    
  def check_angles(self):
    sum = self.angle1 + self.angle2 + self.angle3
    if sum == 180:
      return True
    else:
      return False