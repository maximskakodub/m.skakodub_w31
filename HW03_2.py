from random import randint as rand

a = (int(input( "Введіть бажану довжину списку ")))
b = (int(input("Введіть бажане максимальне значення елементів списку ")))

def spisok (x,y):
    list = []
    for i in range(x):
        list.append(rand(0,y+1))
    return list

print(spisok(a,b))