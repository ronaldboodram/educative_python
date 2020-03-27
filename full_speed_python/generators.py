def odd(n):
    for i in range(1, n + 1, 1):
        if i % 2 != 0:
            yield i


def reverse(n):
    for i in range(n, -1, -1):
        yield i


# The Fibonacci Sequence is the series of numbers in which the next term is found by adding the two previous terms:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci(n):
    myArray = []
    for i in range(n):
        if i is 0 or i is 1:
            myArray.append(i)
            yield i
        else:
            x = myArray[i - 2] + myArray[i - 1]
            myArray.append(x)
            yield x


for i in fibonacci(8):
    print(i)

for n in odd(8):
    print(n)

for n in reverse(5):
    print(n)