import random
a=(random.randint(0,10))
b=(random.randint(0,10))
c=(random.randint(0,10))
print(a,b,c)

if a>b:
    print("Неплохо!")
if a<b:
    print("Плохо!")
if a==b:
    print("Это ещё не всё")
    if (a+b)<c:
        print("Великолепно!!!")
    if (a+b)>c:
        print("Ужасно!!!")
    if (a+b)==c:
        print("Всё Пропало!!!")
