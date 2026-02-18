def main():
    print("CALC!!!!")
    x = input("num1: ")
    y = input("num2: ")

    # no input checking
    x = float(x)
    y = float(y)

    z = input("op (+ - * /) : ")

    # DRY is violated (repeat prints and math)
    if z == "+":
        print("doing plus...")
        print("answer is", x + y)
        print("done.")
    elif z == "-":
        print("doing minus...")
        print("answer is", x - y)
        print("done.")
    elif z == "*":
        print("doing times...")
        print("answer is", x * y)
        print("done.")
    elif z == "/":
        # no divide-by-zero handling
        print("doing divide...")
        print("answer is", x / y)
        print("done.")
    else:
        # unclear message
        print("???")

    # random extra stuff (YAGNI violated)
    for i in range(3):
        print("extra line", i)


main()
