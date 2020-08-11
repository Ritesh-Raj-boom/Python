Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=5
>>> id(num)
1833543664
>>> name='RITESH'
>>> id(name)
14554816
>>> a=10
>>> b=a
>>> a
10
>>> b
10
>>> id(a)
1833543744
>>> id(b)
1833543744
>>> id(10)
1833543744
>>> k=10
>>> id(k)
1833543744
>>> a=9
>>> id(a)
1833543728
>>> b
10
>>> id(b)
1833543744
>>> k=a
>>> id(k)
1833543728
>>> PI=3.14
>>> PI
3.14
>>> PI=3.15
>>> type(PI)
<class 'float'>
>>> type(a)
<class 'int'>
>>> type(name)
<class 'str'>
>>> 