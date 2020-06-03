#1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, чи введені дані коректні.
num = int(input("PLease put the number: "))
def digit(num):
    try:
        
        if num%2 == 0 :
            return "This is the even number"
        return "this is the odd number"
    except ValueError as e :
        return e

print(digit(num))

#2.

class CustomError(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(self.data)


def person_age():
    try:
        num = int(input("PLease put your age: "))
        if num < 1:
            raise CustomError("Your age can't be less than 1")
        return digit(num)
    except CustomError as e:
        print("We obtain error:", e.data)   


print(person_age())

