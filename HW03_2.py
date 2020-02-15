from random import randint as rand

a = (int(input( "Довжину списку ")))
b = (int(input("Максимальне значення елементів списку ")))

def spisok (c,d):
    list = []
    for i in range(c):
        list.append(rand(0,d+1))
    return list

print(spisok(a,b))