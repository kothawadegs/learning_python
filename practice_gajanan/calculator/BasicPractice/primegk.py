for x in range(2, 10):
	prime = True
	for n in range(2, x):
		if (x % n == 0):
			prime = False
	if prime:
		print x
