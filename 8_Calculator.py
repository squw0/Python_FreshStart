
operator = input("Enter an operator (+ - * /): ")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))


if operator not in ["+","-","*","/"]:
    print(f"{operator} is not valid operator try again!")
elif operator == "+":
    sum = number1 + number2
    print(f"{number1} + {number2} = {sum}")
elif operator == "-":
    sub = number1 - number2
    print(f"{number1} - {number2} = {sub}")
elif operator == "*":
    mult = number1 * number2
    print(f"{number1} * {number2} = {mult}")
elif operator == "/":
    if number2 == 0:
        print("You can't divide by 0!")
    else:
        div = number1 / number2
        print(f"{number1} / {number2} = {div}")
else:
    print("Try again!")