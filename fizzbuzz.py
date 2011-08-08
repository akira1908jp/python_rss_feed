#!/usr/bin/python


for i in range(1,101):
	if not i %  15:
		print "Fizzbuzz"
	elif not i % 3:
		print "Fizz"
	elif not i % 5:
		print "Buzz"
	else:
		print i


