#A simple Python calculator with memory and error handling


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b

def main():
    memory = 0.0
    
    while True:

        print(f"\n--- Current Saved Memory: {memory} ---")
        print("Ops: + , - , * , / | 'quit' to exit")

        choice = input("Choose an option: ").strip().lower()

        if choice == "quit":
            print("Goodbye!")
            break

        if choice not in ["+", "-", "*", "/"]:
            print("Invalid choice, please try again.")
            continue

        try:
            num1_input = input("Enter 1st number (or press Enter to use memory): ").strip()
            num1 = memory if num1_input == "" else float(num1_input)

            num2_input = input("Enter 2nd number (or press Enter to use memory): ").strip()
            num2 = memory if num2_input == "" else float(num2_input)

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue


        if choice == "+":
            result = add(num1, num2)

        elif choice == "-":
            result = subtract(num1, num2)

        elif choice == "*":
            result = multiply(num1, num2)

        elif choice == "/":
            result = divide(num1, num2)


        if result is None:
            print("Error: Cannot divide by zero")
            continue

        print(f"Result: {result}")

        memory = result
   
if __name__ == "__main__":
        main()
