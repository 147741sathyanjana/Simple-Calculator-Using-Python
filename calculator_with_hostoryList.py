# List to store history of operations
history_list = []

# Arithmetic operation functions
def add(a,b):
    result = a + b
    return f"{a} + {b} = {result}"

def subtract(a,b):
    result = a - b
    return f"{a} - {b} = {result}"

def multiply(a,b):
    result = a * b
    return f"{a} * {b} = {result}"

def divide(a,b):
    try:
        result = a / b
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        print("float division by zero")
        return f"{a} / {b} = None"

def power(a,b):
    result = a ** b
    return f"{a} ^ {b} = {result}"

def remainder(a,b):
    try:
        result = a % b
        return f"{a} % {b} = {result}"
    except ZeroDivisionError:
        print("float modulo by zero")
        return f"{a} % {b} = None"

# Function to show history
def show_history():
    if not history_list:
        print("No past calculations to show")
    else:
        for entry in history_list:
            print(entry)

# Operation selector
def select_op(choice):
    if choice in ('+', '-', '*', '/', '^', '%'):
        # Get first number
        num_1 = input()
        print(f"Enter first number: {num_1}")
        if num_1.endswith('$'):
            return 0
        elif num_1.endswith('#'):
            return -1
        try:
            num_1 = float(num_1)
        except:
            print("Not a valid number,please enter again")
            return 0

        # Get second number
        num_2 = input()
        print(f"Enter second number: {num_2}")
        if num_2.endswith('$'):
            return 0
        elif num_2.endswith('#'):
            return -1
        try:
            num_2 = float(num_2)
        except:
            print("Not a valid number,please enter again")
            return 0

        # Perform the operation
        if choice == '+':
            result = add(num_1, num_2)
        elif choice == '-':
            result = subtract(num_1, num_2)
        elif choice == '*':
            result = multiply(num_1, num_2)
        elif choice == '/':
            result = divide(num_1, num_2)
        elif choice == '^':
            result = power(num_1, num_2)
        elif choice == '%':
            result = remainder(num_1, num_2)

        print(result)
        history_list.append(result)

    elif choice == '?':
        show_history()
    elif choice == '#':
        return -1
    elif choice == '$':
        history_list.clear()
    else:
        print("Unrecognized operation")

# Main loop
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ?")

    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if select_op(choice) == -1:
        print("Done. Terminating")
        break
