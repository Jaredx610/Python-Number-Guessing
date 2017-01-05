#!/usr/bin/python
#Jared McDonald
import random
import sys
num = random.randint(1,100)
i = 0

def compareGuess(guess):
	if (guess < num):
		return -1;
	elif (guess == num):
		return 0;
	elif (guess > num):
		return 1;
		
while(i < 6):
	guess = int(input("Guess a number: "));
	res = compareGuess(guess)
	if(res == -1):
		print ("HIGHER")
	elif (res == 0):
		print ("CORRECT!")
		sys.exit()
	else:
		print ("LOWER")
	i = i+1
print ("The number was...")
print(num)