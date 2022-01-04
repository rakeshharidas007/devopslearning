print(f"Welcome to calculator program!")
a=int(input("Enter the first number :  "))
b=int(input("Enter the second number :  "))
operation=input("Enter the operation to be performed: ")
if operation == "+":
    result=a+b
    print(f"The result is {result}")
elif operation == "-":
    result = a - b
    print(f"The result is {result}")
elif operation == "*":
    result=a*b
    print(f"The result is {result}")
elif operation == "/":
    result=a/b
    print(f"The result is {result}")
else:
    print(f"you have entered wrong operation")