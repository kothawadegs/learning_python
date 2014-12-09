[8, 5, 3] + [4, 2, 1]
print[8, 5, 3] + [4, 2, 1]

x = 8
if x < 5:
	y = -1
	z = 5
elif x > 5:
	y = 1
	z = 11
else:
	y = 0
	z = 10
print (x, y, z)

p = 8
if p < 8:
	q = 6
	r = 3
elif p > 8:
	q = 2
	r = 22
else:
	q = 2
	r = 0
print(p, q, r)
a, b, c, d = 5, 8, 0, 200
while c > d:
	a = a + d
	c = c - d
if c < d + 3:
	b = b + c
	c = 0
else:
	b = b + d + 3
	c = c - d - 2
print (c, d)

item_list = [3, "string1", 23, 14.0, "string2", 49, 64, 70]
for x in item_list:
	if not isinstance(x, int):
continue
if not x % 7:
	print ("found an integer divisible by seven: %d" % x)
break
   


    
