Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup=(21,36,14,25)
>>> tup
(21, 36, 14, 25)
>>> tup[36]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tup[36]
IndexError: tuple index out of range
>>> tup[1]
36
>>> tup[1]=33
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tup[1]=33
TypeError: 'tuple' object does not support item assignment
>>> set={22,25,14,21,5}
>>> s
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> set
{5, 14, 21, 22, 25}
>>> set
{5, 14, 21, 22, 25}
>>> s={25,14,98,63,75,98}
>>> s
{98, 75, 14, 25, 63}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>> s.

