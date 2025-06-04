# PRINTING CONSECUTIVE NUMBERS 5 TIMES USING NESTED LOOP

'''i=1

while i <= 10:
    j = 1
    while j <= 20:
        print(j, end=" ")
        j = j+1
    i = i+1
    print()'''

#FINDNG NUMBER OF EACH LETTER
'''str1 = input("please enter a word of your choice: ")
choice= input("please enter thge letter which you want to count: ")

i = 0
count = 0

while (i < len(str1)):
    if (str1[i] == choice):
       count = count +1
    i = i +1
print("the total number of your given letter is", count)'''

# finding prime number using for loop
num= int(input("enter the number you want to chexk as a prime number: "))

for i in range(2,num):
    if num%i == 0:
        print("given number is not a  prime number: ")
        break
else:
    print("given number is a prime number")

