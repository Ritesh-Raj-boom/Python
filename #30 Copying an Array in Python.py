from numpy import *

arr = array([1,2,3,4,5])
arr1 = array([1,2,3,4,5])
# arr = arr + 5
# print(arr)



#------------- Vectorized Operation-------------

# arr1 = array([1,2,3,4,5])
# arr2 = array([2,5,8,4,6])
#
# arr3=arr1+arr2
#
# print(concatenate([arr1,arr2]))
# #print(arr3)


#-------------  Operations-------------

# print(sin(arr))
# print(cos(arr))
# print(min(arr))
# print(max(arr))
# print(sort(arr))

#-------------  copying array-------------

# #arr2=arr1
# arr2=arr1.view()
#
#
#
# print(arr1)
# print(arr2)
#
# print(id(arr1))
# print(id(arr2))

#----------------Shallow Copy---------------
# arr2=arr1.view()
# arr1[1]=7
#
#
# print(arr1)
# print(arr2)
#
# print(id(arr1))
# print(id(arr2))

#----------------Deep Copy---------------
arr2=arr1.copy()
arr1[1]=7


print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))


#------------------------------Exercise--------------