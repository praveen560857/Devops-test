class PatternSumCalculator:
    def __init__(self, digit):
        if not isinstance(digit, int) or digit < 0 or digit > 9:
            raise ValueError("Input must be a single digit (0–9).")
        self.digit = digit

    def calculate(self):
        total = 0
        pattern = ""
        for _ in range(4):
            pattern += str(self.digit)
            total += int(pattern)
        return total


# ----------- Main Program ------------
if __name__ == "__main__":
    try:
        calc = PatternSumCalculator(3)
        print("Result:", calc.calculate())
    except ValueError as e:
        print("Error:", e)
