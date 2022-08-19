memoize_table = {}

def memoize(f, name):
    if name not in memoize_table:
        memoize_table[name] = {}
    table = memoize_table[name]
    def helper(*args):
        if args in table:
            return table[args]
        else:
            result = f(*args)
            table[args] = result
            return result
    return helper

def collatz_distance_memo(n):
    def helper(n):
        if n <= 1:
            return 0
        else:
            if n%2 == 0:
                return 1 + collatz_distance_memo(n/2) 
            else:
                return 1 + collatz_distance_memo(3*n+1)
    return memoize(helper, "store")(n)

def max_collatz_distance_memo(n):
    def helper(n):
        if n <= 1:
            return collatz_distance_memo(1)
    
        else:
            return max([collatz_distance_memo(n)] + [max_collatz_distance_memo(n-1)])
    return memoize(helper, "store2")(n)

def collatzLenUtil(n, collLenMap):
     
    # If value already
    # computed, return it
    if n in collLenMap:
        return collLenMap[n]
     
    # Base case
    if(n == 1):
        collLenMap[n] = 0
 
    # Even case
    elif(n % 2 == 0):
        collLenMap[n] \
        = 1 \
           + collatzLenUtil(n//2, collLenMap)
 
    # Odd case
    else:
        collLenMap[n] \
        = 1 \
          + collatzLenUtil(3 * n + 1, collLenMap)
     
    return collLenMap[n]
 
def max_collatz_distance_memo2(n):
     
    # Declare empty Map / Dict
    # to store collatz lengths
    collLenMap = {}
     
    collatzLenUtil(n, collLenMap)
 
    # Initialise ans and
    # its collatz length
    num, l =-1, 0
     
    for i in range(1, n + 1):
         
        # If value not already computed,
        # pass Dict to Helper function
        # and calculate and store value
        if i not in collLenMap:
            collatzLenUtil(i, collLenMap)
         
        cLen = collLenMap[i]
        if l < cLen:
            l = cLen
            num = i
     
    # Return ans and (not done)
    # its collatz length
    return l

table = {}
counter = 0
def collatz_distance_memo2(n):
    global counter
    counter += 1
    if n == 1:
        return counter + 1
    else:
        if n in table:
            return table[n]
        else:
            if n%2 == 0:
                cc = collatz_distance_memo(n/2)
                table[n] = cc
                return cc
            else:
                cc = collatz_distance_memo(3*n + 1)
                table[n] = cc
                return cc
    

# finally is always executed regardless of except statement

