print("WELCOME")
a= float(input("Enter first number: "))
b= float(input("Enter second number: "))
o= input("Enter the operation to be performed: ")
if o == '+':
    result= a+b
    print("Result: ", result)
elif o == "-":
    result= a-b
    print("Result: ", result)
elif o == "*":
    result= a*b
    print("Result: ", result)
elif o == "/":
    if b != 0:
        result= a/b
        print("Result: ", result)
    else:
        print("ERROR: DIVISION BY ZERO IS NOT ALLOWED.")
else:
    print("INVALID CHOICE")
