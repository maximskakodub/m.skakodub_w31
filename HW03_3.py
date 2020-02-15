import random
def func(a, b, c):
    return {a: random.randint(b, c)}
d=str(input("Напишіть = "))
print((func(d, 0, 100)))
