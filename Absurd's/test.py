# <- is used to comment code, for others to understand
print "Hello, Python!"

print "a = 2 + 2"
a = 2 + 2
# this is how to print a string and a number
# the str function makes it a string
# + plus puts them together
print ("a = " + str(a))
b = 6
c = 12
d = 324
# use of commas to separate variables
print a, b, c, d
# this is what happens when you add parentheses
print (a, b, c, d)

# This is what they call a for loop, in Csci (Computer Science)
# Runs with x starting at ONE but ENDS onces x is lower than FIVE and will keep
# doing whatever is below the for statement until condition is false (1 < 5).
# Hello will be printed out 4 times.
for x in range(1,5):
	print ("Hello " + str(x))

# the %% is to format, the 2 after the decimal will only take 2 decimal places
# I'm not too sure that the zero in 0.2 does, I think it has to do with spacing
# f stands for float I believe
s = "Numbers formatting: %0.2f"% (356.08977)
print (s)


# BOOLEANS or BOOL --------------------------------------------------------------------------------
# when using True and False, that variable is of type bool
test1 = (True & False)
print ("True AND False = " + str(test1))

test2 = (True | False)
print ("True OR False = " + str(test2))

test3 = test1 & test2
print("False AND True = " + str(test3))

