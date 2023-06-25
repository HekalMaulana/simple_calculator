# Calculator

# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2

# Dictionary of calculator operations
def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    # User input first number, second number, and the operation
    num1 = float(input("What's the first number?: "))

    for key_operations in operations:
        print(key_operations)

    end_of_calculate = False

    # Logic of calculator
    while not end_of_calculate:
        operation_choose = input("What's operation do you wanna choose?: ")
        num2 = float(input("What's the second number?: "))
        operation = operations[operation_choose]
        result = operation(num1, num2)

        # result
        print(f"{num1} {operation_choose} {num2} = {round(result, 2)}")
        num1 = result

        continue_operation = input(f"Continue with '{num1}'. Type 'y' if continue, type 'n' if continue with another number, or type 'exit' for exit the program ?:  ")

        # if statement logic of calc
        if continue_operation == 'n':
            end_of_calculate = True
            calculator()
        elif continue_operation == 'exit':
            end_of_calculate = True
            print("Thank's for use this simple calc")
        else:
            end_of_calculate = False

calculator()
