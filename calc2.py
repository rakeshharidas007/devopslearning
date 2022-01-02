def action1(a , b , operand):
    if operand == "+":
        result = a+b
        return result
    elif operand == "-":
        result = a-b
        return result
    elif operand == "*":
        result=a*b
        return result
    elif operand == "/":
        result=a/b
        return result
    else:
        print(f"you have entered the wrong operand")

opernd=input(f"Enter the operation to be performed: ")
while opernd != "&&":
 a=int(input(f"Enter your 1st number:  "))
 b=int(input(f"Enter your 2nd number: "))
 d = action1(a, b, opernd)
 print(d)
 opernd = input(f"Enter the operation to be performed: ")



#inputing_values(a,b)
#logic(c)
