#
# i=1
#
# while i<=5:
#     print("ritesh " ,end="")
#     j = 1
#     while j<=4:
#         print("Rocks ",end="")
#         j=j+1
#     i=i+1
#     print()

#----------------------------------Exercise----------------------------
for i in range(1,100):
    if (i%3==0)or(i%5==0):
        continue # to skip the statement
    else:
        print(i)

#----------------------------------Exercise----------------------------

# for i in range(1,5):
#     for j in range(1,6):
#         print("*",end="")
#     print()