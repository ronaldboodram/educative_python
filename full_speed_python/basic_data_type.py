def get_square():
    l1=[x**2 for x in range(0,21) if ((x%2 == 0) and (x%3 != 0 ))]
    return l1

print(get_square())

def list_of_even_odds():
    l1 = [x for x in range(0,21) if x%2 == 0]
    l2 = [y for y in range(0,21) if y%2 != 0]
    return [l1, l2]

print(list_of_even_odds())

# write an entire expression in a list. This is called List Comprehension
print([x*x for x in range(2, 5, 2) if x % 2 == 0])
print([x**3 for x in range(1,21)])
g = [2, 3]
i = [1, 2, 3, 4]
avg = sum(i)/len(i)

print(avg)

for elem in g:
    i.remove(elem)

print(i)


m = ['mango']
l = ['w', 1, 'r', 3.5]
print(l + m)
l.append(m)
print(l)
# print(str(l))
# print(l)
#first index val is inclusive and the last value is exclusive
print(l[1:2])

def change_case(s):
    lower_s = s.lower()
    upper_s = s.upper()
    return [lower_s, upper_s]

print(change_case('aaBBccDFg'))

def find_occurence(s):
    end = (len(s) - 1)
    start = 0
    a = s.find('a')
    b = s.find('b')
    # a = s.find('a', start, end)
    # b = s.find('b', start, end)
    return [a, b]

print(find_occurence('aaacccbbbddd'))

def get_str(s):
    s2 = ''
    for c in s:
        s2 += c*3
    strlen = len(s2)
    return [s, strlen, s2]

print(get_str('acbd'))

# the return statement evaluates the function to true or false
def in_range_again(x,y):
    return (x < 1/3 < y)

print(in_range_again(0.1,0.2))

def in_range(x,y):
    if(x < 1/3 < y):
        return True
    else:
        return False

print(in_range(0.2,0.3))

def parity(n):
    return n%2

print(str(parity(5)))

def math_op():
    division = 3 / 2
    floor_division = 3 // 2
    modulus = 3 % 2
    power = 3 ** 2
    p = pow(3, 2)
    return [division, floor_division, modulus, power, p]


[div, fl, md, pwer, w] = math_op()

print(div)
print(fl)
print(md)
print(pwer)
print(w)