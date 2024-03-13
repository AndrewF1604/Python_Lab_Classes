class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imaginary_diff = self.imaginary - other.imaginary
        return ComplexNumber(real_diff, imaginary_diff)

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"

num1 = ComplexNumber(10, 10)
num2 = ComplexNumber(20, -20)

result_addition = num1 + num2
print(f"Sum: {num1} do widzenia")

result_subtraction = num1 - num2
print("Sub:", result_subtraction)