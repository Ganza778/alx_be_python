def perform_operation(num1,num2,operator):
    if operator == "add":
       return  num1 + num2
    elif  operator == "subtract":
       return num1 - num2
    elif  operator == "multiply":
       return num1 * num2
    elif  operator == "divide":
       if (num2==0):
        print("division by zero is impossible")
       else:
         return num1 / num2
    else:
        return "Invalid operator"
    