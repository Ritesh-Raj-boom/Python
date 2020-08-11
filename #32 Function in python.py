

# function defination

def greet():
    print('hello')
    print('good morning')

# # function calling
#  greet()
#  greet()

# # 2 fun
#
# def add(x,y):
#     c=x+y
#     return c
#
# result= add(6,9)
# print(result)


# 3 to returne multiple values

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2=add_sub(6,5)
print(result1,result2)


