def triangle(n):
    if n == 1:
        return "*"
    
    result = ""
    if n %2 == 0:
        for i in range(1,n-2):
            result += "* "*i + "\n" + " *"*i + "\n"
        return result
    else:
        for i in range(1,n-1):
            result += "* "*i + "\n" + " *"*i + "\n"
        result += "* "*(n-1)
        return result
        
print(triangle(4))
