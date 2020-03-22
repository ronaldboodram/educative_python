from _collections import OrderedDict

dict1 = OrderedDict()

dict1['k1'] = 'v1'
dict1['k2'] = 'v2'

dict2 = {}
dict2[1] = 'v1'
dict2[2] = 'v2'

dict3 = {
    'k1': {'k11': 'v11'},
    'k3': {'k33': 'v33'},
    'k2': {'k22': 'v22'}
}

dict1['k3'] = 'i3'

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
      "Gibrael": {"age": 10, "address": "Sesimbra"},
      "Susan": {"age": 11, "address": "Lisbon"},
      "Charles": {"age": 9, "address": "Sesimbra"},
  }

# use the items() method to return a dictionary's keys their values
for k, v in dict1.items():
    print(k, v)

# to iterate over the values
for v in dict2.values():
    print(v)

# to iterate over the keys:
for k in dict3:
    print(k)

# to iterate over a nested dictionary, just remember that the value of
# the parent dictionary is second dictionary that you must extract the key,value pair from

for k1, v1 in dict3.items():
    print(k1)
    for k2, v2 in v1.items():
        print(k2, v2)

print(len(dict2))


def oldestStudent(ages):
    value = list(ages.values())
    key = list(ages.keys())
    return key[value.index(max(value))]


print(oldestStudent(ages))


def updateAges(ages, n):
    # Write your code here
    for k, v in ages.items():
        ages[k] = v + n
    return ages

def find_students(address, students):
    l = []
    for k1, v1 in students.items():
        if v1['address'] == address:
            l.append(k1)
    return sorted(l)

print(find_students('Lisbon', students))
print(sorted(ages))
print(ages)