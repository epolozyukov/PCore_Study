#2.  Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.

num= int(input("please enter the number : "))

if num%2 == 0:
    print("This number {} is even". format(num))
else:
    print("This number {} is odd". format(num))