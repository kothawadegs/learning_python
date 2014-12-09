'#class calculator'


def add(a, b):
	"this function adds two numbers"
	return a + b


def subtract(a, b):
	"this function subtracts two numbers"
	return a - b


def multiply(a, b):
	"this function multiplies two numbers"
	return a * b


def divide(a, b):
	"this function divides two numbers"
	return a / b


print ("select operation")
print ("add")
print ("subtract")
print ("multiply")
print ("divide")

operation = raw_input("Enter input ("
add
"/"
subtract
"/"
multiply
"/"
divide
")": )

a = raw_input(int("Enter value of 'a' : "))
b = raw_input(int("Enter value of 'b' : "))

if operation == '1':
	print "%s + %s = %s"(a, b, add(a, b))

elif operation == '2':
	print "%s - %s = %s"(a, b, subtract(a, b))

elif operation == '3':
	print "%s * %s = %s"(a, b, multiply(a, b))

elif operation == '4':
	print "%s / %s = %s"(a, b, divide(a, b))

else:
	print("Invalid operation")
