def ls (a, b, c):
    return(a, b, c) 

ch =input('введите число: ')# вводим число
mi =input('введите число: ')# вводим число
sec =input('введите число: ')# вводим число

ch = int(ch)# переводим строку в число
mi = int(mi)# переводим строку в число
sec =  int(sec)# переводим строку в число
ch_1=float(ch * 3600)
mi_1=float(ch * 60)

print('часы: ' ,ch, '---  секунд: ' ,ch_1,  )
print('минуты: ' ,mi, '---  секунд: ' ,mi_1, )
print('секунды: ' ,sec,)

print('сумма секунд:  ' ,ch_1 + mi_1 +sec,)


fnc = ls (ch_1, mi_1, sec)