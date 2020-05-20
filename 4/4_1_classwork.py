#1. Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.
num1 = int(input("Please put the number1 : "))
num2 = int(input("Please put the number1 : "))

if num1>num2:
    max_v, min_v = num1, num2
    print("max number is {} and min number is {}".format(max_v,min_v))
elif num1 == num2:
    max_v, max_v = num1, num2
    print("They are both equal")
else:
    max_v, min_v = num2, num1
    print("max number is {} and min number is {}".format(max_v,min_v))






