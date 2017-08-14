#LOOPS
########
#1.Use a while loop to let the user keep guessing so long as guesses_left is greater than zero.

#Ask the user for their guess, just like the second example above.

#If they guess correctly, print "You win!" and break.

#Decrement guesses_left by one.

#Use an else: case after your while loop to print "You lose.".


from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose."