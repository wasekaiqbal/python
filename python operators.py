''' print("BMI CAMCULATION USING ELIF")

height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height/100)**2

if bmi <= 18.4:
    print(f"As you BMI is {bmi}, therefore you are underweight")

elif bmi <= 24.9:
    print(f"As you BMI is {bmi}, therefore you are healthy")

elif bmi <= 29.9:
    print(f"As you BMI is {bmi}, therefore you are overweight")

elif bmi <= 34.9:
    print(f"As you BMI is {bmi}, therefore you are severely overweight")

elif bmi <= 39.9:
    print(f"As you BMI is {bmi}, therefore you are obese")

else:
    print(f"As you BMI is {bmi}, therefore you are severely obese")
    '''

print("USING OR AND AND LOGIC")

a = 20
b = 30
c = -3
d= 0

''' if a and b and c:
    print("all number is greater than 1")

else:
    print("atleast 1 number is smaller than 1")

if a and b and d:
    print("all number is greater than 1")

else:
    print("atleast 1 number is smaller than 1")

if a > b and b < d:
    print("the condition is correct")

else:
    print("the condition is incorrect")

if a < b and b > d:
    print("the condition is correct")

else:
    print("the condition is incorrect")
'''

print(a !=b)
print(b !=c)

a = "python"
b = "coding"

if a !=b :
    print(f" {a} and {b} are different")
          
a = 3
b = 5

if (a==3) != (b==5):
   print("hello")
   
if (a==3) == (b==5):
   print("hello")





