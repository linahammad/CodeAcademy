#INTRODUCTION TO BITWISE OPERATORS
#The Man Behind the Bit Mask
##################################
#1.Define a function, check_bit4, with one argument, input, an integer.

#It should check to see if the fourth bit from the right is on.

#If the bit is on, return "on" (not print!)

#If the bit is off, return "off".

#Check the Hint for some examples!

def check_bit4(input):
  mask = 0b1000
  if input & mask > 0:
    return "on"
  else:
    return "off"