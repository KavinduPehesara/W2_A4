class Calculator:

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        return n * Calculator.factorial(n - 1)

    @staticmethod
    def fibonacci(n):
        if n <= 1:
            return n
        return Calculator.fibonacci(n - 1) + Calculator.fibonacci(n - 2)


def main():
    calc = Calculator()  # Create object of the class

    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")

    if choice in ("1", "2"):
        try:
            n = int(input("Enter the number (n): "))

            if choice == "1":
                ans = calc.factorial(n)
            else:
                ans = calc.fibonacci(n)

        except ValueError:
            ans = "Invalid input. Please enter a Number."
    else:
        ans = "Invalid choice Please Choose (1 or 2)"

    print("\nFinal result:", ans)


if __name__ == "__main__":
    main()
