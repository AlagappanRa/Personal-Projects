##def sumT(t, term, next):
##    if t == ():
##        return ()
##    else:
##        return term(t) + sumT(next(t), term, next)
##
##def prefix_sum_reverse(t):
##    return sumT(t,
##                lambda x:(sum(x),),
##                lambda x: x[:-1])
##
##print(prefix_sum_reverse((1,2,3,4,5,6,7,8,9)))
##print(prefix_sum_reverse((1,2,3,4,5,6,7,8,9,10)))

def sumT(t, term, next):
    if t == ():
        return ()
    else:
        return term(t) + sumT(next(t), term, next)

def prefix(t):
    return sumT(t,
                lambda t:(t[0],),
                lambda t:() if len(t)<2 else(t[0]+t[1],)+ t[2:]
                )

def interleave(t1,t2):
    return sumT(t1+t2,
                lambda t:((t[0],t[int(len(t)/2)]),),
                lambda t:t[1:int(len(t)/2)] + t[int(len(t)/2 + 1):] 
                )

def average (t1, t2, t3):
    return sumT((t1, t2, t3),
                lambda t: () if len(t[0]) == 0 else (((t[0][0] + t[1][0] + t[2][0]) /3),),
                lambda t: () if len(t[0]) == 0 else (t[0][1:], t[1][1:], t[2][1:])
                )

print(average((1,2,3),(2,5,3),(9,1,0)))
print(average((1,2,3),(1,2,3),(1,2,3)))
print(prefix((1,2,3,4,5,6,7,8,9)))
print(prefix((1,2,3,4,5,6,7,8,9,10)))
print(interleave((1,2,3),("a","b","c")))
# unable to do with fold right, need fold left.  
