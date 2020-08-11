from array import *

arr=array('i',[])  # Empty array

n=int(input("Enter the len of array"))

for i in range(n):
    x = int(input("Enter the values"))
    arr.append(x)


print(arr)

# To search the element

val = int(input("Enter the vale to search"))

k=0
for e in arr:
    if e==val:
        print("Given no. is found at index",k)
        break
    k += 1
else:
        print("number not found")



#print(arr.index(val)) # to find the index of number