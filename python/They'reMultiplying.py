#INTRODUCTION TO CLASSES
#They're Multiplying!
########################
#1.After line 3, add a second member variable called health that contains the string "good".

#Then, create two new Animals: sloth and ocelot. (Give them whatever names and ages you like.)

#Finally, on three separate lines, print out the health of your hippo, sloth, and ocelot.

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age
    
hippo = Animal("Jeff", 2)
hippo.description()   

sloth = Animal("aa",5)
ocelot = Animal("bb",12)
print hippo.health
print sloth.health 
print ocelot.health 