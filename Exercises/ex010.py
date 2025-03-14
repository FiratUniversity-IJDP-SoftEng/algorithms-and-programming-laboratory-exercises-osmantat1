# Your Student ID:230543002
# Your Name and Surname:Osman Tat
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        print("Result:", num1 / num2 if num2 != 0 else "Error: Division by zero")
    else:
        print("Invalid operation!")
    again = input("Do another calculation? (yes/no): ").lower()
    if again != "yes":
        break
