'''
print("conditional sentence")

num = int(input("input a bumber to verify: "))
if num > 0:
    print(num, "is a positive number")

if num < 0:
    print(num, "is a negative number")

    '''

''' print("determination of profit or loss")
cost_price = float(input("please enter the cost price of your product: "))
selling_price = float(input("please enter your selling price: "))

if (selling_price > cost_price):
    amount = selling_price - cost_price
    print(f"your total profit is {amount}")

else: 
    print("you have a loss in business!")
    '''
'''
print("determining whether the given number is grther than 15 or smaller than 15")
num1 = int(input("enter the number you wanrt to verify:"))
if num1 > 15:
    print(num1, "is greater than 15")

else:
    print(num1, "is smaller than 15")
    '''

print("checking odd and even numbers")
num2 = int(input("enter the number to verify odd or even: "))

if num2%2==0:
    print(num2, "is an even number")

else:
    print(num2, " is an odd number")
