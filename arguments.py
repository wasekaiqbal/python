'''
print("TIP CALCULATION USING ARGUMENTS")

def total_calc(bill_amount,tip_perc):
    total = bill_amount*(1+0.01*tip_perc)
    total = round(total,2)
    print(f"please pay tk {total}")

bil= int(input("enter your bill: "))
tip = int(input("enetr percentage of tip: "))

total_calc(bil,tip)'''

'''
print("calculating cube of number which is divisible by 3")

def cube(number):
    return number**3

def by_three(number):
    if number % 3 ==0:
        return cube(number)
    else:
        return False
    
num = int(input("eneter an applicable number: "))

print(by_three(num))'''

print("factorial project using recursion")

def factorial(x):
     if x==1 or x==0:
          return 1 
     else:
          return x*factorial(x-1)
     
check = int(input("enetr number you want to check factorial of :"))

print(f"the factorial of {check} is {factorial(check)}")

