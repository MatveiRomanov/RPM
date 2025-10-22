class FibonacciIterator:
    def __init__(self, max_count=15):

        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration

        if self.count == 0:
            result = self.a
        elif self.count == 1:
            result = self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            result = self.b

        self.count += 1
        return result


def fibonacci_generator(max_count=15):
    a, b = 0, 1
    count = 0

    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1


