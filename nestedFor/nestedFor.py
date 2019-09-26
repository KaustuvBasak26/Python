#!/usr/bin/python

var = 2
while(var < 100):
	i = 2
	while(i <= (var/i)):
		if not(var%i): break
		i = i+1;
	if(i > var/i): print(var,"is a prime number")
	var = var+1

print("Good Bye!")

'''i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print (i, " is prime")
   i = i + 1

print ("Good bye!")'''
