"""A small calculator that accepts two numbers and an operation."""

# Convert each number before asking for the operation so invalid input is caught.
try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
except ValueError:
    print("Please enter valid numbers.")
else:
    operation = input("Choose an operation (+, -, *, /): ").strip()

    # Match the symbol to an operation and leave result empty for an error.
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Cannot divide by zero.")
            result = None
        else:
            result = first_number / second_number
    else:
        print("That operation is not supported.")
        result = None

    if result is not None:
        print(f"{first_number:g} {operation} {second_number:g} = {result:g}")
