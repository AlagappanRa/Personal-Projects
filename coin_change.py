# coin change with identity instead of printing the actual result itself.

tup = (2, 3, 5)

def counter(partial_ans):
    x, y ,z = 0, 0, 0
    for element in partial_ans:
        if element == 1:
            x += 1
                
        elif element == 2:
            y += 1
                
        else:
            z += 1
    return x,y,z
    

def cc_listing(a, n, partial_ans, tup):
    if a == 0:
        return (partial_ans),
        
    elif a < 0 :
        return ()

    elif n == 0:
        return (),
            
    else:
        return cc_listing(a-tup[n-1], n, partial_ans + (tup[n-1],), tup) + \
               cc_listing(a, n-1, partial_ans, tup)


print(cc_listing(20, 3, (), tup))

length = list(range(1,11))
price = [1,5,7,9,10,17,17,20,24,30]
d = {k:v for k,v in zip(length, price)}

def cut_rod(a):
    if a in length:
        n = length.index(a) + 1
    else:
        n = len(length) 
        
    def inner_recursion(a, n, partial_ans):
        if a == 0:
            return [partial_ans]
        
        elif a < 0 :
            return []

        elif n == 0:
            return []
            
        else:
            return inner_recursion(a-length[n-1], n, partial_ans + d[length[n-1]]) + \
                   inner_recursion(a, n-1, partial_ans)

    return max(inner_recursion(a, n, 0))

# remember to sort the tuple first before entering the loop
