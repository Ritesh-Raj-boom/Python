# def add(a,b): #>>>> a,b = formal arguments
#     c=a+b
#     print(c)
#
# add(5,6)

# ___________________Actual Arguments--------------
#
# def person(name,age=18):  # here age=18 is default aguments for line 19
#     print(name)
#     print(age)
#
# # #person('ritesh',28)
# #
# # person(28,'ritesh') # it gives an error bcos we did not know the sequence
#
# #person(age=28,name='Ritesh')  #---------------> Key Arguments
#
# person('Ritesh') #----------------------------> Default Arguments



#-------------------- how to take multiple value as arguments-----------

def sum(a,*b):
    print(a)
    print(b)
    c=a
    for i in b:
        c=c+i

    print(c)


sum(5,6,34,78)