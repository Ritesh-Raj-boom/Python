Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> int i=5
SyntaxError: invalid syntax
>>> num=2.5
>>> type(num)
<class 'float'>
>>> num=5
>>> type(num)
<class 'int'>
>>> num=6+9j
>>> type(num)
<class 'complex'>
>>> a=5.6
>>> b=int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k=float(b)
>>> k
5.0
>>> type(k)
<class 'float'>
>>> k=6
>>> c=complex(b,k)
>>> c
(5+6j)
>>> b<k
True
>>> bool=b<k
>>> type(bool)
<class 'bool'>
>>> b>k
False
>>> num=b>k
>>> num
False
>>> type(num)
<class 'bool'>
>>> int(True)
1
>>> int(Flase)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(Flase)
NameError: name 'Flase' is not defined
>>> int(False)
0
>>> lst=[5,6,4,2,3]
>>> lst
[5, 6, 4, 2, 3]
>>> type(lst)
<class 'list'>
>>> tuple={5,6,7,8,2,2}
>>> tuple
{2, 5, 6, 7, 8}
>>> type(tuple)
<class 'set'>
>>> tuple=(5,5,2,5,2,5)
>>> type(tuple)
<class 'tuple'>
>>> str="Ritesh"
>>> type(str)
<class 'str'>
>>> range(0,10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range(10))
<class 'range'>
>>> dictonary={'navin':'mi','Rahul':'iphone','kiran':'onepluse'}
>>> dictonary
{'navin': 'mi', 'Rahul': 'iphone', 'kiran': 'onepluse'}
>>> dictonary.keys()
dict_keys(['navin', 'Rahul', 'kiran'])
>>> dictonary.values()
dict_values(['mi', 'iphone', 'onepluse'])
>>> d['navin']
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d['navin']
NameError: name 'd' is not defined
>>> dictonary['navin']
'mi'
>>> dictonary['Rahul']
'iphone'
>>> dictonary['Rahul']
'iphone'
>>> dictonary.get('kiran')
'onepluse'
>>> 
