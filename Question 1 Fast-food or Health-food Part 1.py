'''
REVISION ON HOW TO DO COUNTING CHANGE WITH OVERLAP/WITHOUT OVERLAP
@ deprecated
def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0],  accumulate(fn, initial, seq[1:]))

tup = ('H','F')
def meals(n):
    def cc_listing(a, n, partial_ans, tup): 
        if a == 0:
            return (partial_ans),
        
        elif a < 0 :
            return ""

        elif n == 0:
            return (partial_ans),
            
        else:
            return cc_listing(a-1, n, partial_ans + (tup[n-1],) , tup) + \
                   cc_listing(a, n-1, partial_ans, tup)

    ans = list(map(lambda x: accumulate(lambda x,y : x + y, "", x), cc_listing(n, len(tup), (), tup)))
    list(filter(lambda y: 'FF' not in y, list(filter(lambda x: len(x) == n, ans))))
    return ans
'''
def meals(n):
    if n == 0:
        return 0
    def recursion(n, partial_ans):
        if n == 0:
            return (partial_ans,)
        else:
            return recursion(n-1, partial_ans + "F") + recursion(n-1, partial_ans + "H")
    
    return len(list(filter(lambda x: "FF" not in x, recursion(n, partial_ans = ""))))

for i in range(5):
    print(f"meals {i} : ", meals(i))

def spend(amount, ffcost, hfcost):
    tup = (ffcost, hfcost)
    def cc_listing(amount, tuple_length, partial_ans): 
        if amount == 0:
            return (partial_ans),
        
        elif amount < 0 :
            return ()

        elif tuple_length == 0:
            return (partial_ans),
            
        else:
            return cc_listing(amount-tup[tuple_length-1] , tuple_length, partial_ans + (tup[tuple_length-1],)) + \
                   cc_listing(amount, tuple_length-1, partial_ans)

    answers = cc_listing(amount, len(tup), ())
    max_sum = max(list(map(lambda x: sum(x), answers)))
    filtered_closest_list = list(filter(lambda x: sum(x) == max_sum, answers))
    max_health_count = max(map(lambda x: x.count(hfcost), filtered_closest_list))
    final_answer = list(filter(lambda x: x.count(hfcost) == max_health_count, filtered_closest_list))[0]
    return final_answer.count(ffcost), final_answer.count(hfcost)

print(spend(50, 7, 3))

def max_element(set1, set2):
    if not set1 and not set2:
        return None
    return max(list(set1) + list(set2))

def is_equal_set(set1, set2):
    list(set1).sort()
    list(set2).sort()
    return set(set1) == set(set2)


def union(set1, set2):
    list(set1).sort()
    list(set2).sort()
    set_a, set_b =  set(set1), set(set2)
    return tuple(set_a.union(set_b))

print(is_equal_set((), (1,)))

def symmetric_difference(set1, set2):
    if is_equal_set(set1, set2):
        return ()
    else:
        list(set1).sort()
        list(set2).sort()
        set_a, set_b =  set(set1), set(set2)
        return tuple(set_a.symmetric_difference(set_b))
