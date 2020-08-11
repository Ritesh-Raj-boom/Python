from numpy import *

# 2-D  array

#  arr1=array([
#     [1,2,3],
#     [4,5,6]
#
# ])
# print(arr1.dtype)
# print(arr1.ndim)     # shows the dimention of array
# print(arr1.shape)    # shows no. of rows and colums
# print(arr1.size)     # no. of total element in array

# change multidimention array in to 1 dimentional array

# arr2=arr1.flatten()
# print(arr2)


# 3-D array
#
# arr1=array([
#
#     [1,2,3,6,2,9],
#     [4,5,6,7,5,3]
#
# ])

# arr2=arr1.flatten()
#
#
# #arr3=arr2.reshape(3,4)      # 3---> rows and 4---> coloums
# #arr3=arr2.reshape(2,2,3)   # 2--> 2D array | 2---> 2 row in each array| 3----> each row has 3 values
#
# print(arr3)

# ------------------------------matrixs-------------------
#
# arr1=array([
#
#     [1,2,3,6],
#     [4,5,6,7]
#
# ])
# #1
# #m = matrix(arr1)
#
# #2
# #m= matrix('1 2 3 4 ; 5 6 7 8')
# m= matrix('1 2 3 ;4 5 6; 1 7 8')
#
#
#
# #print(m)
#
# print(diagonal(m)) # diagonal elements
# print(m.min())     # min value of matrix
# print(m.max())    # max value of matrix

#----------------------multiplication in matrix----------------------

m1=matrix('1 2 3; 6 4 5; 1 6 7 ')
m2=matrix('1 2 3; 6 8 5; 2 6 7 ')

m3=m1*m2

print(m3)

#------------------------------------Exercise-------------------------




