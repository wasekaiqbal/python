"""print("SUM OF NATURAL NUMBERS")

n = float(input("please enter the number of terms you want to add : "))

sum = 0
i = 1
while i<=n :
    sum = sum+i
    i = i+1

print("\n sum: ", sum)"""

# infinite loop
'''
i = 0
while i<=0:
    print("HAHAHAHAHAH!! i will run foreverrrrr!!!")
'''

#finding out armstrong number

num = int(input("please enter number you want to check for armstrong eligibility: "))
num1 = int(input("enter the number of digits in your given number: "))

sum = 0
temp = num

while temp>0 :
    digit = temp % 10
    sum += digit ** num1
    temp //= 10

if num == sum:
    print(num, " is an armstong number") 
else:
    print(num, " is not an armstong number")
""" for 153
after 1st loop:
sum = 3**3 = 27
temp=15 
after 2nd loop:
sum = 3**3 + 5**3 = 27 + 125 = 152
temp=1
after 3rd loop:
sum = 3**3 + 5**3 + 1**3 = 27 + 125 + 1**3 = 153
temp=0
"""
 
