# program to find Fibonacci number series
number = raw_input("Enter quantity of number:")
p = 0
q = 1
# print p
# print q
for s in range(int(number)):
	r = p + q
	print r
	p = q
	q = r