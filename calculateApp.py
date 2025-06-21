import art
print(art.logo)

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

def calculator():
    num1 = float(input("Enter first number: "))
    while True:
        print("Select operation:")
        print("+. Add")
        print("-. Subtract")
        print("*. Multiply")
        print("/. Divide")
        print("E. Exit")

        operation = input("Enter choice (+, -, *, /): ").lower()

        if operation == 'e':
            print("Goodbye 👋")
            break

        num2 = float(input("Enter next number: "))

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation.")
            continue

        print(f"Result: {num1} {operation} {num2} = {result}")

        cont = input(f"Type 'y' to continue calculating with {result}, or 'n' to start new, or 'e' to exit: ").lower()

        if cont == 'y':
            num1 = result
        elif cont == 'n':
            calculator()
            break
        elif cont == 'e':
            print("Goodbye 👋")
            break
        else:
            print("Invalid input. Exiting.")
            break

calculator()
