#INTRODUCTION TO BITWISE OPERATORS
#Turn It On
##################################
#1.In the editor is a variable, a. Use a bitmask and the value a in order to achieve a result where the third bit from the right #of a is turned on. Be sure to print your answer as a bin() string!

a = 0b10111011
mask = 0b100

print bin(a | mask)