Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums=[25,12,36,95,14]
>>> nums
[25, 12, 36, 95, 14]
>>> nums[4]
14
>>> nums[2:]
[36, 95, 14]
>>> nums[-1]
14
>>> nums[-5]
25
>>> names=['navin','kiran','john']
>>> names
['navin', 'kiran', 'john']
>>> values=[9.5,'navin',25]
>>> mil=[nums,names]
>>> mil
[[25, 12, 36, 95, 14], ['navin', 'kiran', 'john']]
>>> nums.append(45)
>>> nums
[25, 12, 36, 95, 14, 45]
>>> nums.insert(2:77)
SyntaxError: invalid syntax
>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 36, 95, 14, 45]
>>> nums.remove(14)
>>> nums
[25, 12, 77, 36, 95, 45]
>>> nums.pop(1)
12
>>> nums
[25, 77, 36, 95, 45]
>>> nums.pop()
45
>>> nums
[25, 77, 36, 95]
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend([29,12,14,36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> min(nums)
12
>>> max(nums)
77
>>> sum(nums)
193
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
>>> 