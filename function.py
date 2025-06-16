'''
def message():
    print("how are you?")
    print("you good?")

message()  

def weather(spring,autumn):
    print("the weather is pleasent in",spring)
    print("the weather is pleasent in",autumn,"too")

weather("spring","autumn") '''

print("BASIC MATHEMATICAL CALCULATION USING FUNCTION")

def add(p,q):
    return p+q

def subtract(p,q):
    return p-q

def multiply(p,q):
    return p*q

def divide(p,q):
    return p/q

choice = input("enter your choice of claculation. \na. addition \nb.subtraction \nc.Multiplication \nd.division \nenter: ")

num1= int(input("enter the first digit: "))
num2= int(input("enter the second digit: "))

if choice == 'a':
    print(num1, "+" ,num2,"= " ,add(num1,num2))
elif choice == 'b':
    print(num1, "-" ,num2,"= " ,subtract(num1,num2))
elif choice == 'c':
    print(num1, "x" ,num2,"= " ,multiply(num1,num2))
elif choice == 'd':
    print(num1, "/" ,num2,"= " ,divide(num1,num2))

else:
    print("INCORRECT INPUT ")
