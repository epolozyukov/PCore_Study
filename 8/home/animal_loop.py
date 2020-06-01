def list_animals(animals):
    la = ''
    for i in range(len(animals)):
        la += str(i + 1) + '. ' + animals[i] + '\n'
    return la


animals = [ 'dog', 'cat', 'elephant' ]

print(list_animals(animals))