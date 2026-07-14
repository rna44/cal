#A simple Python calculator with memory and error handling
memory = 0.0

def safe_divide(a, b):
    if b == 0:
        return None
    

while True:
    print(f"\n--- Current Saved Memory: {memory} ---")
    print("Ops: + , - , * , / | 'quit' to exit")
    
    choice = input("Choose an option: ").strip().lower()
    
    if choice == 'quit':
        print("Goodbye!")
        break
        
    if choice not in ['+', '-', '*', '/']:
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

    if choice == '+':
        result = num1 + num2
    elif choice == '-':
        result = num1 - num2
    elif choice == '*':
        result = num1 * num2
    elif choice == '/':
        result = safe_divide(num1, num2)

    print(f"Result: {result}")
    
   
    if isinstance(result, (int, float)):
        memory = result

