# Basic Arithmetic Calculator

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    # Prompt the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt for operation choice
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            return
    else:
        print("Invalid operation choice.")
        return

    # Display the result
    print(f"The result of {num1} {operation} {num2} is: {result}")


# Run the calculator
calculator()
