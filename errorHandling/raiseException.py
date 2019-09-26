#!/usr/bin/python

def functionName(level):
	if level < 1:
		raise Exception("Invalid level!", level)


try:
	functionName(0)
except Exception as level:
	print(type(level))
	print(level.args)
	x, y = level.args
	print(x)
else:
	"No error!"
