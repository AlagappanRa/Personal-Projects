###########################################################
##
## Q4, Q5, Q6, Q7 - you are not allowed to use any import function

def print_matrix(matrix):
    for i in range(len(matrix)):
        print (matrix[i])

# Q4        
def make_rotation_matrix(m, n):
    matrix = []
    first_col = [i for i in range(n)]
    final = [first_col]
    for row in range(m-1):
        new = first_col[row + 1:] + first_col[:row + 1]
        final.append(new)

    return final
        

print("* rotation *")
print(" rotation 5x5")
print_matrix(make_rotation_matrix(5,5))
print("")
print(" rotation 6x5")
print_matrix(make_rotation_matrix(6,5))

# Q5
def make_symmetrical_matrix(n):
    first_row = [i for i in range(n)]
    final = [first_row]
    for row in range(n-1):
        select_no = row + 1
        new = [i for i in range(select_no + 1)][::-1] + [i for i in range(1, n-select_no)]
        final.append(new)

    return final

print("")
print("* symmetrical *")
print(" symmetrical 5x5")
print_matrix(make_symmetrical_matrix(5))
print("")
print(" symmetrical 6x6")
print_matrix(make_symmetrical_matrix(6))

# Q6
def make_concentric_matrix(m,n):
    if m % 2 == 0:
        gen_number = int(m/2)
    else:
        gen_number = int(m//2) + 1 # and the copy down m//2 rows only (+1 is the sp, row)

    start_number = 2

    first_row = [0 for i in range(n)]
    output = [first_row]
    for row in range(gen_number -1):
        middle = n - len(list(range(start_number))*2)
        last = list(range(start_number))[::-1]
        if n <= 5 and row == gen_number - 2 and n%2 != 0:
            last = list(range(start_number))[::-1][1:]
        final = list(range(start_number)) + [start_number-1 for i in range(middle)] + last
        start_number += 1
        output.append(final)
        
    if m % 2 == 0:
        for i in output[::-1]:
            output.append(i)
        return output
    else:
        for index,i in enumerate(output[::-1]):
            if index == 0:
                continue
            else:
                output.append(i)
            
        return output

print("")
print("* concentric *")
print(" concentric 3x3")
print_matrix(make_concentric_matrix(3,3))
print("")
print(" concentric 4x4")
print_matrix(make_concentric_matrix(4,4))
print("")
print(" concentric 5x5")
print_matrix(make_concentric_matrix(5,5))
print("")
print(" concentric 5x6")
print_matrix(make_concentric_matrix(5,6))
print("")
print(" concentric 5x10")
print_matrix(make_concentric_matrix(5,10))

# Q7
def make_diamond_matrix(m,n):
    if n%2 == 0:
        end_number = int(n/2)
    else:
        end_number = int(n//2) + 1

    start_number = 0
    output = []
    if m%2 == 0:
        rg = int(m/2)
    else:
        rg = int(m//2) + 1
        
    for k in range(rg):
        next_row = [i for i in range(start_number, end_number)] + [i for i in range(start_number, end_number - 1)][::-1]
        start_number += 1
        end_number += 1
        output.append(next_row)

    if m % 2 == 0:
        for i in output[::-1]:
            output.append(i)
        return output
    
    else:
        for index,i in enumerate(output[::-1]):
            if index == 0:
                continue
            else:
                output.append(i)
            
        return output
        
        
print("")
print("* diamond *")
print(" diamond 7x7")
print_matrix(make_diamond_matrix(7,7))
print("")
print(" diamond 8x8")
print_matrix(make_diamond_matrix(8,8))
print("")
print(" diamond 9x9")
print_matrix(make_diamond_matrix(9,9))
print("")
print(" diamond 7x8")
print_matrix(make_diamond_matrix(7,8))
print("")
print(" diamond 8x7")
print_matrix(make_diamond_matrix(8,7))
print("")

