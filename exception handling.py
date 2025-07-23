''' print("testing error handling")

try:
    num = int(input("enter a number: "))
    print("the number entered is: ", num)

#if mistake is made in try then it will move to except section

except ValueError as ex:
    print ("exception:", ex)
'''
'''
try:
    num1,num2 = eval(input("enter teo numbers, separated by a comma: " ))
    result = num1/num2
    print("result is", result)

except ZeroDivisionError:
    print("divisions by 0(zero) is error!! ")

except SyntaxError:
    print("comma is missing. Enter numbers separated by comma like this 1,2")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("this will execute no matter what ")'''


print("printing a word infinite tumes if even number is given as input")
valid = False
while not valid:
    try:
        n=int(input("enter a number: "))
        while n%2==0:

            print("bye")
        valid = True
    except ValueError:
        print("invalid")
