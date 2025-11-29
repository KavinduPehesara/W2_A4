class MathSeries:
    # @staticmethod
    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n - 1)



    # @staticmethod
    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return MathSeries.fibonacci_recursive(n - 1) + MathSeries.fibonacci_recursive(n - 2)

    def get_fibonacci(n):
        list = []
        for i in range(n):
            list.append(MathSeries.fibonacci_recursive(i))
        return list


if __name__ == "__main__":
    obj = MathSeries()
    n = 5
    factorial = MathSeries.factorial_recursive(n)
    fibonacci = MathSeries.fibonacci_recursive(n)
    fibonacci_list = MathSeries.get_fibonacci(n)

    print("Factorial (recursive):", factorial)
    print("Fibonacci (recursive):", fibonacci)
    print("Fibonacci list (recursive):", fibonacci_list)
