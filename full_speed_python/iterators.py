class MyRange:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):  # returns the iterator object itself
        return self

    def __next__(self):  # returns the next item in the sequence
        if self.a >= self.b:
            raise StopIteration

        self.a += 1

        return self.a


class Test:

    # Constructor
    def __init__(self, limit):
        self.limit = limit

        # Called when iteration is initialized

    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

            # Else increment and return old value
        self.x = x + 1;
        return x


# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

# count up to n

for i in MyRange(5, 10):
    print(i)
