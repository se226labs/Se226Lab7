import math_utils
def main():
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    op = input("Enter the operator (+, -, *, /, ^, %): ").strip()

    operations = {
        "+": math_utils.add,
        "-": math_utils.subtract,
        "*": math_utils.multiply,
        "/": math_utils.divide,
        "^": math_utils.power,
        "%": math_utils.mod
    }

    if op in operations:
        result = operations[op](x, y)
        print(f"Result: {result}")
    else:
        print("Invalid operator. Please use one of the following: +, -, *, /, ^, %.")

if __name__ == "__main__":
    main()
