def ls (a):
    print(sum(a))# выводим сумму элиментов списка  (a)
    return(a) 

# создаем рандомнные числа и помещаем их в список
from random import randint
a = [randint(1, 20) for i in range(10)] 

print(a)# выводим список, чтобы видеть какие числа в нем существуют
fnc = ls (a)