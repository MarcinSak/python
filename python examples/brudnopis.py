def add(a: int, b: int) -> int:
    return a + b
print(add(5,4))
print(add("5","4"))

def odd(i: int) -> bool: return i%2==0

def ok(s: dict): return s

print(odd(3))
print(odd(4))
print(ok({}))

a = 5
print(f"{a=}")

#operacja morsa := przypisanie wartości
some_list = [1,2,3,4,5,6]
n = len(some_list)
if n > 5:
    print(f"List is too long: {n} elements")
#
if (n := len(some_list)) > 5:
    print(f"List is too long: {n} elements")

#skrócone porównania łańcuchowe:
x = 10
if x > 5 and x < 15:
    print("x is between 5 and 15")
#
if 5 < x < 15:
    print("x is between 5 and 15")

    from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
d['b'] += 2
print(d)

from collections import defaultdict

purchases = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
product_count = defaultdict(int)

for product in purchases:
    product_count[product] += 1
print(purchases)
print(product_count)  

from collections import defaultdict

employees = [
    ('HR', 'John'),
    ('IT', 'Marcin'),
    ('HR', 'Anna'),
    ('IT', 'Aga'),
    ('Finance', 'Dorota')
]

departments = defaultdict(list)

for department, employee in employees:
    departments[department].append(employee)

print(f"{departments=}")
print(departments["HR"][0])
print(departments["IT"][1])


from collections import Counter

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(items)
print(counter)  



squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]



