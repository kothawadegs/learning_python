x = "gajanan"

In[2]: x
Out[2]: 'gajanan'

In[3]: y = x + "gajanan"

In[4]: y
Out[4]: 'gajanangajanan'

In[5]: y = x + " kothawade"

In[6]:

In[6]: y
Out[6]: 'gajanan kothawade'

In[7]: z = 12

In[8]: y = x + z

In[9]: y = x + str(z)

In[10]: y
Out[10]: 'gajanan12'

In[11]: y = "something%d" % z

In[12]: y
Out[12]: 'something12'

In[13]: x = "te/n/nst"

In[14]: x
Out[14]: 'te/n/nst'

In[16]: print x
te / n / nst

In[17]: print "test/n/ntest"
test / n / ntest

In[18]: cd..
/ home

In[19]:


Python
2.7
.6(default, Mar
22
2014, 22:59:38)
[GCC 4.8.2]
on
linux2
Type
"help", "copyright", "credits" or "license"
for more information.
	>> > x = "te/n/nst"
>> > x
'te/n/nst'
>> > print x
te / n / nst
>> > x =
File
"<stdin>", line
1
x =
^
SyntaxError: invalid
syntax
>> > x = "te/n/nst"
>> > x
'te/n/nst'
>> > print x
te / n / nst
>> > x = "test\t\ttest"
>> > printx
Traceback(most
recent
call
last):
File
"<stdin>", line
1, in < module >
NameError: name
'printx' is not defined
>> > print x
test
test
>> > "gajanan" in "gajanankothawade"
True
>> > 'f' in 'gajanankothawade'
False
>> > x = ["pune", 8, 3.2]
>> > x
['pune', 8, 3.2]
>> > x.append(9)
>> > x
['pune', 8, 3.2, 9]
>> > x.insert(2, 5.365)
>> > x
['pune', 8, 5.365, 3.2, 9]
>> > x.pop(2)
5.365
>> > x
['pune', 8, 3.2, 9]
>> > len
< built - in function
len >
>> > lenth()

>> > len("words")
5
>> > len(x)
4
>> > y = list(x)
>> > y
['pune', 8, 3.2, 9]
>> > y.append(x)
>> > y
['pune', 8, 3.2, 9, ['pune', 8, 3.2, 9]]
>> > y = x + str(z)

>> > x = 'gajanan'
>> > x
'gajanan'
>> > x = "gajanan"
>> > x
'gajanan'
>> > y = x + "kothawade"
>> > y
'gajanankothawade'
>> > y = x + " kothawade"
>> > y
'gajanan kothawade'
>> > z = 15
>> > z
15
>> > y = x + z

>> > y = str(z)
>> > y
'15'
>> > y = x + str(z)
>> > y
'gajanan15'
>> > y = "something%d" % z
>> > y
'something15'
>> > y = "something%f" % z
>> > y
'something15.000000'
>> > y = "something%.3" % z

>> > y = "something%.3f" % z
>> > y
'something15.000'
>> > z = 5.3625
>> > z
5.3625
>> > y = "something%.2f" % z
>> > y
'something5.36'
>> > kh = {}
>> > kh = ["gajanan"] = "satellite"

>> > kh["input"] = "output"
>> > kh["crop"] = "growth"
>> > kh
{'input': 'output', 'crop': 'growth'}
>> >
