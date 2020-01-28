from random import randrange as rand
a=rand(0,10)
b=rand(0,10)
c=rand(0,10)
if a > b:
    print("Неплохо!")
elif a < b:
    print("Плохо!")
elif a == b:
   print ("Это ещё не всё")
   print(b,a+b)
if (a + b) < b:
        print("Великолепно!!!")
    elif (a + b) > b:
        print("Ужасно!!!")
    elif (a + b) == b:
        print("Всё пропало!")

