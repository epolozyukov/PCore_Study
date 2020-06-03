#4.  Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.

week_days = {1:"Monday", 2:"Tuesday", 3: 'Wendsday', 4:"Thursday",5: "Friday", 6:"Saturday", 7:"Sunday"}
class CustomError(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(self.data)

def day_week():
    try:
        day = int(input("Put the day of the week "))
        if day > 7:
            raise CustomError("Your day can't be more than 7")
        return week_days.get(day)
    except ValueError: 
        print("Caught ValueError Exception") 

print(day_week())