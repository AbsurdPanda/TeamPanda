print"Hello, for this test, we are going to have you put in two numbers, and choose to, add, subtract, multiply or divid the two numbers."
firstnum = raw_input("What is your first number? - ")
if firstnum.isdigit() != True:
	print"Error, try again."
else:	
	secondnum = raw_input("WHat is your second number? - ")
	if secondnum.isdigit() != True:
		print"Error, try again."
	else:
		op = raw_input("Choose to either (+, -, /, or *): ")
		if op == '+':
			print(int(firstnum) + int(secondnum))
		elif op == '-':
			print(int(firstnum) - int(secondnum))
		elif op == '/':
			print(int(firstnum) / int(secondnum))
		elif op == '*':
			print(int(firstnum) * int(secondnum))
		else:
			print"Error, try again."