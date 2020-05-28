#In this kata you will create a function that takes in a list and returns a list with the reverse order.

def reverse_list(l):
  '''return a list with the reverse order of l'''
  return(list(reversed(l)))

print(reverse_list.__doc__)

print(reverse_list([1,2,3,4,444]))

#ex 2
def reverse_list2(l):
    return l[::-1]

print(reverse_list2([1,2,3,4,444]))

#ex3
reverse_list3 = lambda x : x[::-1]
print(reverse_list3([1,2,3,4,444]))