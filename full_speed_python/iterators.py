class MyRange:

    def __init__(self, n):
        self.n = n

    def __iter__(self): # returns the iterator object itself
        return self

    def __next__(self): # returns the next item in the sequence
        evenArray = []  # next method returns this list
        for i in range(1, self.n + 1):
            if i % 2 is 0:  # checks if number is even
                value = i
                evenArray.append(i)  # adds the even number to the list
            else:  # number was odd
                i += 1
        return evenArray


for value in MyRange(8):
     print(value)
