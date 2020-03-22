l = [1, 4, 3, 5, 3]
i = 0


def sumList(l):
    sum = 0
    for i in range(0, len(l), 2):
        sum = sum + l[i]
    return sum


print(sumList(l))


# l.sort()
# print(l)
# print(max(l))

def findMaximum(l):
    # write your code here
    m = max(l)
    return [l.index(m), m]


print('index & value of max number:', findMaximum(l))

print(str(len(l)))
print(type('7'))

for n in l:
    print(n)

while i < len(l):
    print(l[i])
    i += 1

for x in range(2, 10, 2):
    print(x)

for index, value in enumerate(l):
    # print("index: " + str(index) + " value: " + str(value))
    print("index:", index, "value:", value)


def reverse(l):
    r = []
    i = len(l) - 1
    while i >= 0:
        r.append(l[i])
        i -= 1
    return r


print(l)
print(reverse(l))


def isSorted(l):
    # write your code here
    m = 0
    for n in l:
        if m <= n:
            m = n
        else:
            return False
    return True


# l.sort()
print(isSorted(l))


def hasDuplicates(l):
    for n in range(len(l)):
        # print('n:',n)
        # print(range(len(l)))
        for m in range(n+1, len(l)):
            # print('m:', m)
            if l[n]==l[m]:
                return True
    return False

print(hasDuplicates(l))


def printEvenOdd(n):
    while (n > 0):
        if (n%2) == 0:
            print("even number", n)
        else:
            print("odd number", n)
        n -= 1

print(printEvenOdd(10))
