'''
final review
'''
def deep_reverse(tree):
    if type(tree) == int:
        return tree
    
    if tree == []:
        return []          
    
    if type(tree) == list:
        return deep_reverse(tree[1:]) + [deep_reverse(tree[0])] 
    
print(deep_reverse([1,2,[3,4],[[5,[7,8]]],[6,[7,8],9]]))

def deep_sum(tree):
    def inner_fn(tree):
        if type(tree) == int:
            return [tree]
    
        if tree == []:
            return []          
    
        if type(tree) == list:
            return inner_fn(tree[0]) + inner_fn(tree[1:])

    return sum(inner_fn(tree))

print(deep_sum([1,2,[3,4],[[[5]]],[6,[7,8],9]]))


class Number(object):
    def __init__(self, num):
        self.num = num

    def plus(self, inc):
        try:
            Number(self.num + inc.num)

        except:
            return Number("Undefined")

        else:
            return Number(self.num + inc.num)
        
    def minus(self, inc):
        try:
            Number(self.num- inc.num)
            
        except:
            return Number("Undefined")

        else:
            return Number(self.num- inc.num)

    def times(self, inc):
        try:
            Number(self.num* inc.num)
            
        except:
            return Number("Undefined")

        else:
            return Number(self.num* inc.num)

    def divide(self, inc):
        try:
            Number(self.num/inc.num)

        except:
            return Number("Undefined")

        else:
            return Number(self.num/inc.num)

    def value(self):
        return self.num

    def spell(self):
        if self.num >= 10**7: 
            return "really large number"

        else:
            num_list = ["0","1","2","3","4","5","6","7","8","9"]
            d1 = ["" ,"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            d2 = ["","ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
            d3 = ["hundred", "thousand", "million"]

            d1_m = {num_list[i]: d1[i] for i in range(len(d1))}
            d2_m = {num_list[i]: d2[i] for i in range(len(d2))}
                             
            nums_str_split = list(str(self.num))[::-1]
            n = len(nums_str_split)-1
            translate_list = []

            def recursion(n):
                if n == 0:
                    translate_list.append(d1_m[nums_str_split[n]])
                    return translate_list
                if n == 1:
                    translate_list.append(d2_m[nums_str_split[n]])
                if n == 2:
                    translate_list.append(d1_m[nums_str_split[n]])
                    translate_list.append(d3[0])
                    translate_list.append("and")
                if n == 3:
                    translate_list.append(d1_m[nums_str_split[n]])
                    translate_list.append(d3[1] + ",")
                if n == 4:
                    translate_list.append(d2_m[nums_str_split[n]])
                    
                if n == 5:
                    translate_list.append(d1_m[nums_str_split[n]])
                    translate_list.append(d3[0])
                    translate_list.append("and")
                if n == 6:
                    translate_list.append(d1_m[nums_str_split[n]])
                    translate_list.append(d3[2] + ",")

                return recursion(n-1)
            
            translate_list = recursion(n)
            while '' in translate_list:
                translate_list.remove('')
                
            return ' '.join(translate_list)
   
seventeen = Number(17)
four = Number(4)
zero = Number(0)
thirteen = seventeen.minus(four)
fiftytwo = thirteen.times(four)
blackjack=seventeen.plus(four)
something=blackjack.divide(zero)
another_thing=blackjack.plus(something)
something_else=another_thing.divide(blackjack)


def power_set(lst):
    pow_set = []
    t = -1
    init_lst = lst
    def recursion(lst, t):
        if not lst:
            return [init_lst] + pow_set
        else:
            for i in range(len(lst)):
                curr_lst = lst.copy()
                curr_lst.remove(lst[i])
                if curr_lst not in pow_set:
                    pow_set.append(curr_lst) 
            
            t += 1
            return recursion(pow_set[t], t)
            
    return recursion(lst, t)
            
print(power_set([1,2,3]))


def power_set_check(lst):
    init, elem = 0, 0
    for i in lst:
        if len(i) > init:
            init = len(i)
            elem = i

    pow_set = power_set(elem)
    for x in pow_set:
        if x not in lst:
            return False if lst != [[]] else True

    return True   

print(power_set_check([[]]))

def enumerate_interval(min, max):
    return list(range(min, max+1))

def map(fn, seq):
    if seq == []:
        return []
    else:
        return [fn(seq[0]),] + map(fn, seq[1:])

def filter(pred, seq):
    if seq == []:
        return []
    elif pred(seq[0]):
        return [seq[0],] + filter(pred, seq[1:])
    else:
        return filter(pred, seq[1:])

def accumulate(fn, initial, seq):
    if seq == []:
        return initial
    else:
        return fn(seq[0], 
                  accumulate(fn, initial, seq[1:]))

# accumulate works on sequences within sequences such that a fn is applied on them. aka if [(1,2,3),(4,5,6),(7,8,9)] if you want to flatten
# it, you use accumulate with init = []. accumulate_n works such that you can apply fns to terms within the sequences and return them
# just like zip. Revise zip, accumulate_n, accumulate equivalents 

# Leave your answers below   
    
def part_i():
    '''code for [1, 2, 3, 4, 5, 6, 7, 8]'''
    return enumerate_interval(1,8)

def part_ii():
    '''code for [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]'''
    return map(lambda x: x*5, enumerate_interval(1,12))

def part_iii():
    '''code for [1, 9, 25, 49, 81, 121]'''
    return map(lambda x: x**2, filter(lambda x: x%2 != 0, enumerate_interval(1, 11)))

def part_iv():
    '''code for [1, 1, 9, 2, 25, 3, 49, 4, 81, 5]'''
    return accumulate(lambda x,y: x+y, [], map(lambda x: [(x*2 - 1)**2, x], enumerate_interval(1,5)))

def part_v():
    '''code for [20, 16, 14, 10, 8, 4, 2]'''
    return accumulate(lambda x,y: y + [x], [] , map(lambda x: x*2, filter(lambda x: x%3 != 0, enumerate_interval(1,10))))

print("part i : ",part_i())
print("part ii : ", part_ii())
print("part iii : ", part_iii())
print("part iv : ", part_iv())
print("part v : ", part_v())        

def make_stack():
    stack = []
    def msg_reader(*args):
        if args[0] == "push":
            stack.append(args[1])

        elif args[0] == "peek":
            return stack[-1]

        elif args[0] == "pop":
            return stack.pop(-1)

        elif args[0] == "size":
            return len(stack)

    return msg_reader
    
a = make_stack()
print(a("push", 1))
print(a("push", 2))
print(a("push", 3))
print(a("peek"))
print(a("pop"))
print(a("peek"))
print(a("size"))
    
def prefix_infix(lst):
    def result_formatter(lst):
        if not lst:
            return ()
    
        elif not isinstance(lst,list):
            return lst
    
        else:
            return (result_formatter(lst[1]),) + (result_formatter(lst[0]),) + (result_formatter(lst[2]),)

    result = result_formatter(lst)
    string_result = str(result)
    return string_result.replace("'", "").replace(",", "") 

print(prefix_infix (['+', ['*', 5, 4], ['-', 2, 1]]))
print(prefix_infix(['-',['*',5,4],['-',['/',1,45],['+',1,1]]]))
# "((5 * 4) + (2 - 1))"
# "((5 * 4) - ((1 / 45) - (1 + 1)))"
def unflatten_prefix(lst): # one dimensional
    opr_stack = make_stack()
    num_stack = make_stack()
    final_stack = []
    
    for i in lst:
        if isinstance(i, str):
            opr_stack("push", i)
            final_stack.append("(")

        elif isinstance(i, int):
            num_stack("push", i)
            if num_stack("size") == 2:
                second = num_stack("pop")
                first = num_stack("pop")
                final_stack.append(str(first) + " " + opr_stack("pop") + " " + str(second) + ")")

                if opr_stack("size"):
                    final_stack.append(" " + opr_stack("pop") + " ")
                    
    final_stack.append(")")
    return accumulate(lambda x,y: x + y, "", final_stack)

print("UNFLATTEN PREFIX 1", unflatten_prefix(['-','*',5,4,'-','/',1,45,'+',1,1]))
print("UNFLATTEN PREFIX 2", prefix_infix (['+', ['*', 5, 4], ['-', 2, 1]]))
print("UNFLATTEN PREFIX 3", prefix_infix(['-',['+', ['*', 5, 4], ['-', 2, 1]],['-',['/',1,45],['+',1,1]]]))

def bubble_sort(lst):
    inital_i = len(lst)
    if not lst:
        return lst
    while True:
        for i in range(inital_i - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                no_swap = False
        if not no_swap:
            no_swap = True       # reset if even one time it is False
        else:                    # else break out of the while loop
            break
        inital_i -= 1
    return lst 
print(bubble_sort([5,8,9,8,7,2,1,0,-5]))

def split(n,lst):
    if not lst:
        return [[],[]]
    return [list(filter(lambda x: x <= n, lst)), list(filter(lambda x: x > n, lst))]

print(split(5,[1,10,4,9,7,2,5,8,3,4,9,6,2]))

def selection_sort(a, size):
    lb = 0
    while (lb < size):
        current = a[lb]
        minpos = lb
        for i in range (lb + 1, size):
            if (a[i] < current):
                current = a[i]
                minpos = i
			
        temp = a[minpos]
        a[minpos] = a[lb]
        a[lb] = temp
        print(a)
        lb += 1
    
