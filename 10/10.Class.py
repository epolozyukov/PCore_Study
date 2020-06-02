class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)  #super().__init__(3) 

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

class Rect(Polygon):
    def __init__(self):
        super().__init__(2)
    
    def findArea(self):
        a,b = self.sides
        area = a*b
        print('The area is {}'.format(area))

#r = Rect()
#r.inputSides()
#r.dispSides()
#r.findArea()

#1.  Створити клас машина з атрибутами name,  make, model та методами start та stop, які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.
class Auto:
    def __init__(self, name, made_in, model, speed):
        self.name = name
        self.made_in = made_in
        self.model = model
        self.speed = speed

    def start(self):
        print ("The auto {} with the model {} started".format(self.name, self.model))
    
    def stop(self):
        print ("The auto {} with the model {} stoped".format(self.name, self.model))

    def move(self):
        print("{} moves at the speed {}".format(self.name, self.speed))

bmw = Auto('BMW', 'Germany', 'X5', 100)
bmw.start()
bmw.stop()
bmw.move()

#2.  Створити клас особа,  в якому конструктор встановлює ім’я, а метод info виводить повідомлення “Hello, my name is {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль,  в якому конструктор встановлює ім’я, а метод move виводить повідомлення 
#{ім’я конкретного екземпляра класу}  moves at the speed {speed(цей параметр метод moveотримує як вхідний)} km / h

class Person:
    def __init__(self, name):
        self.name = name
        
    def info(self):
        print("Hello, my name is {}".format(self.name))
        
val = Person("Valik")
val.info()