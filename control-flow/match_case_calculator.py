num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        addition = num1 + num2
        print("the result is " + str(addition))  
    case "-":
        subtraction = num1 - num2
        print("the result is " + str(subtraction))   
    case "*":
        multiplication = num1 * num2
        print("the result is " + str(multiplication))
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            division =  num1 / num2
            print("the result is " + str(division))
    case _:
        print("invalid option")
            