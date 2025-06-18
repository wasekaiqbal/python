print("different areas of different shapes and circumperence of circle")

def circumference(x,y,z):
    return x*y*z

def circle(x,y,):
    return x*y**2

def square(x):
    return x**2

def rec(x,y):
    return x*y

def triangle(x,y,z):
    return x*y*z


choice = input("WHAT DO YOU WANT TO CALCULATE? \na. circumference of circle " \
"\nb.area of circle"  "\nc.area of square" "\nd.area of rectangle" "\ne.area of triangle" \
"\n enter choice: ")

if choice == 'a':
    radius = int(input("enter the radius of circle: "))
    print(f"the circumference of your circle is {circumference(2,3.14,radius)}")
elif choice == 'b':
    radius = int(input("enter the radius of circle: "))
    print(f"the area of your circle is {circle(3.14,radius)}")
elif choice == 'c':
    length = int(input("enter length of your square: "))
    print(f"the area of your square is {square(length)}")
elif choice == 'd':
    length = int(input("enter length of your rectangle: "))
    breadth = int(input("enter width of your rectangle: "))
    print(f"the area of your rectangle is {rec(length,breadth)}")
elif choice == 'e':
    base = int(input("enter base of your triangle: "))
    height = int(input("enter height of your triangle: "))
    print(f"the area of your triangle is {triangle(0.5,base,height)}")
else:
    print("incorrect input. PLEASE TRY AGAIN!!")
