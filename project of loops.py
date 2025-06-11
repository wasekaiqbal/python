print("Calculating the power of given number and power")

num1 = int(input("please enter the base number: "))
power = int(input("please enter your power number: "))

mypower = 1

for i in range(1, power+1 ):
    mypower = mypower * num1

print(f"{num1} to the power {power} is {mypower}")  
