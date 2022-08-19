def smallest(*args):
    if not args:
        return None
    
    check = len(list(filter(lambda x: x == 0,args)))
    if check == len(args):
        return 0

    lst = []
    lst2 = []
    sorted_args = sorted(list(args))
    for i in sorted_args:
        if i == 0:
            lst.append(i)
        else:
            lst2.append(i)

    for index in range(1,len(lst2)):
        for y in lst:
            lst2.insert(index, y)
            lst.remove(y)
    return eval("".join(list(map(str, lst2))))

def second_smallest(*args):
    if len(args) == 1:
        return None
    if not args:
        return None
    
    check = len(list(filter(lambda x: x == 0,args)))
    if check == len(args):
        return 0

    output = list(str(smallest(*args)))
    output[-1], output[-2] = output[-2],output[-1]
    return eval("".join(output))

print(smallest(5678))
    
























        
        
