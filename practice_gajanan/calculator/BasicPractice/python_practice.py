fiboSeq = []

x, y = 0, 1

while (y < 1000):
	fiboSeq.append(x)
x, y = y, x + y
print fiboSeq


def returnTwo():
	return20, 30


x, y = returnTwo()
printx, y


def myfunc():
	'''
	I joined kisanhub.
	'''
	# Only
	pass


print myfunc.__doc__

In[50]: for i in [[1, 2, 3], [4, 5], [6, 7]]:
	....:     for j in i:
		....:         if (4 < j <= 6):
		....:             print j

In[52]: for i in range(10):
	....:     if (i % 2):
		....:         pass
	....:     else:
	....:         continue
	....:     print i
	....:



	In[53]: for i in range(50):
		....:     if (i % 5):
			....:         pass
		....:     else:
		....:         continue
		....:     print i

	[54]: def doesNothing():
		....:     pass
		....:

		In[55]: doesNothing()

		In[56]: def kisanHub():
			....:     pass
			....:

			In[57]: kisanHub()

			In[58]: def makeOne():
				....:     return 1
				....:

				In[59]: x = makeOne()

				In[60]: print x
				1

				In[61]: def addTen(myInt):
					....:     myInt += 10
					....:     return myInt
					....:

					In[62]: x = 13

					In[63]: dir()
					Out[63]:


