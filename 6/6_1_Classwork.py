#1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 

def avr (*args):
    return sum(args)/len(args)

print(avr(1,2,3))


#3.  Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.

def max (a,b):
    """
    this func helps to find max element from two parameters
    """
    if a>b:
        return (f"max {a}")
    elif a==b:
        return ('They are equal')
    return (f"max {b}")

print(max(1,2))
print(max.__doc__)

#4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)

PI = 3.14

def square (type, *args):
    if type == 'triangle':
        return 0.5*args[0]*args[1]
    elif type == 'rect':
        return args[0]*args[1]
    elif type == 'circle':
        return PI*args[0]*args[0]

print(square('triangle',2,2))
print(square('rect',2,3))
print(square('circle',2))

#4 example #2
def square_2():
    num = int(input("To calculate the square, please put the number 1 - triangle, 2 - rect, 3 - circle:"))
    if num==1:
        square_triangle()

def square_triangle():
    a = float(input('You chose triangle, now put figure for a: '))
    h = float(input('You chose triangle, now put figure for h: '))
    s = a*h
    return s


print(square_2())