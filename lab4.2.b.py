def addition(a,b):
    if (a==0 or b==0):
        return 0
    elif (a>b):
        return (a+addition(a,b))

print('Addition Example')
a= int(input("Enter a Number1: "))
b= int(input("Enter a Number2: "))
print("Addition =", (a+b))

def subtraction(a,b):
    if (a==0 or b==0):
        return 0
    elif (a>b):
        return (a+subtraction(a,b))
print('Subraction Example')
a= int(input("Enter a Number1: "))
b= int(input("Enter a Number2: "))
print("Subtraction =", (a-b))


