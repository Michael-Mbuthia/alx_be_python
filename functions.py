''''
# Ask for user input
name = input("What's your name: ")

def greet(name):
    " Prints a welcome message"
    print(f"Hello {name}, welcome to Mike Expo!!")

greet(name)
greet(name)
greet(name)
greet(name)
greet(name)
'''

'''
" Get user input"
length = int(input("Enter the lenght: "))
width = int(input("Enter the width: "))
def rectangle_area(width, length):
    " Calculate the area"
    area = length * width
    " Prints the area"
    print(f"The area of the rectangle is : {area}")
    
rectangle_area(width, length)
'''

'''
" Get user input"
number = int(input("Enter a number: "))

def checker(number):
    "Use if to check if the number is an even number or odd number"
    if (number % 2) == 0:
        print(f"This is an even number.")
    else:
        print(f"This is an odd number..")

checker(number)
'''