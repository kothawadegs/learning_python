# program to find fibonacci number series..
fibonacci_sequence = []
x, y = 0, 1
while (y < 10):
	fibonacci_sequence.append(x)
	x, y = y, x + y
	print fibonacci_sequence