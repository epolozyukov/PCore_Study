#3.  Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій. Використати блоки else та finally.

def number_div(a,b):
    try:
        result = a / b
    except (ZeroDivisionError, ValueError) as e:
        print(e)
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

a, b = [int(x) for x in input("Enter two value: ").split()]

number_div(a,b)