#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.


def solution(n):    
    return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])
    

    

print(solution(10))

