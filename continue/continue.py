#!/usr/bin/python

for letter in "Python":
	if letter == 'h':
		continue
	print("Current letter: ", letter)

var = 10
while var>0:
	var = var-1
	if var == 5:
		continue
	print("Current value: ", var)

print("Good Bye!")
