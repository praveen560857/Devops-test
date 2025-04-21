class EvenFibonacciSum:
    def __init__(self, limit):
        self.limit = limit  # number of even Fibonacci numbers to find

    def calculate_sum(self):
        even_sum = 0
        a, b = 0, 1
        count = 0

        while count < self.limit:
            a, b = b, a + b
            if a % 2 == 0:
                even_sum += a
                count += 1

        return even_sum

# ----------- Main Program ------------
if __name__ == "__main__":
    fib = EvenFibonacciSum(100)
    print("Sum of first 100 even Fibonacci numbers:", fib.calculate_sum())
