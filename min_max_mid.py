
def ms (a):

        print('минимальное:  ' ,min(a), )# минимальное значение
        print('максимальное:  ' ,max(a), )# максимальное значение
        print('среднее:  ' ,float(sum(a)/len(a) ), )# среднее значение
        return(a) 




n = input('введите кол-во элиментов:  ')
from random import randint
p = [randint(1, n+1) for i in range(20)] 
print(p)


#for i in range(1, data[])



fnc = ms (p)