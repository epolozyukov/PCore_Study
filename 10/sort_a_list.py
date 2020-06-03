def sorter(textbooks):
    return sorted(textbooks, key=str.lower)
    

books = ["English", 'algebra']
print(sorter(books))