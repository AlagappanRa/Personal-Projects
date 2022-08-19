def shift_left_alt(num,n):
    nlist = []
    while num:
        nlist.append(num % 10)
        num //= 10
    numlist = nlist[::-1]
    n = n % (len(numlist))
    
    right_list = numlist[n:]
    left_list  = numlist[:n]
    final_list = right_list + left_list
    
    string = ''
    for i in final_list:
        string += str(i)
        
    return int(string)
    
print(shift_left_alt(12345,7))

def shift_left(num,n):
    total = 0
    a = num
    while a:
        a //= 10
        total += 1
        
    n = n % total
    
    left_str = str(num//(10**(total-n)))
    right_str = str(num%(10**(total-n)))

    return int(right_str + left_str)

print(shift_left(12345,7))

    

