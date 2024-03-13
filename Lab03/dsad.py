class FibonacciIterator:
    def __init__(self, steps):
        self.steps = steps
        self.current = 0
        self.next_value = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.steps:
            raise StopIteration
        else:
            result = self.current
            temp = self.current
            self.current = self.next_value
            self.next_value = temp + self.next_value
            self.count += 1
            return result

if __name__ == "__main__":
    steps = 10
    fibonacci_iterator = FibonacciIterator(steps)

    print("Ciąg Fibonacciego ({} kroków):".format(steps))
    for number in fibonacci_iterator:
        print(number)