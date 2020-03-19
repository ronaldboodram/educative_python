import module_test
import math

# example of importing and using a module
print(module_test.mult(4,2))

def find_gcd(a, b):
    return math.gcd(a,b)

def find_sinecostan(x):
    sine = math.sin(x)
    cos = math.cos(x)
    tan = math.tan(x)
    return [sine, cos, tan]

def find_max(x,y):
    if (x>y):
        return x
    else:
        return y

print(find_gcd(4,8))
print(find_sinecostan(5))

