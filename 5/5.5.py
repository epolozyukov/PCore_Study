#Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

#ex 1
def count_sheeps(sheep):
    count = 0
    for x in sheep:
        if x:
            count += 1
    return count


sheep = [True, True, True, True, False]

print(count_sheeps(sheep))

#ex 2
def count_sheep2(sheep):
    return sheep.count(True)

print(count_sheep2(sheep))