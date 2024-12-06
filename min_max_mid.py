
def ms (a):
    print('минимальное:  ' ,min(a), )# минимальное значение
    print('максимальное:  ' ,max(a), )# максимальное значение
    print('среднее:  ' ,float(sum(a)/2 ), )# среднее значение
    return(a) 
   
from random import randint
p = [randint(1, 10) for i in range(20)] 
print(p)

fnc = ms (p)