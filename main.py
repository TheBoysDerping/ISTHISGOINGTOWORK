import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
guess=0
tries = 1
print("What is your name")
name = input()
print ('Hi, %s.' % name)
print(f'Whats going on, {name}')
input()
print("Thats good")
print("Would you like to play a game?")
input()
print("Well to bad, your playing it anyway!")
the_number = random.randint(1, 20)
print("What number am i thinking of? Its between 1 and 20")
while guess != the_number and tries != 5:
	if tries != 1:
		if guess > the_number:
			print("Lower...")
		else:
			print("Higher...")
	guess = int(input(f'Take guess number {tries}:'))
	print ("")
	tries += 1
if guess != the_number: 

	print(f'You ran out of tries! The number was {the_number}.')
else:
	tries -= 1
	print(f'You guessed it! The number was {the_number}.')
	print("And it only took you", tries, "tries!")

spin_number = random.randint(1,6)
print("Well now that that is done, Lets do a little something")
print("Hit Enter To spin the Wheel!")
input()
print("spining wheel")
print("")
if spin_number == 1:
	print("Great, now i have to jump off a cliff, great, just great")
if spin_number == 2:
	print(f'Screw you {name}')
if spin_number == 3:
	print(f'Go die in a hole {name}')
if spin_number == 4:
	print("You won! Well actually you didnt, i just wanted to say that, nothing happened")
if spin_number == 5:
	print("Oh F***. You actually Won this time... Well, time to die... (X_X)")
if spin_number == 6:
	print("Well that was a bust, There was nothing on the section it landed on.")
	