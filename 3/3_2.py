#Задано чотирицифрове натуральне число. 
digit = 1234
#Знайти добуток цифр цього числа.
mult = str(digit).split()
for m in mult:
    m = int(m) * int (m)
print(m)

#Записати число в реверсному порядку.
reverse = int(str(digit)[::-1])
print(reverse)
#Посортувати цифри, що входять в дане число
res = [int(x) for x in str(digit)]
res.sort()
print(res)
