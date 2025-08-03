def add(a,b):
    sum = a + b
    return f"{a} + {b} = {sum}"

def subtract(a,b):
    sub = a - b
    return f"{a} - {b} = {sub}"

def multiply(a,b):
    multi = a * b
    return f"{a} * {b} = {multi}"

def divide(a,b):
    try:
        div = a / b
        print(f"{a} / {b} = {div}")
    except ZeroDivisionError:
        print("float division by zero")
        print(f"{a} / {b} = None")

def power(a,b):
    pow = a ** b
    return f"{a} ^ {b} = {pow}"

def remainder(a,b):
    rem = a % b
    return f"{a} % {b} = {rem}"

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    symbols = {"+", "-", "*", "/", "^", "%", "#", "$"}
    if choice in symbols:
        if choice in {"#"}:
            choice = -1
            return choice      
        num_1 = (input())
        print(f"Enter first number: {num_1}")
        if num_1.endswith("$"):
            return 0
        elif num_1.endswith("#"):
            return -1
        else:
            try:
                num_1 = float(num_1)            
            except:
                print("Not a valid number,please enter again")
        num_2 = (input())
        print(f"Enter second number: {num_2}")
        if num_2.endswith("$"):
            return 0
        elif num_2.endswith("#"):
            return -1
        else:
            try:
                num_2 = float(num_2)
            except:
                print("Not a valid number,please enter again")
        if choice in {"+"}:
            print(add(num_1,num_2))
        if choice in {"-"}:
            print(subtract(num_1,num_2))
        if choice in {"*"}:
            print(multiply(num_1,num_2))
        if choice in {"/"}:
            divide(num_1,num_2)
        if choice in {"^"}:
            print(power(num_1,num_2))
        if choice in {"%"}:
            print(remainder(num_1,num_2))

    else:
        print("Unrecognized operation")

#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
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
 

  # take input from the user
    choice = str(input("Enter choice(+,-,*,/,^,%,#,$): "))
    print(choice)
    if(select_op(choice) == -1):
        #program ends here
        print("Done. Terminating")
        exit()
