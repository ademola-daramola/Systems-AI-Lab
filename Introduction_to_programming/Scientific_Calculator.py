import math

def scientific_calculator():
    print("--- Advanced Scientific Calculator ---")
    print("Operations: +, -, *, /, sin, cos, tan, log (base 10), ln (natural log), exp, pow")
    print("Type 'quit or stop' to exit.")

    while True:
        user_input = input("\nEnter operation or calculation (e.g., 'sin', '+', 'ln'): ").lower()

        if user_input in ['quit', 'stop']:
            break

        try:
            # Trigonometric and Single-Input Functions
            if user_input in ['sin', 'cos', 'tan', 'log', 'ln', 'exp']:
                val = float(input("Enter value: "))

                if user_input == 'sin':
                    # math functions use radians; we convert from degrees for ease of use
                    print(f"sin({val})° = {math.sin(math.radians(val))}")
                elif user_input == 'cos':
                    print(f"cos({val})° = {math.cos(math.radians(val))}")
                elif user_input == 'tan':
                    print(f"tan({val})° = {math.tan(math.radians(val))}")
                elif user_input == 'log':
                    print(f"log10({val}) = {math.log10(val)}")
                elif user_input == 'ln':
                    print(f"ln({val}) = {math.log(val)}")
                elif user_input == 'exp':
                    print(f"e^{val} = {math.exp(val)}")

            # Arithmetic and Two-Input Functions
            elif user_input in ['+', '-', '*', '/', 'pow']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if user_input == '+':
                    print(f"Result: {num1 + num2}")
                elif user_input == '-':
                    print(f"Result: {num1 - num2}")
                elif user_input == '*':
                    print(f"Result: {num1 * num2}")
                elif user_input == '/':
                    if num2 == 0:
                        print("Error: Division by zero.")
                    else:
                        print(f"Result: {num1 / num2}")
                elif user_input == 'pow':
                    print(f"{num1} ^ {num2} = {math.pow(num1, num2)}")

            else:
                print("Invalid operation. Please try again.")

        except ValueError:
            print("Error: Invalid numerical input.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    scientific_calculator()