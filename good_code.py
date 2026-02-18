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


def get_number(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please type a number (example: 3 or 3.5).")


def get_operation():
    while True:
        op = input("Choose (+, -, *, /) or q to quit: ").strip().lower()
        if op in {"+", "-", "*", "/", "q"}:
            return op
        print("Please choose one of: +  -  *  /  q")


def main():
    print("Simple Calculator")
    print("Type two numbers and pick an operation.\n")

    while True:
        op = get_operation()
        if op == "q":
            print("Bye!")
            break

        a = get_number("First number: ")
        b = get_number("Second number: ")

        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        else:
            result = divide(a, b)
            if result is None:
                print("Cannot divide by zero.\n")
                continue

        print(f"Result: {result}\n")


if __name__ == "__main__":
    main()
