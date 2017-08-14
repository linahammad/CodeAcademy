#CLASSES
#Overriding methods
######################
#1.Inside ElectricCar add a new method drive_car that changes the car's condition to the string "like new".

#Then, outside of ElectricCar, print the condition of my_car

#Next, drive my_car by calling the drive_car function

#Finally, print the condition of my_car again

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
    
  def display_car (self):
    return "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

  def drive_car (self):
    self.condition = "used"
my_car = Car("DeLorean", "silver", 88)
print my_car.model
print my_car.color
print my_car.mpg
print my_car.condition 
print my_car.drive_car () 
print my_car.condition 


class ElectricCar(Car):
  def __init__(self,battery_type, model, color, mpg ):    
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
 
  def drive_car (self):
    self.condition = "like new"
    
    
my_car = ElectricCar("molten salt","DeLorean", "silver", 88)
print my_car.condition 
print my_car.drive_car () 
print my_car.condition     
    
