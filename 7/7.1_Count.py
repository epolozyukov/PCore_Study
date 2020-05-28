#Given an array of integers.
#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#If the input array is empty or null, return an empty array.

def count_positives_sum_negatives(arr):
    positive_count = 0
    negative_sum = 0
    if not arr:
        return []  
    for i in arr:
        if i > 0 :
            positive_count = positive_count + 1
            
        elif i < 0 :
            negative_sum += i              
    return [positive_count,negative_sum]

arr2 = [1,2,-4,3,-9]
arr3 = []
print(count_positives_sum_negatives(arr2))
print(count_positives_sum_negatives(arr3))

#better example
def count_positives_sum_negatives2(arr):
    pos = sum([1 for x in arr if x>0])
    neg = sum([x for x in arr if x<0])
    return [pos,neg] if len(arr) else []

print(count_positives_sum_negatives2(arr2))
print(count_positives_sum_negatives2(arr3))