try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("Result is:", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter two numbers separated by a comma.")

except:
    print("Wrong input") 

else:
    print("No exceptions occurred")    

finally:
    print("This is programmed by Mithul")

