#1.  Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх хеш-прізвищами, використовуючи  більш надійний метод-хешування.

names = ['Sam', 'Don', 'Daniel'] 
for i in range(len(names)): 
    names[i] = hash(names[i]) 
print(names) 

print(map(lambda i: hash(names[i]), names))
print(list(map(hash, names)))


# => [6306819796133686941, 8135353348168144921, -1228887169324443034]

#3. Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список, всі числа якого мають тип даних integer:
#1)  використовуючи метод  append
#2)  використовуючи метод  map

str_list = ['1','2','3','4','5','7']
str_list1= []
for x in str_list:
    str_list1.append(int(x))
print(str_list1)


print(list(map(int,str_list)))

#44. Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
#a) використовуючи функцію map
# b) використовуючи функцію map та lambda
miles = [1,4,5,4]
def mile (x):
    return x *1.6
print(list(map(mile, miles)))
print(list(map(lambda x: x*1.6, miles)))
