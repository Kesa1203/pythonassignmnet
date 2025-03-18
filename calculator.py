Num1 = float (input("Please input your first number:"))
Num2 = float (input("Please input your second number:"))
operation=input("Enter operation (+,-,*,/):")

if operation =='+':
    result = Num1 + Num2
    print(f"{Num1} + {Num2} = {result}")
elif operation =='-':
    result = Num1 - Num2
    print(f"{Num1} - {Num2} = {result}")
elif operation =='*':
    result = Num1 * Num2
    print(f"{Num1} * {Num2} = {result}")
elif operation =='/':
    if Num2 != 0:
        result = Num1 / Num2
        print(f"{Num1} / {Num2} = {result}")
    else: 
        print("Cant divide by zero!")
else:
    print("Error: Invalid Operation")