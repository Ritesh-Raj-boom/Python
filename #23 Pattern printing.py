 #Pattern :1

for i in range(4):
    for j in range(4):
        print("# ",end="")

    print()

 #Pattern :2
for i in range(13):
    for j in range(i+1):
        print("# ",end="")

    print()

#  Pattern :3
for i in range(4):
    for j in range(4-i):
        print("# ",end="")

    print()

 #Pattern :4
for i in range(4):
    for j in range(4-i):
        print(" ",end="")
    for k in range(j,4):
        print("#",end="")

    print()