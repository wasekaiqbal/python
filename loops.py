'''
print("sum of series using for loop ")
n = int(input("enter the number upto which you want your arihtmetic series to continue:"))
sum = 0

#here n+1 is used to reflect that loop should continue upto 5 for ex not 4
for i in range(1, n+1):
    sum = sum + i 
    print("\nYOUR REQUIRED SUM IS:", sum)
    '''

'''
print("REVERSE LETTERS USING LOOP")
str = input("please inout the letter you want to reverse: ")

str2=("")

# time for loop at first we will set the balue for loop to as the first ketter and then when it woll be the time of loop for 2nd letter first letter will automatically come after 1st letter due to ging trhough loop 
for i in str:
    str2 = i + str2

print("the original word: ", str)
print("the reversed word: ", str2)
'''

for i in range(20,9,-2):
    print(i)
