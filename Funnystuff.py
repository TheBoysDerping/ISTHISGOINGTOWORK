#hit run to activate program



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
print("Would you like to play a game? Answer Yes or No")
yn = input()
if yn == "Yes":
	print("Ok Good.")
if yn == "yes":
	print("Ok Good.")
if yn == "No":
	print("Well to bad, your playing it anyway!")
if yn == "no":
	print("Well to bad, your playing it anyway!")
else:
	print("?")
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

spin_number = random.randint(1,11)
print("Well now that that is done, Lets do a little something")
print("Hit Enter To spin the Wheel!")
input()
print("spining wheel")
print("")
if spin_number == 1:
	print("Great, now i have to jump off a cliff, great, just great")
if spin_number == 2:
	print(f'Fuck you {name}')
if spin_number == 3:
	print(f'Go die in a hole {name}')
if spin_number == 4:
	print("You won! Well actually you didnt, i just wanted to say that, nothing happened")
if spin_number == 5:
	print("Oh Shoot. You actually Won this time... Well, time to die... (X_X)")
if spin_number == 6:
	print("Well that was a bust, There was nothing on the section it landed on.")
if spin_number == 7:
	print("GIVE ME YOUR WALLET!")
if spin_number == 8:
	print("Well, Now you have Covid-19. I gave it to you")
if spin_number == 9:
	print("Ok then, Climate change has increased")
if spin_number == 10:
	print("DIE PEASANT!")
	print("(X.X)")
print("Press enter to laugh")
input()
print("HAHAHAHAHAHAHAHAHA")
print()
print("well i am never doing that again... well, unless you run this program again, which means i have to")
print()
print("Press enter for an insult")
input()
insultnum=random.randint(1,5)
if insultnum == 1:
	print("My middle finger salutes you")
if insultnum == 2:
	print("People always say I act like i dont give a shit. Im not acting")
if insultnum == 3:
	print("You dont have to die to be dead to me, I have Mental funerals on a daily basis")
if insultnum == 4:
	print("Life is full of dissapointments and I just added you to the list")
print()
print("Well, im done, Ill see you later")
print("HIT ENTER TO END TASK")
input()
print("POWERING DOWN...")