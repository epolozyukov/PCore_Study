#Task1
#Define variables a and b. Read values a and b from console and calculate: 
#a + b 
#a - b 
#a * b 
#a / b. 
#Output obtained results.

a = int(input('Enter a number a '))
b = int(input('Enter a number b '))
print(a+b, a-b, a*b, a/b)

#Task2
#Output question “What is your name?“, “How old are you?“, Where do you live?“. Read the answer of user and output next information: 
#“Hello, (answer(name))“, “Your age is  (answer(age))“, “You live in  (answer(city))“   
name = input('What is your name?')
age= input('How old are you?')
city = input('Where do you live?')
print ('Hello {0} ,Your age is {1}, You live in {2}'.format(name, age, city))