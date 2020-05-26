
def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i = i + 1
        
    return res

print(create_array(4))

#when yuo need to send several arguments  

def create_array2(*args):
    res=[]
    i=1
    j =0
    n= len(args)
    while i<=n: 
        res+=[args[j]]
        n = n-1
        j = j + 1
    return res

print(create_array2(1,6,3,4))