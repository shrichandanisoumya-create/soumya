#calculator.py
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
function=input("Enter the operation you want to perform (+, -, *, /): ")
if function=='+':
    sum=number1+number2
    print("The sum of", number1, "and", number2, "is:", sum)
elif function=='-':
    difference=number1-number2
    print("The difference of", number1, "and", number2, "is:", difference)
elif function=='*':
    product=number1*number2
    print("The product of", number1, "and", number2, "is:", product)
elif function=='/':
    if number2!=0:
        quotient=number1/number2
        print("The quotient of", number1, "and", number2, "is:", quotient)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter a valid operation (+, -, *, /).")