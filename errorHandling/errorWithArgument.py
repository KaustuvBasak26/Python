#!/usr/bin/python

def temp_convert(var):
	try:
		return int(var)
	except ValueError as Argument:
		print("The argument doesnot contain numbers\n",Argument)

temp_convert("xyz")
