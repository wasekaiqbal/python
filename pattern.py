"""
thing= str(input("inout the thing you want to create half pyramid of: "))
n = int(input("please enter the number of rows: "))

for i in range(n):
    for j in range(i+1):
        print(thing, end="")
    print()"""

"""
#creating floyds 
rows = int(input("please enter the total number of rows: "))
num = 1

for i in range(1, rows+1 ):
    for j in range(1, i+1):
        print(num, end=" ")
        num = num + 1
    print()
    """

#diamond pattern
rowsize = int(input("enter number of rows: "))
if rowsize%2==0:
    halfdiamondrow = int(rowsize/2) # even
else:
    halfdiamondrow = int(rowsize/2)+1 #odd
space = halfdiamondrow - 1
#loop for upper part

for i in range(1, halfdiamondrow +1):
    for j in range(1, space + 1):
        print(end=" ")
    space = space - 1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        #incrementing number at each column
        num = num + 1
    print()
space = 1
#loop for upper part
for i in range(1, halfdiamondrow ):
    for j in range(1, space + 1):
        print(end=" ")
    space = space + 1
    num = 1
    for j in range(1, 2*(halfdiamondrow - i)):
        print(end = str(num))
        #incrementing number at each column
        num = num + 1
    print()
