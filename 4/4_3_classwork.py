#3.  Написати скрипт, який обчислить факторіал введеного числа.

def factorial(num):
    if num == 0:
        print ('Equals 1')
    elif num <0:
        print('Does not exist')
    else:
        for i in range(1,num+1):
            f= i *i
        print(f)
        
print(factorial(3))
print(factorial(0))
print(factorial(-1))