Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3+6
9
>>> 2+5
7
>>> x=2
>>> x+3
5
>>> y=4
>>> x+y
6
>>> x=9
>>> x+y
13
>>> x
9
>>> abc
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> x+10
19
>>> 19+y
23
>>> _+y
27
>>> name='youtube'
>>> name
'youtube'
>>> name+'rocks'
'youtuberocks'
>>> 
>>> name'rock'
SyntaxError: invalid syntax
>>> name[0]
'y'

>>> name[6]
'e'
>>> name[8]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    name[8]
IndexError: string index out of range
>>> name[-1]
'e'
>>> name[-2]
'b'
>>> name[-7]
'y'
>>> name[0:2]
'yo'
>>> name[1:4]
'out'
>>> name[1:]
'outube'
>>> name[:4]
'yout'
>>> name[3:50}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> name[3:50]
'tube'
>>> name[0:3]='my'
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    name[0:3]='my'
TypeError: 'str' object does not support item assignment
>>> name[0]='R'
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    name[0]='R'
TypeError: 'str' object does not support item assignment
>>> 'my '+ name[3:]
'my tube'
>>> may name='Ritesh raj'
SyntaxError: invalid syntax
>>> myname='Ritesh Raj'
>>> len(myname)
10
>>> 